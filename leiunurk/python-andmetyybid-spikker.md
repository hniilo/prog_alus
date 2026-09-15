# Python: andmetüübid ja andmestruktuurid

> **Spikker** · MI.2030 · Python 3.12+
> Näited on kontrollitud Python 3.12-ga. Kommentaar `# →` näitab tulemust.
> Funktsioonid, f-sõnede vormindus ja standardteek: vt `python-funktsioonid-meetodid-spikker.md`.

| Tähis | Tähendus |
|---|---|
| **R** | *Reegel* — interpretaator nõuab; rikkumine annab vea |
| **K** | *Konventsioon* — PEP 8 või hea tava; interpretaator ei kontrolli |
| ⚠️ | Levinud lõks |

---

## Sisukord

0. [Õpetajale: soovitatav ülesehitus](#0-õpetajale-soovitatav-ülesehitus)
1. [Mõttemudel: nimi ja objekt](#1-mõttemudel-nimi-ja-objekt)
2. [Ülevaade: kõik põhitüübid](#2-ülevaade-kõik-põhitüübid)
3. [Arvud: int, float, Decimal](#3-arvud-int-float-decimal)
4. [Tõeväärtus ja None](#4-tõeväärtus-ja-none)
5. [Sõne — str](#5-sõne--str)
6. [Järjend — list](#6-järjend--list)
7. [Ennik — tuple](#7-ennik--tuple)
8. [Sõnastik — dict](#8-sõnastik--dict)
9. [Hulk — set ja frozenset](#9-hulk--set-ja-frozenset)
10. [Vahemik — range](#10-vahemik--range)
11. [Tüübiteisendused](#11-tüübiteisendused)
12. [Millist struktuuri valida?](#12-millist-struktuuri-valida)
13. [Jooksev näide: kaupluse hinnaarvestus](#13-jooksev-näide-kaupluse-hinnaarvestus)
14. [Levinud erindid](#14-levinud-erindid)
15. [Kontrollküsimused](#15-kontrollküsimused)

---

## 0. Õpetajale: soovitatav ülesehitus

| Samm | Teema | Põhisõnum tudengile | Demo |
|---|---|---|---|
| 1 | Nimi → objekt, `type()`, `id()` | Muutuja on silt, mitte kast | Thonny *View → Variables* ja *View → Heap* |
| 2 | Arvud, `bool` | `/` annab alati `float`; `float` on ligikaudne | `0.1 + 0.2` |
| 3 | `str` | Sõne on muutumatu; meetod tagastab uue sõne | `s.upper()` vs `s = s.upper()` |
| 4 | `list`, `tuple` | Muudetav vs muutumatu; alias vs koopia | `b = a; b.append(3)` |
| 5 | `dict`, `set` | Otsing võtme järgi; räsitavus | `d["x"]` vs `d.get("x")` |
| 6 | Valik ja kombineerimine | Struktuuri valik sõltub kasutusest | Jooksev näide (ptk 13) |

💡 Thonny *Heap* vaade näitab objekte koos id-dega — sobib aliase ja koopia vahe näitamiseks paremini kui ükski joonis.

---

## 1. Mõttemudel: nimi ja objekt

Igal objektil on kolm omadust:

| Omadus | Kuidas vaadata | Kas saab muutuda? |
|---|---|---|
| Identiteet | `id(x)` | Ei |
| Tüüp | `type(x)` | Ei |
| Väärtus | `print(x)` | Ainult muudetavatel tüüpidel |

Muutuja on **nimi, mis viitab objektile**. Omistamine `=` seob nime objektiga — see ei kopeeri midagi.

```python
a = [1, 2]
b = a            # b viitab SAMALE objektile
b.append(3)
print(a)         # → [1, 2, 3]
print(a is b)    # → True
```

```
a ──┐
    ├──► [1, 2, 3]      üks objekt, kaks nime
b ──┘
```

Muutumatu objektiga tundub sama olukord teistsugune, sest „muutmine" loob tegelikult uue objekti:

```python
x = 5
y = x
y += 1           # luuakse uus objekt 6 ja y seotakse sellega
print(x, y)      # → 5 6
```

### `==` vs `is`

| Operaator | Küsimus | Millal kasutada |
|---|---|---|
| `==` | Kas väärtused on võrdsed? | Peaaegu alati |
| `is` | Kas see on täpselt sama objekt? | `None` kontrolliks (**K**) |

⚠️ `is` võib arvude või sõnede puhul „kogemata töötada", sest CPython hoiab väikeseid arve vahemälus. See on implementatsiooni detail, mitte reegel.

---

## 2. Ülevaade: kõik põhitüübid

| Tüüp | Eesti termin | Literaal | Muudetav | Järjestatud | Indeks | Duplikaadid | Räsitav |
|---|---|---|---|---|---|---|---|
| `int` | täisarv | `42` | ei | – | – | – | jah |
| `float` | ujukomaarv | `3.14` | ei | – | – | – | jah |
| `bool` | tõeväärtus | `True` | ei | – | – | – | jah |
| `NoneType` | tühiväärtus | `None` | ei | – | – | – | jah |
| `str` | sõne | `"tere"` | **ei** | jah | jah | jah | jah |
| `list` | järjend | `[1, 2]` | **jah** | jah | jah | jah | ei |
| `tuple` | ennik | `(1, 2)` | **ei** | jah | jah | jah | jah\* |
| `dict` | sõnastik | `{"a": 1}` | **jah** | lisamise järjekord | võtme järgi | võtmed unikaalsed | ei |
| `set` | hulk | `{1, 2}` | **jah** | ei | ei | ei | ei |
| `frozenset` | külmutatud hulk | `frozenset({1})` | ei | ei | ei | ei | jah |
| `range` | vahemik | `range(5)` | ei | jah | jah | – | jah |

\* Ennik on räsitav ainult siis, kui kõik tema elemendid on räsitavad.

**Räsitav** (*hashable*) — objekti väärtus ei saa muutuda, seega sobib ta **sõnastiku võtmeks** ja **hulga elemendiks**. Rusikareegel: muutumatud tüübid on räsitavad, muudetavad mitte.

---

## 3. Arvud: int, float, Decimal

### 3.1 Aritmeetika

| Operaator | Nimi | Näide | Tulemus | Märkus |
|---|---|---|---|---|
| `+` `-` `*` | liitmine, lahutamine, korrutamine | `7 * 2` | `14` | `int` ja `float` koos → `float` |
| `/` | jagamine | `10 / 2` | `5.0` | **R**: tulemus alati `float` |
| `//` | täisarvuline jagamine | `7 // 2` | `3` | ümardab **alla** |
| `%` | jääk | `7 % 2` | `1` | paarsus: `n % 2 == 0` |
| `**` | astendamine | `2 ** 10` | `1024` | `2 ** -1` → `0.5` |
| `divmod(a, b)` | jagatis ja jääk | `divmod(17, 5)` | `(3, 2)` | |

⚠️ `-7 // 2` → `-4` (alla, mitte nulli poole) ja `-7 % 2` → `1`.

- Lühikujud: `x += 1`, `x -= 2`, `x *= 3`, `x /= 2`. Pythonis **pole** `x++` (**R**).
- Võrdlused: `<` `<=` `>` `>=` `==` `!=`. Aheldamine on lubatud: `0 <= vanus < 120`.

### 3.2 `int`

- Piiramatu suurus: `2 ** 100` töötab.
- `1_000_000` — alakriipsud loetavuseks (**K**).
- Muud alused: `0b1010` (kahend), `0o17` (kaheksand), `0xFF` (kuueteistkümnend).

### 3.3 `float`

```python
0.1 + 0.2              # → 0.30000000000000004
0.1 + 0.2 == 0.3       # → False

import math
math.isclose(0.1 + 0.2, 0.3)   # → True
```

- `float` on kahendsüsteemis ligikaudne (IEEE 754). See ei ole Pythoni viga — sama juhtub kõigis keeltes.
- ⚠️ Ära võrdle ujukomaarve `==` abil; kasuta `math.isclose()`.
- ⚠️ `round()` ümardab poole juures **paarisarvuni**: `round(2.5)` → `2`, `round(3.5)` → `4`.
- ⚠️ `round(2.675, 2)` → `2.67`, sest 2.675 on mälus tegelikult veidi väiksem.
- Eriväärtused: `float("inf")`, `float("nan")`.

### 3.4 Raha: `Decimal`

```python
from decimal import Decimal, ROUND_HALF_UP

hind = Decimal("2.675")                                    # K: loo alati SÕNEST
hind.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)     # → Decimal('2.68')

Decimal(0.1)   # → Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

⚠️ `Decimal(0.1)` kannab `float`-i ebatäpsuse kaasa. Kasuta `Decimal("0.1")`.

---

## 4. Tõeväärtus ja None

### 4.1 `bool`

- `True` ja `False` — suure algustähega (**R**).
- `bool` on `int`-i alamtüüp: `True + True` → `2`.
- Loogikatehted: `and`, `or`, `not`.

**Lühisarvutus** — parem pool arvutatakse ainult vajadusel:

```python
if x != 0 and 10 / x > 1:     # kui x == 0, jagamist ei toimu
    ...

nimi = sisestus or "anonüümne"   # or tagastab esimese tõese operandi
```

### 4.2 Tõesus

**Väärad väärtused:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `range(0)`.
Kõik muu on tõene.

| Halvem | Parem (**K**) |
|---|---|
| `if len(korv) > 0:` | `if korv:` |
| `if valmis == True:` | `if valmis:` |
| `if x == None:` | `if x is None:` |

⚠️ `bool("False")` → `True` ja `bool("0")` → `True` — mittetühi sõne on alati tõene.

### 4.3 `None`

- Tähendab „väärtus puudub".
- Funktsioon ilma `return`-ita tagastab `None`.
- Kontroll: `x is None` (**K**, PEP 8).

---

## 5. Sõne — str

**Omadused:** muutumatu · järjestatud · indekseeritav · itereeritav · Unicode (täpitähed on tavalised märgid)

### 5.1 Loomine

```python
'tere'  "tere"                  # samaväärsed (R)
"""mitu
rida"""
"rida1\nrida2\ttabulaator"      # \n reavahetus, \t tabulaator
r"C:\kaust\uus"                 # toorsõne: \ ei ole erimärk
```

**K:** vali üks jutumärgistiil ja hoia seda läbivalt (`ruff format` kasutab `"`).

### 5.2 Indekseerimine ja viilutamine

```
 s = "Python"
       P    y    t    h    o    n
       0    1    2    3    4    5
      -6   -5   -4   -3   -2   -1
```

```python
s[0]        # → 'P'
s[-1]       # → 'n'
s[1:4]      # → 'yth'      [algus:lõpp] — lõpp EI kuulu hulka
s[:2]       # → 'Py'
s[-3:]      # → 'hon'
s[::2]      # → 'Pto'      [algus:lõpp:samm]
s[::-1]     # → 'nohtyP'
s[10]       # IndexError
s[2:100]    # → 'thon'     viilutamine ei anna viga
s[0] = "J"  # TypeError — sõne on muutumatu (R)
```

### 5.3 Operaatorid

| Avaldis | Tulemus | Tähendus |
|---|---|---|
| `"tere" + " " + "maailm"` | `'tere maailm'` | ühendamine |
| `"ab" * 3` | `'ababab'` | kordamine |
| `"er" in "tere"` | `True` | alamsõne kontroll |
| `len("tere")` | `4` | pikkus |
| `"apelsin" < "banaan"` | `True` | võrdlus märgikoodide järgi |

⚠️ `"Hind: " + 5` → `TypeError`. Kasuta f-sõnet: `f"Hind: {5}"`.

### 5.4 f-sõned (lühidalt)

```python
toode, hind, kogus = "leib", 1.89, 3
print(f"{toode}: {kogus} × {hind:.2f} € = {kogus * hind:.2f} €")
# → leib: 3 × 1.89 € = 5.67 €
```

Täielik vormindustabel on funktsioonide spikris.

### 5.5 Meetodid

⚠️ **Sõnemeetodid ei muuda sõnet.** Nad tagastavad uue väärtuse.

```python
nimi = "  mari  "
nimi.strip()          # tagastab 'mari', aga nimi on endiselt '  mari  '
nimi = nimi.strip()   # alles nüüd seotakse nimi uue sõnega
```

| Rühm | Meetod | Näide | Tulemus |
|---|---|---|---|
| **Suurtähed** | `lower()` | `"TeRe".lower()` | `'tere'` |
| | `upper()` | `"tere".upper()` | `'TERE'` |
| | `capitalize()` | `"tere maailm".capitalize()` | `'Tere maailm'` |
| | `title()` | `"tere maailm".title()` | `'Tere Maailm'` |
| **Tühimärgid** | `strip()` | `"  x  ".strip()` | `'x'` |
| | `lstrip()` / `rstrip()` | `"x\n".rstrip()` | `'x'` |
| **Otsimine** | `find(x)` | `"banaan".find("a")` | `1` (puudub → `-1`) |
| | `index(x)` | `"banaan".index("z")` | `ValueError` |
| | `count(x)` | `"banaan".count("a")` | `3` |
| | `startswith(x)` | `"toode_leib".startswith("toode")` | `True` |
| | `endswith(x)` | `"hinnad.csv".endswith(".csv")` | `True` |
| **Muutmine** | `replace(vana, uus)` | `"1,89".replace(",", ".")` | `'1.89'` |
| | `removeprefix(x)` | `"toode_leib".removeprefix("toode_")` | `'leib'` |
| | `removesuffix(x)` | `"hinnad.csv".removesuffix(".csv")` | `'hinnad'` |
| | `zfill(n)` | `"7".zfill(3)` | `'007'` |
| **Tükeldamine** | `split()` | `"a  b c".split()` | `['a', 'b', 'c']` |
| | `split(eraldaja)` | `"a,,b".split(",")` | `['a', '', 'b']` |
| | `splitlines()` | `"r1\nr2".splitlines()` | `['r1', 'r2']` |
| | `partition(x)` | `"võti=väärtus".partition("=")` | `('võti', '=', 'väärtus')` |
| **Ühendamine** | `eraldaja.join(jada)` | `", ".join(["leib", "piim"])` | `'leib, piim'` |
| **Kontroll** | `isdigit()` | `"123".isdigit()` | `True` |
| | `isalpha()` | `"õun".isalpha()` | `True` |
| | `isalnum()` | `"ab12".isalnum()` | `True` |
| | `isspace()` | `"  ".isspace()` | `True` |

⚠️ `split()` ilma argumendita ja `split(" ")` käituvad erinevalt: esimene ühendab järjestikused tühikud, teine mitte.

⚠️ `"-5".isdigit()` → `False` ja `"3.5".isdigit()` → `False`. Arvu kontrolliks kasuta `try: int(tekst)` (vt funktsioonide spikker).

⚠️ `", ".join([1, 2])` → `TypeError`: `join` vajab sõnesid.
Õigesti: `", ".join(str(x) for x in arvud)`.

⚠️ **Eesti tähestik ja sorteerimine:**

```python
sorted(["õun", "ämber", "Zebra", "auto"])   # → ['Zebra', 'auto', 'ämber', 'õun']
```

Python sorteerib Unicode koodide järgi: suurtähed enne väiketähti, `ä` enne `õ`. Eesti tähestiku järjekord nõuab `locale` moodulit ja sõltub operatsioonisüsteemist.

---

## 6. Järjend — list

**Omadused:** muudetav · järjestatud · duplikaadid lubatud · elemendid võivad olla eri tüüpi

**K:** hoia järjendis sama tähendusega elemente. Kui väljadel on eri tähendus (nimi, hind, kogus), kasuta ennikut või sõnastikku.

### 6.1 Loomine ja ligipääs

```python
tooted = ["leib", "piim", "juust"]
korv = []                        # K: [] eelistatud list() ees

tooted[0]            # → 'leib'
tooted[-1]           # → 'juust'
tooted[1] = "keefir" # muudab järjendit kohapeal
tooted[0:2]          # → ['leib', 'keefir']   viil on UUS järjend
len(tooted)          # → 3
"piim" in tooted     # → False
```

### 6.2 Meetodid

| Meetod | Tegevus | Tagastab | Viga |
|---|---|---|---|
| `a.append(x)` | lisab `x` lõppu | `None` | |
| `a.extend(jada)` | lisab jada kõik elemendid lõppu | `None` | |
| `a.insert(i, x)` | lisab `x` indeksile `i` | `None` | |
| `a.pop()` | eemaldab viimase | eemaldatud elemendi | `IndexError`, kui tühi |
| `a.pop(i)` | eemaldab indeksilt `i` | eemaldatud elemendi | `IndexError` |
| `a.remove(x)` | eemaldab esimese `x` | `None` | `ValueError`, kui puudub |
| `a.clear()` | tühjendab | `None` | |
| `a.index(x)` | esimese `x` indeks | `int` | `ValueError`, kui puudub |
| `a.count(x)` | `x` esinemiste arv | `int` | |
| `a.sort()` | sorteerib kohapeal | `None` | `TypeError` eri tüüpide korral |
| `a.sort(key=..., reverse=True)` | sorteerib võtme järgi, kahanevalt | `None` | |
| `a.reverse()` | pöörab kohapeal ümber | `None` | |
| `a.copy()` | pinnapealne koopia | uue järjendi | |

⚠️ **Muutvad meetodid tagastavad `None`:**

```python
hinnad = [3.5, 1.2, 2.8]
hinnad = hinnad.sort()     # VIGA: hinnad on nüüd None
hinnad.append(4.0)         # AttributeError: 'NoneType' object has no attribute 'append'
```

Õigesti: `hinnad.sort()` (muudab kohapeal) **või** `sorteeritud = sorted(hinnad)` (tagastab uue, originaal jääb alles).

**`append` vs `extend`:**

```python
a = [1, 2]
a.append([3, 4])    # → [1, 2, [3, 4]]   üks element juurde

b = [1, 2]
b.extend([3, 4])    # → [1, 2, 3, 4]     kaks elementi juurde
```

### 6.3 Koopiad

| Viis | Mis juhtub |
|---|---|
| `b = a` | **alias** — sama objekt, kaks nime |
| `b = a.copy()` · `b = a[:]` · `b = list(a)` | **pinnapealne koopia** — uus järjend, sisemised objektid jagatud |
| `b = copy.deepcopy(a)` | **sügav koopia** — kõik tasemed kopeeritakse |

⚠️ **Pesastatud järjend korrutamisega:**

```python
tabel = [[0] * 3] * 3
tabel[0][0] = 1
print(tabel)    # → [[1, 0, 0], [1, 0, 0], [1, 0, 0]]   kolm viidet SAMALE reale

tabel = [[0] * 3 for _ in range(3)]    # õigesti: iga rida on eraldi objekt
```

⚠️ **Ära eemalda elemente järjendist, mida parasjagu läbid:**

```python
arvud = [1, 2, 2, 3]
for x in arvud:
    if x == 2:
        arvud.remove(x)
print(arvud)    # → [1, 2, 3]   üks 2 jäi alles!

arvud = [x for x in arvud if x != 2]   # õigesti: loo uus järjend
```

### 6.4 Järjendikomprehensioon

```python
hinnad = [1.89, 0.99, 4.49]

[round(h * 0.9, 2) for h in hinnad]    # teisendus → [1.7, 0.89, 4.04]
[h for h in hinnad if h > 1]           # filtreerimine → [1.89, 4.49]
```

**K:** kui komprehensioon ei mahu mõistlikult ühele reale või vajab mitut tingimust, kirjuta tavaline `for`-tsükkel.

---

## 7. Ennik — tuple

**Omadused:** muutumatu · järjestatud · duplikaadid lubatud · räsitav (kui sisu on räsitav)

```python
rida = ("leib", 2, 1.89)
rida[0]          # → 'leib'
rida[1] = 3      # TypeError (R)
```

⚠️ **Enniku teeb koma, mitte sulud (R):**

```python
type((5))      # → <class 'int'>
type((5,))     # → <class 'tuple'>
x = 1, 2       # → (1, 2)
tyhi = ()      # tühi ennik
```

### 7.1 Lahtipakkimine

```python
nimi, kogus, hind = rida          # elementide arv peab klappima (R), muidu ValueError
a, b = b, a                       # kahe muutuja vahetamine
esimene, *muud = [1, 2, 3, 4]     # esimene = 1, muud = [2, 3, 4]

for nimi, kogus in [("leib", 2), ("piim", 1)]:
    print(nimi, kogus)
```

### 7.2 Meetodid

| Meetod | Tegevus |
|---|---|
| `t.count(x)` | `x` esinemiste arv |
| `t.index(x)` | esimese `x` indeks (`ValueError`, kui puudub) |

⚠️ **Muutumatu ennik võib sisaldada muudetavat objekti:**

```python
t = (1, [2])
t[1].append(3)    # lubatud — ennik viitab endiselt samale järjendile
print(t)          # → (1, [2, 3])
hash(t)           # TypeError: unhashable type: 'list'
```

**Millal ennik?** Fikseeritud struktuuriga kirje · funktsiooni mitu tagastusväärtust · sõnastiku võti (nt koordinaadid `(x, y)`).

---

## 8. Sõnastik — dict

**Omadused:** võti → väärtus · muudetav · võtmed unikaalsed ja räsitavad (**R**) · säilitab lisamise järjekorra (keele garantii alates Python 3.7)

### 8.1 Põhitegevused

```python
hinnakiri = {"leib": 1.89, "piim": 0.99}

hinnakiri["leib"]              # → 1.89
hinnakiri["sai"]               # KeyError: 'sai'
hinnakiri.get("sai")           # → None
hinnakiri.get("sai", 0.0)      # → 0.0

hinnakiri["sai"] = 1.29        # lisamine (uus võti)
hinnakiri["leib"] = 1.99       # muutmine (olemasolev võti)
del hinnakiri["piim"]          # kustutamine (KeyError, kui puudub)

"leib" in hinnakiri            # → True    in kontrollib VÕTMEID
1.99 in hinnakiri              # → False   ⚠️ väärtusi ei kontrollita
1.99 in hinnakiri.values()     # → True
```

### 8.2 Meetodid

| Meetod | Tegevus | Tagastab |
|---|---|---|
| `d.get(k)` · `d.get(k, vaikimisi)` | väärtus, kui võti olemas | väärtuse / `None` / vaikeväärtuse |
| `d.keys()` | võtmete vaade | `dict_keys` |
| `d.values()` | väärtuste vaade | `dict_values` |
| `d.items()` | `(võti, väärtus)` paaride vaade | `dict_items` |
| `d.update(teine)` | lisab / kirjutab üle teise sõnastiku paarid | `None` |
| `d.pop(k)` | eemaldab võtme | väärtuse (`KeyError`, kui puudub) |
| `d.pop(k, vaikimisi)` | eemaldab, kui olemas | väärtuse / vaikeväärtuse |
| `d.popitem()` | eemaldab viimati lisatud paari | `(võti, väärtus)` |
| `d.setdefault(k, v)` | kui `k` puudub, lisab `k: v` | `d[k]` |
| `d.clear()` | tühjendab | `None` |
| `d.copy()` | pinnapealne koopia | uue sõnastiku |
| `d \| teine` | ühendab kaks sõnastikku (3.9+) | uue sõnastiku |

### 8.3 Läbimine

```python
for toode in hinnakiri:                     # võtmed
    print(toode)

for hind in hinnakiri.values():             # väärtused
    print(hind)

for toode, hind in hinnakiri.items():       # paarid — kõige sagedasem
    print(f"{toode}: {hind:.2f} €")
```

### 8.4 Levinud mustrid

```python
# Loendamine
loendur = {}
for toode in ["leib", "piim", "leib"]:
    loendur[toode] = loendur.get(toode, 0) + 1
# → {'leib': 2, 'piim': 1}         valmislahendus: collections.Counter

# Rühmitamine
kategooriad = {}
for toode, kat in [("leib", "pagar"), ("piim", "piim"), ("sai", "pagar")]:
    kategooriad.setdefault(kat, []).append(toode)
# → {'pagar': ['leib', 'sai'], 'piim': ['piim']}

# Sõnastikukomprehensioon
kallid = {t: h for t, h in hinnakiri.items() if h > 1.5}
```

⚠️ **Sõnastiku suurust ei tohi muuta selle läbimise ajal:**

```python
for toode in hinnakiri:
    if hinnakiri[toode] > 1.5:
        del hinnakiri[toode]     # RuntimeError: dictionary changed size during iteration

for toode in list(hinnakiri):    # õigesti: läbi võtmete koopia
    if hinnakiri[toode] > 1.5:
        del hinnakiri[toode]
```

⚠️ Järjend ei saa olla võti: `{[1, 2]: "x"}` → `TypeError: unhashable type: 'list'`. Kasuta ennikut `(1, 2)`.

---

## 9. Hulk — set ja frozenset

**Omadused:** unikaalsed elemendid · järjekord pole garanteeritud · muudetav · elemendid peavad olema räsitavad

```python
kategooriad = {"piim", "pagar", "piim"}   # → {'piim', 'pagar'}  (järjekord võib erineda)
tyhi = set()                              # ⚠️ {} on tühi SÕNASTIK (R)
kategooriad[0]                            # TypeError — hulgal pole indekseid
```

| Tegevus | Meetod | Operaator | `a = {1, 2, 3}`, `b = {2, 3, 4}` |
|---|---|---|---|
| lisa | `a.add(x)` | | |
| eemalda | `a.remove(x)` | | `KeyError`, kui puudub |
| eemalda vaikselt | `a.discard(x)` | | viga ei teki |
| ühend | `a.union(b)` | `a \| b` | `{1, 2, 3, 4}` |
| ühisosa | `a.intersection(b)` | `a & b` | `{2, 3}` |
| vahe | `a.difference(b)` | `a - b` | `{1}` |
| sümmeetriline vahe | `a.symmetric_difference(b)` | `a ^ b` | `{1, 4}` |
| alamhulk | `a.issubset(b)` | `a <= b` | `False` |
| lõikumatud | `a.isdisjoint(b)` | | `False` |

### Kasutus

```python
ostud = ["leib", "piim", "leib"]

"piim" in soodustooted          # kiire liikmesuse kontroll
len(set(ostud))                 # erinevate toodete arv → 2
list(set(ostud))                # ⚠️ duplikaadid kaovad, aga järjekord võib muutuda
list(dict.fromkeys(ostud))      # duplikaadid kaovad, järjekord säilib → ['leib', 'piim']
```

- `frozenset` — muutumatu hulk; võib olla sõnastiku võti või teise hulga element.
- 💡 `in` on hulgas ja sõnastikus keskmiselt sama kiire sõltumata suurusest (O(1)), järjendis aeglustub koos pikkusega (O(n)).

---

## 10. Vahemik — range

```python
range(5)            # 0, 1, 2, 3, 4
range(2, 6)         # 2, 3, 4, 5
range(0, 10, 3)     # 0, 3, 6, 9
range(5, 0, -1)     # 5, 4, 3, 2, 1
list(range(3))      # → [0, 1, 2]
```

- Lõpp ei kuulu hulka — sama loogika nagu viilutamisel.
- Laisk: arve ei looda ette mällu, seega `range(10**9)` on kohe valmis.
- **K:** `for i in range(len(a)):` asemel kasuta `for x in a:` või `for i, x in enumerate(a):`.

---

## 11. Tüübiteisendused

| Avaldis | Tulemus | Märkus |
|---|---|---|
| `int("42")` | `42` | |
| `int(" 42 ")` | `42` | tühikud servades lubatud |
| `int("3.5")` | `ValueError` | ⚠️ enne `float()`, siis `int()` |
| `int(3.9)` | `3` | lõikab murdosa ära, ei ümarda |
| `int(-3.9)` | `-3` | nulli poole |
| `float("3.5")` | `3.5` | |
| `float("3,5")` | `ValueError` | ⚠️ eesti komakiri |
| `str(3.5)` | `'3.5'` | |
| `bool("False")` | `True` | ⚠️ mittetühi sõne |
| `bool("")` | `False` | |
| `list("abc")` | `['a', 'b', 'c']` | sõne on jada |
| `list({"a": 1, "b": 2})` | `['a', 'b']` | ainult võtmed |
| `tuple([1, 2])` | `(1, 2)` | |
| `set([1, 1, 2])` | `{1, 2}` | |
| `dict([("a", 1), ("b", 2)])` | `{'a': 1, 'b': 2}` | paaride jadast |
| `dict(zip(["a", "b"], [1, 2]))` | `{'a': 1, 'b': 2}` | kahest jadast |

**Kasutaja sisendi muster:**

```python
tekst = input("Hind: ")                  # input tagastab ALATI str
hind = float(tekst.replace(",", "."))    # lubab ka eesti komakirja
```

---

## 12. Millist struktuuri valida?

| Vajadus | Vali | Miks |
|---|---|---|
| Järjestatud kogum, mis muutub | `list` | `append`, `pop`, `sort` |
| Fikseeritud väljadega kirje | `tuple` | muutumatu, lahtipakitav |
| Otsing nime või koodi järgi | `dict` | kiire otsing võtme järgi |
| „Kas on olemas?" / unikaalsed väärtused | `set` | kiire `in`, duplikaadid kaovad |
| Unikaalsete väärtuste kogum võtmena | `frozenset` | räsitav |
| Arvujada tsükli jaoks | `range` | ei võta mälu |
| Rahasummad | `Decimal` | täpne kümnendaritmeetika |

💡 **Rusikareegel:** kui kirjutad `for`-tsükli ainult selleks, et järjendist midagi **üles leida**, sobiks ilmselt paremini sõnastik või hulk.

---

## 13. Jooksev näide: kaupluse hinnaarvestus

```python
from decimal import Decimal

# Hinnakiri: otsing toote nime järgi → sõnastik
hinnakiri = {
    "leib": Decimal("1.89"),
    "piim": Decimal("0.99"),
    "juust": Decimal("4.49"),
}

# Ostukorv: järjestatud read → järjend; iga rida on fikseeritud kirje → ennik
ostukorv = [("leib", 2), ("piim", 3), ("juust", 1)]

# Soodustooted: vaja ainult „kas on?" kontrolli → hulk
soodustooted = {"piim", "juust"}

SOODUSTUS = Decimal("0.10")    # K: konstant suurtähtedega, mitte „maagiline arv"

summa = Decimal("0")
for nimi, kogus in ostukorv:
    rea_summa = hinnakiri[nimi] * kogus
    if nimi in soodustooted:
        rea_summa -= rea_summa * SOODUSTUS
    summa += rea_summa

print(f"Kokku: {summa.quantize(Decimal('0.01'))} €")   # → Kokku: 10.49 €
```

**Arutelu tudengitega**

1. Miks on hinnakiri sõnastik, mitte järjend? Kuidas näeks otsing välja järjendiga?
2. Miks on ostukorvi rida ennik? Millal oleks parem kasutada sõnastikku `{"nimi": ..., "kogus": ...}`?
3. Mis juhtub, kui ostukorvis on toode, mida hinnakirjas pole? Kuidas seda käsitleda?
4. Mis muutuks tulemuses, kui kasutada `Decimal` asemel `float`?
5. Kas soodustuse arvutus peaks olema eraldi funktsioon? Miks?

---

## 14. Levinud erindid

Kõik allolevad on **täitmisaegsed** vead — need tekivad alles siis, kui rida käivitatakse. `SyntaxError` avastatakse enne käivitamist (nt `{"a": }`).

💡 **Tracebacki lugemine:** alusta **viimasest reast** — seal on erindi tüüp ja põhjus. Rida selle kohal näitab, kus viga tekkis.

| Erind | Näide | Tavaline põhjus |
|---|---|---|
| `TypeError` | `"Hind: " + 5` | vale tüüp tehtes |
| `TypeError` | `{[1, 2]: "x"}` | muudetav objekt võtmena |
| `TypeError` | `"tere"[0] = "T"` | muutumatu objekti muutmine |
| `ValueError` | `int("abc")` | õige tüüp, sobimatu väärtus |
| `ValueError` | `[1, 2].remove(3)` | elementi pole |
| `IndexError` | `[1, 2][5]` | indeks väljaspool vahemikku |
| `KeyError` | `{"a": 1}["b"]` | võtit pole |
| `AttributeError` | `(5).append(1)` | tüübil pole sellist meetodit |
| `AttributeError` | `None.append(1)` | tavaliselt `a = a.sort()` tagajärg |
| `NameError` | `print(hinad)` | kirjaviga nimes või määramata muutuja |
| `RuntimeError` | sõnastiku muutmine läbimise ajal | vt ptk 8.4 |

---

## 15. Kontrollküsimused

Sobivad suuliseks eksamiks ettevalmistumiseks. Proovi vastata enne vastuse avamist.

**1.** Mida prindib?
```python
a = [1, 2]
b = a
b += [3]
print(a)
```
<details><summary>Vastus</summary>

`[1, 2, 3]` — `b` on alias ja järjendi `+=` muudab objekti kohapeal.
</details>

**2.** Mida prindib?
```python
x = "tere"
x.upper()
print(x)
```
<details><summary>Vastus</summary>

`tere` — sõne on muutumatu; `upper()` tagastas uue sõne, mida ei seotud ühegi nimega.
</details>

**3.** Miks `{[1, 2]: "a"}` annab vea, aga `{(1, 2): "a"}` mitte?
<details><summary>Vastus</summary>

Sõnastiku võti peab olema räsitav. Järjend on muudetav ega ole räsitav; ennik on muutumatu ja räsitav.
</details>

**4.** Mis vahe on `a.sort()` ja `sorted(a)` vahel? Kumba kasutad, kui algne järjekord peab säilima?
<details><summary>Vastus</summary>

`a.sort()` muudab järjendit kohapeal ja tagastab `None`. `sorted(a)` tagastab uue järjendi ja originaal jääb samaks — seda kasutan, kui algne järjekord peab säilima.
</details>

**5.** Mis on `type((5))` ja `type((5,))`?
<details><summary>Vastus</summary>

`int` ja `tuple`. Enniku teeb koma, sulud ainult rühmitavad.
</details>

**6.** Mis on `-7 // 2` väärtus ja miks?
<details><summary>Vastus</summary>

`-4`. Operaator `//` ümardab alati alla (miinus lõpmatuse suunas), mitte nulli poole.
</details>

**7.** Miks `0.1 + 0.2 == 0.3` on `False`? Kuidas ujukomaarve võrrelda ja kuidas raha arvutada?
<details><summary>Vastus</summary>

`float` esitatakse kahendsüsteemis ligikaudselt. Võrdlemiseks `math.isclose()`, raha jaoks `Decimal` (loodud sõnest).
</details>

**8.** Mis on `bool("0")` väärtus?
<details><summary>Vastus</summary>

`True` — iga mittetühi sõne on tõene.
</details>

**9.** Mida teeb see kood?
```python
d = {}
d["x"] += 1
```
<details><summary>Vastus</summary>

`KeyError: 'x'` — `+=` loeb enne olemasolevat väärtust, aga võtit pole. Õigesti: `d["x"] = d.get("x", 0) + 1`.
</details>

**10.** Kas `t = (1, [2]); t[1].append(3)` õnnestub? Kas see on vastuolus sellega, et ennik on muutumatu?
<details><summary>Vastus</summary>

Õnnestub. Ennik hoiab viidet järjendile ja see viide ei muutu; muutub järjendi sisu. Ennik on muutumatu, tema elemendid ei pruugi olla.
</details>

**11.** Miks annab `[[0] * 3] * 3` ootamatu tulemuse, kui muuta ühte elementi?
<details><summary>Vastus</summary>

Välimine `* 3` kordab **viidet** samale sisemisele järjendile. Kõik kolm rida on sama objekt. Õigesti: `[[0] * 3 for _ in range(3)]`.
</details>

**12.** Sul on 10 000 tootekoodi ja pead korduvalt kontrollima, kas kood on olemas. Kas kasutad järjendit või hulka? Miks?
<details><summary>Vastus</summary>

Hulka. `in` on hulgas keskmiselt konstantse ajaga, järjendis peab Python läbi vaatama elemente ükshaaval.
</details>
