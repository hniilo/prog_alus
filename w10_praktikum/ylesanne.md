# w10 praktikum – lao hinnad ja käibemaksu tõus

## Taust

Väikepoe laoarvestuse süsteemist on eksporditud fail [`tooted.csv`](tooted.csv), milles on
1000 toodet. Hinnad ja käibemaksumäärad on **2025. aasta I poolaasta** seisuga.

1. juulil 2025 tõusis Eestis käibemaksu üldmäär **22% → 24%**. Vähendatud määr 9%
(raamatud, ravimid, meditsiiniseadmed, ajalehed ja ajakirjad) jäi samaks.
Poe omanik tahab teada, kuidas määra muutus tema laole mõjub.

## Andmed

Fail on UTF-8 kodeeringus, väljad on eraldatud semikooloniga `;`, kümnendkohti eraldab punkt.

```
inventari_nr;nimetus;hind_km_ta;laoseis;km_maar
INV-101894;Veebikaamera Lite;60.19;240;22
INV-100989;Lasteajakiri mai;8.95;153;9
```

| väli | tähendus | tüüp pärast teisendamist |
|---|---|---|
| `inventari_nr` | toote unikaalne inventarinumber | `str` |
| `nimetus` | toote nimetus | `str` |
| `hind_km_ta` | ühiku hind **ilma** käibemaksuta, eurodes | `float` |
| `laoseis` | mitu tükki on laos | `int` |
| `km_maar` | käibemaksumäär protsentides | `int` |

Samad andmed on ka JSON-failis [`tooted.json`](tooted.json), objektide massiivina.
Erinevalt CSV-st on seal arvud juba arvud, mitte tekst:

```json
[
  {
    "inventari_nr": "INV-101894",
    "nimetus": "Veebikaamera Lite",
    "hind_km_ta": 60.19,
    "laoseis": 240,
    "km_maar": 22
  },
  ...
]
```

Hind käibemaksuga arvutatakse nii: `hind_km_ta * (1 + km_maar / 100)`, ümardatuna
**2 kohani pärast koma**. Lao väärtuse arvutamisel ümarda **ühiku** hind enne laoseisuga korrutamist
(nii teeb ka kassasüsteem).

## Ülesanne

Kirjuta programm `ladu.py`. Iga osa jaoks kirjuta eraldi funktsioon; `main()` ainult kutsub funktsioone
välja ja prindib tulemused.

### 1. Faili sisselugemine

Kirjuta funktsioon `loe_tooted(failinimi)`, mis tagastab järjendi sõnastikest, üks sõnastik toote kohta.
Teisenda väljad tabelis toodud tüüpideks.

*Vihje:* `csv.DictReader(f, delimiter=";")`

### 2. Abifunktsioonid

- `hind_km_ga(hind, maar)` – tagastab hinna käibemaksuga, ümardatuna 2 kohani.
  Negatiivse hinna korral tõstatab `ValueError`.
- `uus_maar(maar)` – tagastab määra pärast 1.07.2025: `22` → `24`, kõik teised jäävad samaks.
  Kui määr pole Eestis kehtiv (`0`, `9`, `13`, `22`, `24`), tõstatab `ValueError`.
- `lao_vaartus(tooted, km_ga=False)` – tagastab kõigi toodete `hind * laoseis` summa,
  `km_ga=True` korral käibemaksuga hindade järgi.

### 3. Aruanne

Prindi ekraanile:

1. mitu toodet failis on;
2. mitu toodet on iga käibemaksumääraga;
3. mitu toodet on laost otsas (`laoseis == 0`) ja nende nimetused;
4. kõige kallim ja kõige odavam toode (nimetus, inventarinumber, hind km-ta ja km-ga);
5. lao koguväärtus käibemaksuta;
6. lao koguväärtus käibemaksuga **vana** ja **uue** määraga ning nende vahe.

### 4. Uue hinnakirja salvestamine

Kirjuta fail `tooted_2025_07.csv`, kus `km_maar` on uus määr ja lisatud on veerg `hind_km_ga`
(uue määraga). Kasuta samu eraldajaid mis sisendfailis.

### 5. Testid (pytest)

Paigalda pytest (`pip install pytest`, Thonnys *Tools → Manage packages*) ja kirjuta fail
`test_ladu.py`. Testi vähemalt:

- `hind_km_ga` tavalise hinnaga mõlema määra puhul (nt `hind_km_ga(10, 22) == 12.2`);
- **piirjuhte**: hind `0`, väga väike hind (`0.01`), määr `0`;
- et negatiivne hind tõstatab vea – vt `pytest.raises`;
- `uus_maar` kõigi kehtivate määrade ja ühe vigase määra (nt `23`) korral;
- `lao_vaartus` väikese käsitsi koostatud järjendiga, kus üks toode on laoseisuga `0`;
- `loe_tooted` väikese testfailiga: loo pytesti `tmp_path` abil ajutine CSV-fail kahe reaga
  ja kontrolli, et väljad on õiget tüüpi.

Käivita testid käsurealt: `pytest -v`

### 6. Lisaülesanne

- Kirjuta funktsioon `otsi(tooted, sona)`, mis leiab kõik tooted, mille nimetuses sõna esineb,
  sõltumata suurtest ja väikestest tähtedest. Mitu toodet leiab sõna `piim`?
- Prindi iga käibemaksumäära kohta lao väärtus käibemaksuga.
- Kirjuta funktsioon `loe_tooted_json(failinimi)`, mis loeb samad tooted failist `tooted.json`
  (*vihje:* `json.load`). Kas tüüpe on vaja teisendada? Lisa test, mis kontrollib, et
  `loe_tooted("tooted.csv") == loe_tooted_json("tooted.json")`.
- Mis juhtub, kui CSV-failis on tühi rida või hinna asemel tekst `"puudub"`?
  Muuda faili koopiat, käivita programm ja kasuta siluri (Thonnys *Debug*) abi, et vea põhjus leida.

## Kontrollvastused

Kui su programm annab need tulemused, on arvutused tõenäoliselt õiged.

| küsimus | vastus |
|---|---|
| toodete arv | 1000 |
| tooteid määraga 22% / 9% | 805 / 195 |
| laost otsas | 46 |
| kõige kallim toode | INV-101800, 876.19 € km-ta, 1068.95 € km-ga |
| kõige odavam toode | INV-101051, 0.19 € km-ta |
| lao väärtus km-ta | 10 242 839.97 € |
| lao väärtus km-ga, vana määr | 12 414 552.99 € |
| lao väärtus km-ga, uus määr | 12 607 348.61 € |
| vahe | 192 795.62 € |
| tooteid sõnaga `piim` | 18 |

---

Andmed on genereeritud skriptiga [`genereeri_tooted.py`](genereeri_tooted.py) (mock-andmed,
tooted ja hinnad on välja mõeldud).
