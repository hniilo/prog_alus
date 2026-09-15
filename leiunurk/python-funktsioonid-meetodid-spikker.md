# Python: enamkasutatavad funktsioonid ja meetodid

> **Spikker** · MI.2030 · Python 3.12+
> Näited on kontrollitud Python 3.12-ga. Kommentaar `# →` näitab tulemust.
> Andmetüüpide omadused ja tüübipõhised meetodid detailselt: vt `python-andmetyybid-spikker.md`.

| Tähis | Tähendus |
|---|---|
| **R** | *Reegel* — interpretaator nõuab; rikkumine annab vea |
| **K** | *Konventsioon* — PEP 8 või hea tava; interpretaator ei kontrolli |
| ⚠️ | Levinud lõks |

---

## Sisukord

1. [Funktsioon vs meetod](#1-funktsioon-vs-meetod)
2. [Sisend ja väljund](#2-sisend-ja-väljund)
3. [f-sõnede vormindus](#3-f-sõnede-vormindus)
4. [Sisseehitatud funktsioonid](#4-sisseehitatud-funktsioonid)
5. [Meetodite kiirülevaade tüüpide kaupa](#5-meetodite-kiirülevaade-tüüpide-kaupa)
6. [Oma funktsioonide kirjutamine](#6-oma-funktsioonide-kirjutamine)
7. [Veakäsitlus](#7-veakäsitlus)
8. [Failid](#8-failid)
9. [Standardteegi sagedasemad moodulid](#9-standardteegi-sagedasemad-moodulid)
10. [Kontrollküsimused](#10-kontrollküsimused)

---

## 1. Funktsioon vs meetod

| | Funktsioon | Meetod |
|---|---|---|
| Kuju | `nimi(argumendid)` | `objekt.nimi(argumendid)` |
| Näide | `len(tooted)` | `tooted.append("leib")` |
| Seos tüübiga | töötab paljude tüüpidega | kuulub konkreetsele tüübile |
| Uurimine | `help(len)` | `help(list.append)`, `dir(tooted)` |

### Muudab kohapeal või tagastab uue?

See on **kõige olulisem küsimus** iga meetodi või funktsiooni juures.

| Muudab objekti, tagastab `None` | Tagastab uue, originaal jääb |
|---|---|
| `a.sort()` | `sorted(a)` |
| `a.reverse()` | `reversed(a)` · `a[::-1]` |
| `a.append(x)` | `a + [x]` |
| `d.update(e)` | `d \| e` |
| `s.add(x)` | `s \| {x}` |
| `random.shuffle(a)` | `random.sample(a, len(a))` |
| — (sõne on muutumatu) | `tekst.upper()`, `tekst.replace(...)`, `tekst.strip()` |

⚠️ `a = a.sort()` → `a` on nüüd `None`.

---

## 2. Sisend ja väljund

### `print()`

```python
print("a", "b", "c")            # → a b c
print("a", "b", sep="-")        # → a-b
print("laadin", end="...")      # ei vaheta rida
print()                         # tühi rida
print(1, "tere", [2, 3])        # → 1 tere [2, 3]   suvalised tüübid
```

| Parameeter | Vaikimisi | Tähendus |
|---|---|---|
| `sep` | `" "` | eraldaja argumentide vahel |
| `end` | `"\n"` | mis prinditakse lõppu |
| `file` | ekraan | kuhu kirjutada (nt avatud fail) |

⚠️ `print()` tagastab `None`. `x = print(5)` → `x` on `None`.

### `input()`

```python
nimi = input("Nimi: ")                  # tagastab ALATI str
kogus = int(input("Kogus: "))           # ValueError, kui pole täisarv
arvud = list(map(int, input().split())) # "3 5 7" → [3, 5, 7]
```

⚠️ `input("Kogus: ") * 2` sisendiga `3` annab `'33'`, mitte `6`.

---

## 3. f-sõnede vormindus

Kuju: `f"{avaldis:vorming}"`

| Vorming | Näide | Tulemus | Tähendus |
|---|---|---|---|
| `.2f` | `f"{3.14159:.2f}"` | `3.14` | 2 kohta pärast koma |
| `,` | `f"{1234567:,}"` | `1,234,567` | tuhandete eraldaja |
| `,.2f` | `f"{1234.5:,.2f}"` | `1,234.50` | koos |
| `.1%` | `f"{0.256:.1%}"` | `25.6%` | protsendina |
| `>8` | `f"{'leib':>8}"` | `'    leib'` | paremale, laius 8 |
| `<8` | `f"{'leib':<8}"` | `'leib    '` | vasakule, laius 8 |
| `^8` | `f"{'leib':^8}"` | `'  leib  '` | keskele, laius 8 |
| `08.2f` | `f"{3.5:08.2f}"` | `00003.50` | nullidega täitmine |
| `03d` | `f"{7:03d}"` | `007` | täisarv nullidega |
| `=` | `f"{kogus=}"` | `kogus=5` | silumiseks |
| `!r` | `f"{'5'!r}"` | `'5'` | `repr()` kuju — näitab jutumärke |

**Tabeli joondamine:**

```python
print(f"{'Toode':<10}{'Kogus':>6}{'Summa':>10}")
print(f"{'leib':<10}{2:>6}{3.78:>10.2f}")
# Toode      Kogus     Summa
# leib           2      3.78
```

⚠️ **Eesti numbrivorming** (tühik tuhandete vahel, koma kümnendkohas) ei tule automaatselt:

```python
f"{1234.5:,.2f}".replace(",", " ").replace(".", ",")   # → '1 234,50'
```

---

## 4. Sisseehitatud funktsioonid

Neid ei pea importima.

### 4.1 Tüübid ja teisendused

| Funktsioon | Tegevus | Näide | Tulemus |
|---|---|---|---|
| `type(x)` | objekti tüüp | `type(3.5)` | `<class 'float'>` |
| `isinstance(x, tüüp)` | kas `x` on seda tüüpi | `isinstance(5, int)` | `True` |
| `isinstance(x, (t1, t2))` | kas mõni neist | `isinstance(5, (int, float))` | `True` |
| `int(x)` | täisarvuks | `int("42")` | `42` |
| `float(x)` | ujukomaarvuks | `float("3.5")` | `3.5` |
| `str(x)` | sõneks (kasutajale) | `str(3.5)` | `'3.5'` |
| `repr(x)` | sõneks (programmeerijale) | `repr("5")` | `"'5'"` |
| `bool(x)` | tõeväärtuseks | `bool([])` | `False` |
| `list(x)` · `tuple(x)` · `set(x)` | jadast kogumiks | `list("ab")` | `['a', 'b']` |
| `dict(x)` | paaridest sõnastikuks | `dict([("a", 1)])` | `{'a': 1}` |

**K:** tüübi kontrolliks eelista `isinstance(x, int)` võrdlusele `type(x) == int`.
⚠️ `isinstance(True, int)` → `True`, sest `bool` on `int`-i alamtüüp.

### 4.2 Arvud

| Funktsioon | Näide | Tulemus | Märkus |
|---|---|---|---|
| `abs(x)` | `abs(-3)` | `3` | |
| `round(x)` | `round(2.5)` | `2` | ⚠️ poole juures paarisarvuni |
| `round(x, n)` | `round(3.14159, 2)` | `3.14` | |
| `min(...)` · `max(...)` | `max(3, 7, 5)` | `7` | ka jadaga: `max([3, 7, 5])` |
| `sum(jada)` | `sum([1, 2, 3])` | `6` | |
| `sum(jada, algus)` | `sum([1, 2], 10)` | `13` | |
| `pow(a, b)` | `pow(2, 10)` | `1024` | sama mis `2 ** 10` |
| `divmod(a, b)` | `divmod(17, 5)` | `(3, 2)` | jagatis ja jääk |

⚠️ `max([])` → `ValueError`. Kasuta `max(hinnad, default=0)`.
⚠️ `sum(["a", "b"])` → `TypeError`. Sõnede jaoks: `"".join(["a", "b"])`.

### 4.3 Jadad ja iteratsioon

| Funktsioon | Tegevus | Näide | Tulemus |
|---|---|---|---|
| `len(x)` | elementide arv | `len("tere")` | `4` |
| `range(...)` | arvujada | `list(range(3))` | `[0, 1, 2]` |
| `enumerate(jada, start=0)` | `(indeks, element)` paarid | `list(enumerate("ab"))` | `[(0, 'a'), (1, 'b')]` |
| `zip(a, b, ...)` | paneb jadad paari | `list(zip("ab", [1, 2]))` | `[('a', 1), ('b', 2)]` |
| `sorted(jada)` | uus sorteeritud järjend | `sorted([3, 1, 2])` | `[1, 2, 3]` |
| `reversed(jada)` | tagurpidi iteraator | `list(reversed([1, 2]))` | `[2, 1]` |
| `any(jada)` | kas vähemalt üks on tõene | `any([0, 0, 1])` | `True` |
| `all(jada)` | kas kõik on tõesed | `all([1, 1, 0])` | `False` |
| `map(f, jada)` | rakendab `f` igale elemendile | `list(map(str, [1, 2]))` | `['1', '2']` |
| `filter(f, jada)` | jätab elemendid, kus `f` on tõene | `list(filter(None, [0, 1, 2]))` | `[1, 2]` |

#### `enumerate` — kui on vaja ka järjekorranumbrit

```python
tooted = ["leib", "piim", "juust"]
for nr, toode in enumerate(tooted, start=1):
    print(f"{nr}. {toode}")
# 1. leib
# 2. piim
# 3. juust
```

**K:** `for i in range(len(tooted)): print(tooted[i])` asemel kasuta `for toode in tooted:` või `enumerate`.

#### `zip` — mitu jada korraga

```python
nimed = ["leib", "piim", "juust"]
hinnad = [1.89, 0.99, 4.49]

for nimi, hind in zip(nimed, hinnad):
    print(nimi, hind)

dict(zip(nimed, hinnad))     # → {'leib': 1.89, 'piim': 0.99, 'juust': 4.49}
```

⚠️ `zip` lõpetab **lühima** jada lõpus ilma veata. Kui pikkused peavad klappima: `zip(a, b, strict=True)` → `ValueError`.

#### `sorted`, `min`, `max` ja `key`

`key` on **funktsioon**, mida kutsutakse iga elemendi jaoks; võrreldakse selle tagastusväärtusi.

```python
hinnakiri = {"leib": 1.89, "piim": 0.99, "juust": 4.49}

sorted(hinnakiri)                          # → ['juust', 'leib', 'piim']   võtmed tähestikus
sorted(hinnakiri, key=hinnakiri.get)       # → ['piim', 'leib', 'juust']   hinna järgi
max(hinnakiri, key=hinnakiri.get)          # → 'juust'                     kalleim toode

sorted(hinnakiri.items(), key=lambda paar: paar[1], reverse=True)
# → [('juust', 4.49), ('leib', 1.89), ('piim', 0.99)]

min(["Tartu", "Tallinn", "Elva"], key=len) # → 'Elva'
sorted(["b", "A", "c"], key=str.lower)     # → ['A', 'b', 'c']
```

⚠️ `key=len`, mitte `key=len()` — anname funktsiooni, mitte selle tulemust.

#### `any` ja `all`

```python
hinnad = [1.89, 0.99, 4.49]
any(h > 4 for h in hinnad)    # → True    kas leidub kallis toode?
all(h > 0 for h in hinnad)    # → True    kas kõik hinnad on positiivsed?
all([])                        # → True    ⚠️ tühi jada rahuldab iga tingimuse
```

#### `map` ja `filter` vs komprehensioon

```python
list(map(int, ["1", "2", "3"]))          # → [1, 2, 3]       valmis funktsiooniga — hea
list(filter(lambda h: h > 1, hinnad))    # → [1.89, 4.49]
[h for h in hinnad if h > 1]             # → [1.89, 4.49]    K: sama, loetavam
```

**K:** kui `map`/`filter` vajaks `lambda`-t, kirjuta komprehensioon.

#### ⚠️ Iteraatorid on ühekordsed

```python
paarid = zip(nimed, hinnad)
print(paarid)       # → <zip object at 0x...>   mitte andmed!
list(paarid)        # → [('leib', 1.89), ('piim', 0.99), ('juust', 4.49)]
list(paarid)        # → []   iteraator on ammendatud
```

Ühekordsed: `zip`, `map`, `filter`, `enumerate`, `reversed`, avatud fail.
Korduvkasutatavad: `list`, `tuple`, `str`, `dict`, `set`, `range`.

### 4.4 Uurimine ja abi

| Funktsioon | Tegevus |
|---|---|
| `help(x)` | dokumentatsioon: `help(str.split)` |
| `dir(x)` | objekti atribuudid ja meetodid |
| `type(x)` | tüüp |
| `id(x)` | objekti identiteet |
| `hash(x)` | räsiväärtus; `TypeError`, kui pole räsitav |

```python
[m for m in dir(str) if not m.startswith("_")]   # sõne avalikud meetodid
```

### 4.5 Märgid

| Funktsioon | Näide | Tulemus |
|---|---|---|
| `ord(märk)` | `ord("õ")` | `245` |
| `chr(kood)` | `chr(245)` | `'õ'` |

### ⚠️ 4.6 Ära kata üle sisseehitatud nimesid

```python
list = [1, 2, 3]       # lubatud (R), aga...
list("abc")            # TypeError: 'list' object is not callable
```

Sagedased ohvrid: `list`, `dict`, `str`, `sum`, `max`, `min`, `input`, `id`, `type`, `len`.
Paremad nimed: `hinnad`, `summa`, `korv`, `suurim`.
💡 Ruff leiab selle reegliga `A001` (tuleb konfiguratsioonis sisse lülitada).

---

## 5. Meetodite kiirülevaade tüüpide kaupa

| Tüüp | Sagedasemad meetodid | Muudab objekti? |
|---|---|---|
| `str` | `lower` `upper` `strip` `split` `join` `replace` `startswith` `endswith` `find` `count` `isdigit` | ei — tagastab uue |
| `list` | `append` `extend` `insert` `pop` `remove` `sort` `reverse` `index` `count` `copy` | jah — enamik tagastab `None` |
| `tuple` | `count` `index` | ei saa muuta |
| `dict` | `get` `items` `keys` `values` `update` `pop` `setdefault` | jah (`get`, `items` jt ainult loevad) |
| `set` | `add` `remove` `discard` `union` `intersection` `difference` | `add`/`remove`/`discard` jah; `union` jt tagastavad uue |

Tabelid näidete, tagastusväärtuste ja vigadega: `python-andmetyybid-spikker.md`.

---

## 6. Oma funktsioonide kirjutamine

### 6.1 Anatoomia

```python
def rea_summa(uhikuhind, kogus, soodustus=0.0):
    """Tagastab ostukorvi rea summa, arvestades soodustust (0.1 = 10%)."""
    return uhikuhind * kogus * (1 - soodustus)

rea_summa(1.89, 2)                    # positsioonilised argumendid
rea_summa(4.49, 1, soodustus=0.1)     # nimega argument
```

| Osa | Näites | Märkus |
|---|---|---|
| `def` | `def` | võtmesõna (**R**) |
| nimi | `rea_summa` | **K**: `snake_case`, kirjeldab tulemust või tegevust |
| parameetrid | `uhikuhind, kogus, soodustus=0.0` | |
| koolon + taane | `:` ja 4 tühikut | koolon ja taane **R**, 4 tühikut **K** |
| dokumendisõne | `"""..."""` | **K**: esimene rida kirjeldab, mida funktsioon teeb |
| `return` | `return ...` | ilma selleta tagastatakse `None` |

### 6.2 Parameetrite liigid

| Definitsioon | Liik | Väljakutse |
|---|---|---|
| `def f(a, b)` | tavalised | `f(1, 2)` · `f(b=2, a=1)` |
| `def f(a, b=0)` | vaikeväärtusega | `f(1)` · `f(1, 5)` |
| `def f(*arvud)` | suvaline arv positsioonilisi → ennik | `f(1, 2, 3)` |
| `def f(**valikud)` | suvaline arv nimega → sõnastik | `f(x=1, y=2)` |
| `def f(a, *, b)` | `b` ainult nimega | `f(1, b=2)` |

**R:** vaikeväärtusega parameetrid tulevad pärast vaikeväärtuseta omi. `def f(a=1, b):` → `SyntaxError`.

### 6.3 Tüübivihjed

```python
from decimal import Decimal

def rea_summa(uhikuhind: Decimal, kogus: int, soodustus: Decimal = Decimal("0")) -> Decimal:
    """Tagastab ostukorvi rea summa, arvestades soodustust."""
    return uhikuhind * kogus * (1 - soodustus)
```

- `list[str]`, `dict[str, float]`, `tuple[str, int]` — kogumite vihjed.
- `int | None` — kas täisarv või `None`.
- Python **ei kontrolli** vihjeid käivitamisel. Need on dokumentatsioon lugejale ja tööriistadele.

### ⚠️ 6.4 `return` vs `print`

```python
def summa_prindib(a, b):
    print(a + b)

def summa_tagastab(a, b):
    return a + b

x = summa_prindib(2, 3)     # prindib 5, aga x on None
y = summa_tagastab(2, 3)    # ei prindi midagi, y on 5
```

**K:** arvutav funktsioon **tagastab** tulemuse. Printimine jääb programmi välimisse kihti. Ainult nii saab funktsiooni kasutada teistes arvutustes ja testida (`pytest`).

### ⚠️ 6.5 Muudetav vaikeväärtus

```python
def lisa_korvi(toode, korv=[]):     # VIGA: [] luuakse ÜKS kord, def-rea täitmisel
    korv.append(toode)
    return korv

print(lisa_korvi("leib"))    # → ['leib']
print(lisa_korvi("piim"))    # → ['leib', 'piim']   eelmise kutse korv!

def lisa_korvi(toode, korv=None):   # õigesti
    if korv is None:
        korv = []
    korv.append(toode)
    return korv
```

⚠️ Funktsioon võib muuta argumendiks antud järjendit või sõnastikku, sest parameeter viitab **samale objektile**. Kui see pole funktsiooni eesmärk, tee koopia või tagasta uus objekt.

### 6.6 Nähtavusala

```python
summa = 0

def lisa(x):
    summa += x      # UnboundLocalError: cannot access local variable 'summa'
```

Omistamine funktsiooni sees teeb nimest **lokaalse** muutuja.
**K:** ära kasuta `global`-it. Anna väärtus parameetrina ja tagasta tulemus:

```python
def lisa(summa, x):
    return summa + x
```

### 6.7 `lambda`

```python
sorted(ostukorv, key=lambda rida: rida[1])    # sorteeri koguse järgi
```

**K:** `lambda` ainult lühikese `key=` argumendina. `ruut = lambda x: x ** 2` asemel kirjuta `def` (ruff `E731`).

### 6.8 Puhta koodi kontroll funktsioonile

| Küsimus | Hea | Halb |
|---|---|---|
| Kas nimi ütleb, mida funktsioon teeb? | `leia_kalleim_toode` | `f2`, `tootle` |
| Kas funktsioonil on üks ülesanne? | arvutab summa | loeb faili + arvutab + prindib |
| Kas tulemus tagastatakse? | `return summa` | `print(summa)` |
| Kas sõltub ainult parameetritest? | `def lisa_soodustus(hind, maar)` | kasutab globaalset muutujat |
| Kas arvudel on nimi? | `SOODUSTUS = 0.10` | `hind * 0.9` |
| Kas mahub ekraanile? | ~20 rida | 100 rida |

---

## 7. Veakäsitlus

```python
def loe_kogus():
    """Küsib kasutajalt koguse, kuni sisestatakse täisarv."""
    while True:
        tekst = input("Kogus: ")
        try:
            return int(tekst)
        except ValueError:
            print("Palun sisesta täisarv.")
```

| Kuju | Millal |
|---|---|
| `try: ... except ValueError:` | püüa konkreetne erind |
| `except (ValueError, TypeError):` | mitu erindit korraga |
| `except ValueError as viga:` | vajad veateadet: `print(viga)` |
| `else:` | käivitub, kui viga **ei** tekkinud |
| `finally:` | käivitub alati |
| `raise ValueError("Kogus peab olema positiivne")` | tekita erind ise |

**K:** ära kasuta paljast `except:` — see peidab ka sinu enda programmivead (ruff `E722`).
**K:** hoia `try` plokk võimalikult lühike — ainult rida, mis võib ebaõnnestuda.

---

## 8. Failid

### 8.1 `open()`

```python
with open("tooted.txt", encoding="utf-8") as f:     # K: alati with ja encoding
    for rida in f:
        print(rida.strip())                           # strip eemaldab \n
```

| Režiim | Tähendus |
|---|---|
| `"r"` | lugemine (vaikimisi) |
| `"w"` | kirjutamine — ⚠️ **kustutab olemasoleva sisu** |
| `"a"` | lisamine faili lõppu |
| `"x"` | uue faili loomine; viga, kui fail on olemas |

| Meetod | Tegevus |
|---|---|
| `f.read()` | kogu sisu ühe sõnena |
| `f.readlines()` | ridade järjend (koos `\n`-ga) |
| `for rida in f:` | rida-realt (mälusäästlik) |
| `f.write(tekst)` | kirjutab; ⚠️ reavahetust ei lisa automaatselt |

⚠️ Ilma `encoding="utf-8"` võivad täpitähed Windowsis katki minna.
💡 `with` sulgeb faili ka siis, kui tekib viga.

### 8.2 `pathlib` — failiteed

```python
from pathlib import Path

kaust = Path("andmed")
fail = kaust / "hinnad.csv"           # / ühendab teeosi igas OS-is õigesti

fail.exists()                         # → True / False
fail.name                             # → 'hinnad.csv'
fail.stem                             # → 'hinnad'
fail.suffix                           # → '.csv'
sisu = fail.read_text(encoding="utf-8")
fail.write_text("tekst", encoding="utf-8")
list(kaust.glob("*.csv"))             # kõik CSV-failid kaustas
Path.home()                           # kasutaja kodukaust
```

---

## 9. Standardteegi sagedasemad moodulid

**K:** impordid faili algusesse. Eelista `import math` → `math.sqrt()`; väldi `from math import *` (ruff `F403`).

### `math`

| Nimi | Näide | Tulemus |
|---|---|---|
| `math.sqrt(x)` | `math.sqrt(16)` | `4.0` |
| `math.ceil(x)` | `math.ceil(2.1)` | `3` |
| `math.floor(x)` | `math.floor(2.9)` | `2` |
| `math.pi` | `math.pi` | `3.141592653589793` |
| `math.isclose(a, b)` | `math.isclose(0.1 + 0.2, 0.3)` | `True` |
| `math.prod(jada)` | `math.prod([2, 3, 4])` | `24` |

⚠️ `math.floor(-2.5)` → `-3`, aga `int(-2.5)` → `-2`.

### `random`

| Nimi | Tegevus |
|---|---|
| `random.random()` | ujukomaarv vahemikus [0, 1) |
| `random.randint(a, b)` | täisarv `a`…`b` — ⚠️ **mõlemad otsad kaasa arvatud** |
| `random.choice(jada)` | üks juhuslik element |
| `random.sample(jada, k)` | `k` erinevat elementi uues järjendis |
| `random.shuffle(a)` | segab kohapeal, tagastab `None` |
| `random.seed(42)` | korratav „juhuslikkus" — kasulik testimisel |

### `statistics`

```python
import statistics
hinded = [3, 5, 4, 5, 2]
statistics.mean(hinded)     # → 3.8
statistics.median(hinded)   # → 4
statistics.mode(hinded)     # → 5
statistics.stdev(hinded)    # standardhälve
```

### `decimal`

```python
from decimal import Decimal, ROUND_HALF_UP

hind = Decimal("1.89") * 3                                  # → Decimal('5.67')
hind.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)      # ümardamine sentideni
```

⚠️ Loo alati sõnest: `Decimal("0.1")`, mitte `Decimal(0.1)`.

### `datetime`

```python
from datetime import date, datetime, timedelta

date.today()                                        # tänane kuupäev
datetime.now()                                      # praegune kuupäev ja kellaaeg
date(2026, 9, 10).strftime("%d.%m.%Y")              # → '10.09.2026'
datetime.strptime("10.09.2026", "%d.%m.%Y")         # sõnest kuupäevaks
date(2026, 9, 8) + timedelta(weeks=11)              # → date(2026, 11, 24)
(date(2026, 11, 24) - date(2026, 9, 8)).days        # → 77
```

| Kood | Tähendus | Kood | Tähendus |
|---|---|---|---|
| `%d` | päev (01–31) | `%H` | tund (00–23) |
| `%m` | kuu (01–12) | `%M` | minut |
| `%Y` | aasta (2026) | `%S` | sekund |

### `json`

```python
import json

hinnad = {"leib": 1.89, "õun": 0.45}

with open("hinnad.json", "w", encoding="utf-8") as f:
    json.dump(hinnad, f, ensure_ascii=False, indent=2)     # ensure_ascii=False säilitab täpitähed

with open("hinnad.json", encoding="utf-8") as f:
    hinnad = json.load(f)
```

| Funktsioon | Tegevus |
|---|---|
| `json.dump(obj, fail)` | kirjutab faili |
| `json.load(fail)` | loeb failist |
| `json.dumps(obj)` | objekt → sõne |
| `json.loads(tekst)` | sõne → objekt |

⚠️ JSON-i võtmed on alati sõned: `json.loads(json.dumps({1: "a"}))` → `{'1': 'a'}`.
⚠️ `Decimal` pole JSON-iks teisendatav → `TypeError`. Salvesta `str(hind)`.

### `csv`

```python
import csv

with open("hinnad.csv", encoding="utf-8-sig", newline="") as f:
    for rida in csv.DictReader(f, delimiter=";"):
        hind = float(rida["hind"].replace(",", "."))
        print(rida["toode"], hind)
```

⚠️ CSV-st loetud väärtused on **alati sõned** — teisenda ise.
⚠️ Eesti keelega Excel salvestab CSV sageli `;`-eraldajaga ja komaga kümnendkohas.
⚠️ Exceli „CSV UTF-8" lisab faili algusesse BOM-märgi → kasuta `encoding="utf-8-sig"`, muidu esimese veeru nimi on `'\ufefftoode'`.

### `collections`

```python
from collections import Counter, defaultdict

ostud = ["leib", "piim", "leib", "juust", "leib"]
loendur = Counter(ostud)        # → Counter({'leib': 3, 'piim': 1, 'juust': 1})
loendur.most_common(1)          # → [('leib', 3)]
loendur["sai"]                  # → 0   KeyErrorit ei teki

kategooriad = defaultdict(list)
kategooriad["pagar"].append("leib")    # võti luuakse automaatselt tühja järjendiga
```

### `copy`

| Funktsioon | Tegevus |
|---|---|
| `copy.copy(x)` | pinnapealne koopia |
| `copy.deepcopy(x)` | sügav koopia — ka pesastatud objektid kopeeritakse |

---

## 10. Kontrollküsimused

**1.** Mida prindib?
```python
def kahekordista(x):
    print(x * 2)

tulemus = kahekordista(5)
print(tulemus)
```
<details><summary>Vastus</summary>

`10` ja siis `None`. Funktsioon prindib, aga ei tagasta midagi.
</details>

**2.** Miks `sorted(hinnakiri, key=hinnakiri.get)` töötab, aga `sorted(hinnakiri, key=hinnakiri.get())` mitte?
<details><summary>Vastus</summary>

`key` ootab funktsiooni, mida Python ise iga elemendi jaoks kutsub. `hinnakiri.get()` kutsub meetodi kohe välja (ja ilma argumendita annab see `TypeError`).
</details>

**3.** Mida prindib?
```python
paarid = zip(["a", "b"], [1, 2])
print(len(list(paarid)))
print(len(list(paarid)))
```
<details><summary>Vastus</summary>

`2` ja `0`. `zip` tagastab iteraatori, mis ammendub esimesel läbimisel.
</details>

**4.** Mis juhtub, kui kutsuda `lisa_korvi("leib")` kaks korda, kui definitsioon on `def lisa_korvi(toode, korv=[])`?
<details><summary>Vastus</summary>

Teisel korral on korvis juba eelmine toode. Vaikeväärtus luuakse ühe korra funktsiooni defineerimisel ja kõik kutsed jagavad sama järjendit. Lahendus: `korv=None` ja kontroll funktsiooni sees.
</details>

**5.** Mis vahe on `random.randint(1, 6)` ja `range(1, 6)` otspunktidel?
<details><summary>Vastus</summary>

`randint` sisaldab mõlemat otsa (1…6). `range` ei sisalda lõppu (1…5).
</details>

**6.** Tudeng kirjutas `sum = 0` ja hiljem `sum(hinnad)`. Mis juhtub ja miks?
<details><summary>Vastus</summary>

`TypeError: 'int' object is not callable`. Nimi `sum` viitab nüüd täisarvule, mitte sisseehitatud funktsioonile.
</details>

**7.** Miks on `except ValueError:` parem kui `except:`?
<details><summary>Vastus</summary>

Paljas `except` püüab kinni kõik vead, sh kirjavead (`NameError`) ja programmi katkestamise. Nii jääb päris viga peitu.
</details>

**8.** Loed CSV-failist veeru `hind` ja arvutad `rida["hind"] * 2`. Väärtus oli `1,89`. Mis tuleb tulemuseks ja kuidas parandada?
<details><summary>Vastus</summary>

`'1,891,89'` — CSV väärtus on sõne ja sõne korrutamine kordab seda. Parandus: `float(rida["hind"].replace(",", ".")) * 2`.
</details>

**9.** Millal kasutad `enumerate`, millal `zip`?
<details><summary>Vastus</summary>

`enumerate` — kui on vaja ühe jada elemente koos järjekorranumbriga. `zip` — kui on vaja mitut jada samaaegselt, element-elemendi haaval.
</details>

**10.** Miks peaks hinnaarvutuse funktsioon tagastama tulemuse, mitte seda printima?
<details><summary>Vastus</summary>

Tagastatud väärtust saab kasutada edasistes arvutustes (nt kogusumma), vormindada eri viisil ja kontrollida automaattestiga. Prinditud väärtus jõuab ainult ekraanile.
</details>

---

## Abi leidmine

| Kus | Mida |
|---|---|
| `help(objekt)` | dokumentatsioon otse Pythonis / Thonny Shellis |
| docs.python.org/3/library/functions.html | kõik sisseehitatud funktsioonid |
| docs.python.org/3/library/stdtypes.html | sisseehitatud tüüpide meetodid |
| progeopik.cs.ut.ee | eestikeelne programmeerimise õpik |
