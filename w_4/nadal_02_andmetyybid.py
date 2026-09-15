"""
Nädal 2 — Andmetüübid ja AI-töövoog
Kontseptuaalne samm: andmel on tüüp ja tüüp määrab käitumise.

Fookus: int, float, str, bool, teisendused, f-stringid, tüübivihjed,
maagilised numbrid -> nimega konstandid. Seadista ruff (E, F reeglid + format).
"""

# 1. Arve
# Küsi kauba hind (float) ja kogus (int).
# Arvuta käibemaks (kasuta nimega konstanti KAIBEMAKSU_MAAR = 0.22)
# ja kogusumma. Väljasta korralikult joondatud tšekk kahe komakohaga,
# kasutades f-stringe (nt f"{summa:.2f}").


# 2. Maagiliste numbrite jaht
# All on skript kaheksa seletamatu arvuga. Leia kõik "maagilised numbrid"
# ja anna neile tähendusega nimed konstantidena. Väljund ei tohi muutuda.
print(3.14159 * 5 * 5)
print(9 / 5 * 20 + 32)
print(1000 * 1.05)
print(60 * 60 * 24)


# 3. Ujukoma-detektiiv
# Kontrolli, kas 0.1 + 0.2 == 0.3. Prindi tulemus.
# Katseta, mis vahemikus erinevus tekib (nt 0.1 + 0.2 - 0.3).
# Kommentaarina kirjuta lahti: miks ei tohiks raha hoida float-ina?


# 4. Tüübi-vaatlus
# Prindi välja ja kommenteeri, mida iga avaldis tagastab ja miks:
print("5" * 3)
print(5 * 3)
print("5" + "3")
# print(5 + "3")  # see rida annab vea — kommenteeri lahti ja seleta, mis viga tuleb


# 5. AI-audit
# Küsi mõnelt AI-assistendilt (või kujuta ette) lahendus ülesandele
# "arvuta keskmine temperatuur antud kolme väärtuse põhjal".
# Kirjuta see lahendus siia ja leia sellest vähemalt kaks probleemi
# (tüübiteisendus? maagiline number? halb nimetus? tühi sisend?).
# Paranda probleemid.


# 6. Tüübivihjed
# Kirjuta funktsioon arvuta_pindala, millel on tüübivihjed
# parameetritele ja tagastusväärtusele:
# def arvuta_pindala(pikkus_m: float, laius_m: float) -> float:
# Funktsioon tagastagu pindala ruutmeetrites.


# 7. Temperatuuri teisendaja
# Küsi temperatuur Celsiuses (float).
# Teisenda Fahrenheitiks (F = C * 9/5 + 32) ja Kelviniks (K = C + 273.15).
# Väljasta mõlemad kahe komakohaga.


# 8. Bool ja tõesus
# Küsi kasutaja vanus. Väljasta bool-väärtus, kas vanus on
# täisealiseks (>= 18). Väljasta ka teistpidi: kas on alaealine.


# 9. Hinnaarvestus, versioon 0 (läbiv näide)
# All on tahtlikult halb kood: viis artiklit, käibemaks korrutatud
# maagilise arvuga 1.22 viies eri kohas.
print("Leib: ", 1.29 * 1.22)
print("Piim: ", 0.99 * 1.22)
print("Sai: ", 1.45 * 1.22)
print("Või: ", 3.20 * 1.22)
print("Juust: ", 5.60 * 1.22)
# Ülesanne: anna 1.22-le nimi (KAIBEMAKSU_MAAR) ja eralda
# netohind brutohinnast eraldi muutujatena iga artikli kohta.
# (Ei ole veel vaja tsüklit ega funktsiooni.)


# 10. Stringide vormindus
# Antud on toote nimi, hind ja kogus. Väljasta ühtlaselt joondatud
# rida kujul "Leib        1.29 EUR   x 2" kasutades f-stringi
# laiuse ja joonduse määrangutega (nt f"{nimi:<12}{hind:>6.2f} EUR").
