"""Genereerib w10 praktikumi jaoks mock-tooteandmed failidesse
tooted.csv ja tooted.json (samad andmed, et harjutada eri failitüüpide lugemist).

Käibemaksumäärad on 2025. aasta I poolaasta seisuga (kuni 30.06.2025):
22% üldmäär, 9% raamatud, ravimid ja meditsiiniseadmed, ajakirjandusväljaanded.
Seeme on fikseeritud, seega tekivad iga käivitusega täpselt samad failid.

Käivita:  python genereeri_tooted.py
"""

import csv
import json
import random
from pathlib import Path

random.seed(2030)

# kategooriad kujul (km-määr, hinnavahemik km-ta, põhinimetused, variandid)
# fmt: off
KATEGOORIAD = [
    (22, (0.39, 12.99), [
        "Piim", "Keefir", "Kohupiim", "Juust", "Või", "Jogurt", "Rukkileib", "Sai",
        "Kaerahelbed", "Tatar", "Riis", "Makaronid", "Suhkur", "Jahu", "Kohv",
        "Tee", "Šokolaad", "Kommid", "Küpsised", "Kartulikrõpsud", "Hakkliha",
        "Viinerid", "Sink", "Kanafilee", "Lõhefilee", "Õunamahl", "Mineraalvesi",
        "Kali", "Ketšup", "Majonees", "Sinep", "Hapukurk", "Moos", "Mesi",
    ], ["0,5 l", "1 l", "200 g", "400 g", "500 g", "1 kg", "mahe", "klassikaline",
        "light", "peremaht", "laktoosivaba", "suitsune"]),
    (22, (0.99, 24.99), [
        "Nõudepesuvahend", "Pesupulber", "Pesuloputusvahend", "Tualettpaber",
        "Majapidamispaber", "Prügikotid", "Käsnad", "Klaasipuhastusvahend",
        "Seep", "Šampoon", "Hambapasta", "Hambahari", "Dušigeel", "Deodorant",
        "Küünlad", "Fooliumirull", "Toidukile", "Patareid AA", "Patareid AAA",
    ], ["väike", "suur", "4 tk", "8 tk", "12 tk", "lõhnatu", "sidruni", "eco",
        "tundlikule nahale", "säästupakk"]),
    (22, (4.99, 899.0), [
        "Kõrvaklapid", "Juhtmevaba hiir", "Klaviatuur", "USB-mälupulk",
        "Laadija", "USB-C kaabel", "Kaasaskantav kõlar", "Veekeetja",
        "Kohvimasin", "Röster", "Saumikser", "Föön", "Triikraud", "Tolmuimeja",
        "Monitor", "Veebikaamera", "Nutikell", "Akupank", "LED-pirn", "Pikendusjuhe",
    ], ["must", "valge", "hõbe", "Pro", "Mini", "Lite", "2025", "Max",
        "juhtmevaba", "kompaktne"]),
    (22, (1.49, 189.0), [
        "Akutrell", "Haamer", "Kruvikeerajate komplekt", "Mõõdulint", "Tangid",
        "Saag", "Värvirull", "Pintsel", "Seinavärv", "Kruvid", "Tüüblid",
        "Töökindad", "Labidas", "Reha", "Aiavoolik", "Muruniiduk", "Lumelabidas",
        "Redel", "Tööriistakast", "Vesilood",
    ], ["väike", "suur", "professional", "hobi", "100 tk", "50 tk", "3 m", "5 m",
        "teleskoopvarrega", "18 V"]),
    (22, (0.29, 39.99), [
        "Pastakas", "Harilik pliiats", "Märkmik", "Vihik", "Kaustik", "Kiirköitja",
        "Klammerdaja", "Kirjaklambrid", "Kleepmärkmed", "Marker", "Kustukumm",
        "Joonlaud", "Kalkulaator", "Paberipakk A4", "Ümbrikud", "Liimipulk",
    ], ["sinine", "punane", "must", "A5", "A4", "ruuduline", "jooneline",
        "10 tk", "kontoripakk", "kooli"]),
    (22, (3.99, 149.0), [
        "T-särk", "Pusa", "Teksapüksid", "Sokid", "Müts", "Sall", "Kindad",
        "Vihmajope", "Talvejope", "Spordipüksid", "Tossud", "Kummikud",
        "Villased sokid", "Särk", "Kleit",
    ], ["S", "M", "L", "XL", "laste", "naiste", "meeste", "unisex", "puuvillane",
        "meriinovill"]),
    (9, (2.99, 49.99), [
        "Romaan", "Luulekogu", "Kokaraamat", "Lasteraamat", "Pildiraamat",
        "Eesti-inglise sõnaraamat", "Python algajatele", "Matemaatika õpik",
        "Eesti ajalugu", "Reisijuht", "Aiandusraamat", "Krimiromaan",
        "Fantaasiaromaan", "Elulooraamat", "Töövihik",
    ], ["kõvakaaneline", "pehmekaaneline", "uus trükk", "2. trükk", "kingitusväljaanne",
        "I osa", "II osa", "illustreeritud"]),
    (9, (0.99, 34.99), [
        "Paratsetamool", "Ibuprofeen", "Köharohi", "Ninasprei", "Kurgutabletid",
        "Vitamiin C", "Vitamiin D", "Magneesium", "Plaastrid", "Sidemerull",
        "Kraadiklaas", "Vererõhumõõtja", "Silmatilgad", "Allergiatabletid",
    ], ["10 tk", "20 tk", "30 tk", "60 tk", "100 ml", "200 ml", "lastele",
        "täiskasvanutele", "digitaalne"]),
    (9, (1.20, 9.99), [
        "Päevaleht", "Nädalaleht", "Maakonnaleht", "Teadusajakiri",
        "Moeajakiri", "Autoajakiri", "Aiandusajakiri", "Ristsõnaajakiri",
        "Lasteajakiri", "Arvutiajakiri",
    ], ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "erinumber",
        "nädalalõpu nr"]),
]

# fmt: on

VALJAD = ["inventari_nr", "nimetus", "hind_km_ta", "laoseis", "km_maar"]

# kaalud: kui tõenäoliselt kategooriast toode valitakse
KAALUD = [30, 14, 10, 9, 9, 8, 9, 7, 4]


def genereeri(arv):
    """Tagastab arv juhuslikku toodet sõnastike järjendina."""
    nimed = set()
    tooted = []
    inv_nr = 100_000
    while len(tooted) < arv:
        maar, (min_h, max_h), pohid, variandid = random.choices(KATEGOORIAD, KAALUD)[0]
        nimi = f"{random.choice(pohid)} {random.choice(variandid)}"
        if nimi in nimed:
            continue
        nimed.add(nimi)
        # hinnad pigem odavamad: ruuttõmme vahemiku alumisse otsa
        hind = min_h + (max_h - min_h) * random.random() ** 2
        hind = round(int(hind) + random.choice([0.19, 0.29, 0.49, 0.79, 0.95, 0.99]), 2)
        laoseis = 0 if random.random() < 0.05 else random.randint(1, 500)
        inv_nr += random.randint(1, 7)
        tooted.append(
            {
                "inventari_nr": f"INV-{inv_nr}",
                "nimetus": nimi,
                "hind_km_ta": hind,
                "laoseis": laoseis,
                "km_maar": maar,
            }
        )
    random.shuffle(tooted)
    return tooted


def salvesta_csv(tooted, failinimi):
    """Kirjutab tooted CSV-faili (eraldaja ;, hind alati 2 kohta pärast koma)."""
    with open(failinimi, "w", encoding="utf-8", newline="") as f:
        kirjutaja = csv.DictWriter(f, fieldnames=VALJAD, delimiter=";")
        kirjutaja.writeheader()
        for toode in tooted:
            kirjutaja.writerow(toode | {"hind_km_ta": f"{toode['hind_km_ta']:.2f}"})


def salvesta_json(tooted, failinimi):
    """Kirjutab tooted JSON-faili objektide massiivina, väljad õiget tüüpi."""
    with open(failinimi, "w", encoding="utf-8") as f:
        json.dump(tooted, f, ensure_ascii=False, indent=2)


def main():
    kaust = Path(__file__).parent
    tooted = genereeri(1000)
    salvesta_csv(tooted, kaust / "tooted.csv")
    salvesta_json(tooted, kaust / "tooted.json")
    print(f"Salvestatud {len(tooted)} toodet: tooted.csv, tooted.json")


main()
