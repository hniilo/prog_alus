"""Pärib Eleringi kogulehelt (dashboard.elering.ee) tänased päev-ette elektrihinnad,
prindib need ja salvestab faili hinnad.csv.

API dokumentatsioon: https://dashboard.elering.ee/assets/swagger-ui/index.html
Vastus tuleb 15-minutiliste intervallidena: {'timestamp': unix-aeg, 'price': EUR/MWh}.
Ajad arvutatakse Eesti ajavööndis (Europe/Tallinn), sõltumata arvuti enda seadetest.

Käivita:  python elering_hinnad.py
"""
import csv
from datetime import datetime, time
from zoneinfo import ZoneInfo

import requests

API = "https://dashboard.elering.ee/api/nps/price"
FAILI_NIMI = "hinnad.csv"
EESTI = ZoneInfo("Europe/Tallinn")


def tanased_hinnad() -> dict[datetime, float]:
    """Tagastab tänased hinnad sõnastikuna {Eesti kellaaeg: hind EUR/MWh}.

    API ootab algus- ja lõpuaega koos ajavööndiga (ISO 8601), lõpp on kaasa arvatud,
    seega küsime Eesti aja järgi 00:00:00 kuni 23:59:59.
    """
    tana = datetime.now(EESTI).date()
    algus = datetime.combine(tana, time.min, tzinfo=EESTI)
    lopp = datetime.combine(tana, time.max, tzinfo=EESTI)
    vastus = requests.get(API, params={"start": algus.isoformat(), "end": lopp.isoformat()})
    vastus.raise_for_status()

    hinnad = {}
    for kirje in vastus.json()["data"]["ee"]:
        aeg = datetime.fromtimestamp(kirje["timestamp"], EESTI)
        hinnad[aeg] = kirje["price"]
    return hinnad


def salvesta_csv(hinnad: dict[datetime, float], failinimi: str) -> None:
    """Kirjutab hinnad CSV-faili: esimesel real veerupäised, edasi aeg;hind."""
    with open(failinimi, "w", newline="") as f:
        kirjutaja = csv.writer(f, delimiter=";")
        kirjutaja.writerow(["aeg", "hind_eur_mwh"])
        for aeg, hind in hinnad.items():
            kirjutaja.writerow([f"{aeg:%Y-%m-%d %H:%M}", hind])

def salvesta_faili(faili_nimi: str, data: list) -> None:
    """Kirjutab listi iga elemendi eraldi reale.

    write() võtab ainult teksti, seega teisendame iga elemendi str()-iga
    ja liidame reavahetustega üheks tekstiks.
    """
    read = [str(element) for element in data]
    with open(faili_nimi, "w") as f:
        f.write("\n".join(read) + "\n")


def main() -> None:
    hinnad = tanased_hinnad()
    salvesta_csv(hinnad, FAILI_NIMI)

    odavaim = min(hinnad, key=hinnad.get)
    salvesta_faili("odav.txt", [str(odavaim), hinnad.get(odavaim)])
    kalleim = max(hinnad, key=hinnad.get)
    salvesta_faili("kallis.txt", [str(kalleim), hinnad.get(kalleim)])

if __name__ == "__main__":
    main()
    # leia soodne
    # kirjuta_faili(faili_nimi, soodne_data)
    # leia kallis
    # kirjuta failifaili_nimi, kallis_data)
