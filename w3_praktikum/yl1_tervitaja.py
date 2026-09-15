from datetime import datetime

KATSETE_ARV = 3 # globaalne muutuja


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


def kysi_synniaasta(sisend=input, valjund=print, praegune_aasta=None):
    """Küsib kuni kolm korda sobivat sünniaastat ja tagastab selle või None."""
    if praegune_aasta is None:
        praegune_aasta = datetime.now().year

    for _ in range(KATSETE_ARV):
        try:
            synniaasta = int(sisend("Mis su sünniaasta on? "))
        except ValueError:
            valjund("Sisesta sünniaasta arvuna.")
            continue

        if synniaasta > praegune_aasta:
            valjund("Sünniaasta ei saa olla tulevikus.")
            continue

        return synniaasta

    valjund(
        f"Sünniaasta sisestamine ebaõnnestus pärast {KATSETE_ARV} katset. "
        "Programm lõpetab töö."
    )
    return None


def kysi_nime():
    """Küsib kasutaja nime."""
    return input("Mis su nimi on? ").strip()


def kuva_kasutaja_andmed(kasutaja_nimi, kasutaja_synniaasta):
    """Kuvab tervituse ja vanuse põhjal kehtivad õigused."""
    vanus = datetime.now().year - kasutaja_synniaasta

    print(f"Tere, {kasutaja_nimi}! Oled {vanus}. aastane vana ja Sinu vanusega seotud õigused:")
    kuva_oigused(vanus)


def main():
    """Käivitab programmi kasutajaliidese."""
    nimi = kysi_nime()
    synniaasta = kysi_synniaasta()

    if synniaasta is None:
        return

    kuva_kasutaja_andmed(nimi, synniaasta)


if __name__ == "__main__":
    main()
