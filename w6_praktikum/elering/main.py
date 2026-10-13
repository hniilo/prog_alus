"""Pärib homsed päev-ette elektrihinnad, salvestab faili, loeb failist ja näitab odavaimad ajad.

Käivita:  python main.py
"""
from datetime import date, time, timedelta

from paring import paeva_hinnad
from fail import salvesta, loe
from tootlus import sordi_hinna_jargi, odavaimad_vahemikus

FAILI_NIMI = "hinnad"
TAISPAEV = 96  # 24 h x 4 intervalli


def naita(pealkiri: str, hinnad: dict, mitu: int | None = None) -> None:
    """Prindib hinnad tabelina; `mitu` piirab ridade arvu (None = kõik)."""
    print(f"\n{pealkiri}")
    for aeg, hind in list(hinnad.items())[:mitu]:
        print(f"  {aeg:%d.%m %H:%M}  {hind:7.2f} EUR/MWh")


def main() -> None:
    paev = date.today() + timedelta(days=1)
    hinnad = paeva_hinnad(paev)
    if len(hinnad) < TAISPAEV:
        print(f"Homse ({paev}) hinnad pole veel avaldatud (avaldatakse ~14:00), kasutan tänaseid.")
        paev = date.today()
        hinnad = paeva_hinnad(paev)

    salvesta(hinnad, FAILI_NIMI)
    hinnad = loe(FAILI_NIMI)

    naita(f"{paev} kõik hinnad ({len(hinnad)} intervalli):", hinnad)
    naita("10 odavaimat intervalli:", sordi_hinna_jargi(hinnad), 10)
    naita("Odavaimad öösel 22:00-06:00:", odavaimad_vahemikus(hinnad, time(22), time(6)), 10)
    naita("Odavaimad päeval 08:00-17:00:", odavaimad_vahemikus(hinnad, time(8), time(17)), 10)


if __name__ == "__main__":
    main()
