'''

meetodid:
* hetkehind
* tänased hinnad
* homsed hinnad

* päringu meetod

* https://dashboard.elering.ee/assets/swagger-ui/index.html
* https://dashboard.elering.ee/api/nps/price?start=2020-05-31T20%3A59%3A59.999Z&end=2020-06-30T20%3A59%3A59.999Z
* https://dashboard.elering.ee/api/nps/price/EE/latest
* https://dashboard.elering.ee/api/nps/price/EE/current
'''


def latest():
    pass

def current():
    pass

def price():
    pass

import datetime

import Request

def hangi_homsed_elektrihinnad() -> list[dict[str, object]]:  # Määrab funktsiooni, mis tagastab Eleringi API-st homse Eesti piirkonna hinnad.
    """Tagastab homse Eesti börsihinna intervallid kujul aeg ja hind EUR/MWh."""  # Kirjeldab funktsiooni tagastusväärtust.
    eesti_ajavooend = ZoneInfo("Europe/Tallinn")  # Kasutab Eesti kohalikku aega, et suve- ja talveaeg oleksid korrektselt arvestatud.
    praegu = datetime.now(eesti_ajavooend)  # Võtab praeguse kuupäeva ja kellaaja Eesti ajavööndis.
    homse_algus = (praegu + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)  # Leiab homse päeva kohaliku alguse kell 00.00.
    ulehomse_algus = homse_algus + timedelta(days=1)  # Leiab ülehomse päeva kohaliku alguse, mis on homse päeva lõpp-piir.
    parameetrid = urlencode({"start": homse_algus.astimezone(ZoneInfo("UTC")).isoformat().replace("+00:00", "Z"), "end": ulehomse_algus.astimezone(ZoneInfo("UTC")).isoformat().replace("+00:00", "Z"), "fields": "ee"})  # Teisendab Eesti ajavahemiku API nõutud UTC-kujule ja valib Eesti hinnapiirkonna.
    url = f"https://dashboard.elering.ee/api/nps/price/csv?{parameetrid}"  # Koostab Eleringi avaliku hinnateenuse täieliku URL-i.
    paring = Request(url, headers={"User-Agent": "Mozilla/5.0"})  # Loob HTTP-päringu kasutajaagendiga, mida veebiserverid üldjuhul aktsepteerivad.

    try:  # Alustab võrgu- ja andmetöötlusvigade käsitlemise plokki.
        with urlopen(paring, timeout=20) as vastus:  # Saadab päringu ning katkestab selle hiljemalt 20 sekundi järel.
            vastuse_tekst = vastus.read().decode("utf-8-sig")  # Loeb UTF-8 tekstivastuse ja eemaldab võimaliku BOM-märgendi.
    except HTTPError as viga:  # Püüab kinni serveri tagastatud HTTP-vea, näiteks 404 või 500.
        raise RuntimeError(f"Eleringi teenus tagastas HTTP vea {viga.code}.") from viga  # Annab edasi arusaadava veateate koos olekukoodiga.
    except URLError as viga:  # Püüab kinni internetiühenduse, DNS-i või TLS-ühenduse vea.
        raise ConnectionError("Eleringi teenusega ei õnnestunud ühendust luua.") from viga  # Teavitab, et probleem on võrguühenduses või teenuse kättesaadavuses.
    except TimeoutError as viga:  # Püüab kinni päringu ajalõpu vea.
        raise TimeoutError("Eleringi teenus ei vastanud 20 sekundi jooksul.") from viga  # Selgitab, et teenuse vastus võttis liiga kaua aega.

    try:  # Alustab CSV-vastuse struktuuri ja väärtuste kontrollimist.
        read = csv.reader(StringIO(vastuse_tekst), delimiter=";")  # Loeb semikoolonitega eraldatud CSV-ridu tekstivoo kaudu.
        pealkiri = next(read)  # Loeb esimese rea, mis peab sisaldama veergude nimetusi.
        if len(pealkiri) < 3 or pealkiri[2].strip() != "NPS Eesti":  # Kontrollib, et vastuses oleks oodatud Eesti hinnaveerg.
            raise ValueError("Eleringi vastuse CSV-vorming või hinnapiirkond ei vasta ootustele.")  # Katkestab töö, kui API vorming on muutunud või andmed on valed.
        hinnad = []  # Loob tühja loendi, kuhu lisatakse iga hinnaintervalli sõnastik.
        for rida in read:  # Töötleb vastuse kõiki andmeridu ükshaaval.
            if len(rida) < 3:  # Jätab vahele katkise või tühja CSV-rea.
                continue  # Liigub järgmise rea juurde ilma vigast kirjet kasutamata.
            aeg = datetime.fromtimestamp(int(rida[0].strip()), tz=ZoneInfo("UTC")).astimezone(eesti_ajavooend)  # Teisendab UTC Unix-ajatempli Eesti kohalikuks ajaks.
            if aeg.date() != homse_algus.date():  # Kontrollib, et API tagastatud intervall kuuluks tõesti homsesse päeva.
                continue  # Jätab kõrvale päringu piirile sattunud muu kuupäeva kirje.
            hind = Decimal(rida[2].strip().replace(",", "."))  # Teisendab Eesti komakohaga hinnateksti täpseks kümnendarvuks EUR/MWh ühikus.
            hinnad.append({"aeg": aeg, "hind_eur_mwh": hind})  # Lisab kontrollitud aja ja hinna tagastusloendisse.
    except (StopIteration, ValueError, InvalidOperation) as viga:  # Püüab kinni puuduva päise, vigase ajatempli või mittenumbrilise hinna vea.
        raise ValueError("Eleringi teenus tagastas puudulikud või vigased hinnaandmed.") from viga  # Muudab tehnilise vea kasutajale arusaadavaks veateateks.

    if not hinnad:  # Kontrollib, kas homse päeva kohta saadi vähemalt üks hinnakirje.
        raise LookupError("Homseid elektrihindu ei ole Eleringi teenuses veel avaldatud.")  # Selgitab tavapärast olukorda, kus järgmise päeva hinnad pole veel saadaval.
    return hinnad  # Tagastab homse päeva kontrollitud hinnaintervallide loendi.