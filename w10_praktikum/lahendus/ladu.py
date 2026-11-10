"""w10 praktikumi näidislahendus: lao hinnad ja käibemaksu tõus 1.07.2025.

Loeb failist tooted.csv tooted, prindib aruande ja salvestab uue hinnakirja
faili tooted_2025_07.csv (mõlemad asuvad kaustas w10_praktikum).

Käivita:  python ladu.py
"""

import csv
import json
from pathlib import Path

KAUST = Path(__file__).parent.parent
SISEND = KAUST / "tooted.csv"
SISEND_JSON = KAUST / "tooted.json"
VALJUND = KAUST / "tooted_2025_07.csv"

KEHTIVAD_MAARAD = (0, 9, 13, 22, 24)
MAARA_MUUTUS = {22: 24}  # 1.07.2025 tõusis üldmäär, teised jäid samaks


def loe_tooted(failinimi):
    """Tagastab failist loetud tooted sõnastike järjendina, väljad õiget tüüpi."""
    tooted = []
    with open(failinimi, encoding="utf-8") as f:
        for rida in csv.DictReader(f, delimiter=";"):
            tooted.append(
                {
                    "inventari_nr": rida["inventari_nr"],
                    "nimetus": rida["nimetus"],
                    "hind_km_ta": float(rida["hind_km_ta"]),
                    "laoseis": int(rida["laoseis"]),
                    "km_maar": int(rida["km_maar"]),
                }
            )
    return tooted


def loe_tooted_json(failinimi):
    """Tagastab JSON-failist loetud tooted; JSONis on arvud juba õiget tüüpi."""
    with open(failinimi, encoding="utf-8") as f:
        return json.load(f)


def hind_km_ga(hind, maar):
    """Tagastab hinna käibemaksuga, ümardatuna 2 kohani."""
    if hind < 0:
        raise ValueError(f"hind ei saa olla negatiivne: {hind}")
    return round(hind * (1 + maar / 100), 2)


def uus_maar(maar):
    """Tagastab käibemaksumäära pärast 1.07.2025."""
    if maar not in KEHTIVAD_MAARAD:
        raise ValueError(f"tundmatu käibemaksumäär: {maar}")
    return MAARA_MUUTUS.get(maar, maar)


def lao_vaartus(tooted, km_ga=False):
    """Tagastab toodete hind * laoseis summa (km_ga=True korral käibemaksuga)."""
    summa = 0
    for toode in tooted:
        hind = toode["hind_km_ta"]
        if km_ga:
            hind = hind_km_ga(hind, toode["km_maar"])
        summa += hind * toode["laoseis"]
    return round(summa, 2)


def uuenda_maarad(tooted):
    """Tagastab uue järjendi, kus igal tootel on 1.07.2025 kehtiv määr."""
    return [toode | {"km_maar": uus_maar(toode["km_maar"])} for toode in tooted]


def loenda_maarad(tooted):
    """Tagastab sõnastiku {määr: toodete arv}."""
    loendur = {}
    for toode in tooted:
        maar = toode["km_maar"]
        loendur[maar] = loendur.get(maar, 0) + 1
    return loendur


def otsas(tooted):
    """Tagastab tooted, mida laos pole."""
    return [toode for toode in tooted if toode["laoseis"] == 0]


def otsi(tooted, sona):
    """Tagastab tooted, mille nimetuses esineb sõna (tõstutundetult)."""
    sona = sona.lower()
    return [toode for toode in tooted if sona in toode["nimetus"].lower()]


def salvesta_hinnakiri(tooted, failinimi):
    """Kirjutab tooted faili koos veeruga hind_km_ga."""
    valjad = [
        "inventari_nr",
        "nimetus",
        "hind_km_ta",
        "laoseis",
        "km_maar",
        "hind_km_ga",
    ]
    with open(failinimi, "w", encoding="utf-8", newline="") as f:
        kirjutaja = csv.DictWriter(f, fieldnames=valjad, delimiter=";")
        kirjutaja.writeheader()
        for toode in tooted:
            hind = hind_km_ga(toode["hind_km_ta"], toode["km_maar"])
            kirjutaja.writerow(toode | {"hind_km_ga": f"{hind:.2f}"})


def kirjelda(toode):
    """Tagastab toote ühe reana: nimetus, inventarinumber ja hinnad."""
    hind = toode["hind_km_ta"]
    return (
        f"{toode['nimetus']} ({toode['inventari_nr']}): "
        f"{hind:.2f} € km-ta, {hind_km_ga(hind, toode['km_maar']):.2f} € km-ga"
    )


def main():
    tooted = loe_tooted(SISEND)
    print(f"Tooteid kokku: {len(tooted)}")

    for maar, arv in sorted(loenda_maarad(tooted).items()):
        print(f"  määraga {maar}%: {arv}")

    laost_otsas = otsas(tooted)
    print(f"Laost otsas: {len(laost_otsas)}")
    for toode in laost_otsas:
        print(f"  {toode['nimetus']}")

    print("Kõige kallim:", kirjelda(max(tooted, key=lambda t: t["hind_km_ta"])))
    print("Kõige odavam:", kirjelda(min(tooted, key=lambda t: t["hind_km_ta"])))

    uued = uuenda_maarad(tooted)
    vana = lao_vaartus(tooted, km_ga=True)
    uus = lao_vaartus(uued, km_ga=True)
    print(f"Lao väärtus km-ta:          {lao_vaartus(tooted):>14,.2f} €")
    print(f"Lao väärtus km-ga (vana):   {vana:>14,.2f} €")
    print(f"Lao väärtus km-ga (uus):    {uus:>14,.2f} €")
    print(f"Vahe:                       {uus - vana:>14,.2f} €")

    salvesta_hinnakiri(uued, VALJUND)
    print(f"Uus hinnakiri salvestatud: {VALJUND.name}")

    # lisaülesanne
    print("JSON-failis on samad andmed:", loe_tooted_json(SISEND_JSON) == tooted)
    print(f"Tooteid sõnaga 'piim': {len(otsi(tooted, 'piim'))}")
    for maar in sorted(loenda_maarad(uued)):
        sama_maaraga = [toode for toode in uued if toode["km_maar"] == maar]
        print(
            f"  määraga {maar}% lao väärtus km-ga: {lao_vaartus(sama_maaraga, True):,.2f} €"
        )


if __name__ == "__main__":
    main()
