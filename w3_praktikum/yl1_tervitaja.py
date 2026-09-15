from datetime import datetime


def kuva_oigused(vanus):
    """Kuvab kasutaja vanuse põhjal juba kehtivad vanusepiirid."""
    vanusepiirid = {
        14: "süüdiv",
        16: "KOV",
        18: "RK, EP, õlu",
        21: "kasiino",
        24: "A-kategooria juhiluba",
        40: "president",
    }

    for piir, oigus in vanusepiirid.items():
        if vanus >= piir:
            print(f"{piir}+ : {oigus}")


def kysy_synniaasta():
    """Küsib sünniaastat, kuni kasutaja sisestab sobiva väärtuse."""
    praegune_aasta = datetime.now().year

    while True:
        try:
            synniaasta = int(input("Mis su sünniaasta on? "))
        except ValueError:
            print("Sisesta sünniaasta arvuna.")
            continue

        if synniaasta > praegune_aasta:
            print("Sünniaasta ei saa olla tulevikus.")
            continue

        return synniaasta


nimi = input("Mis su nimi on? ").strip()
synniaasta = kysy_synniaasta()
vanus = datetime.now().year - synniaasta

print(f"Tere, {nimi}! Sinu vanusega seotud õigused:")
kuva_oigused(vanus)
