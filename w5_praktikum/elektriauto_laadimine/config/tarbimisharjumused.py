from datetime import time

# LAADIMISAJA_GRUPID = {
#     (0, 1, 3, 4): (time(23, 0), time(6, 50)),
#     (2,): (time(22, 0), time(7, 30)),
#     (5, 6): None,
# }

NADALA_LAADIMISAJAD = {
    # nädalapäev : [ laadimise alguse kellaaeg, laadimise lõpetamise kellaaeg ]
    0: [time(23, 0), time(6, 50)],  # esmaspäev
    1: [time(23, 0), time(6, 50)],  # teisipäev
    2: [time(23, 0), time(6, 50)],  # kolmapäev
    3: [time(23, 0), time(6, 50)],  # neljapäev
    4: [time(23, 0), time(6, 50)],  # reede
    5: [time(0, 0), time(0, 0)],    # laupäev: kogu päev
    6: [time(0, 0), time(12, 0)],    # pühapäev: kogu päev
}


def on_lubatud_kellaaeg(kellaaeg, vahemik):
    """Kontrolli, kas kellaaeg jääb lubatud ajavahemikku."""
    algus, lopp = vahemik

    if algus == lopp: # ööpäev on lubatud
        return True
    if algus < lopp: # enne südaööd
        return algus <= kellaaeg < lopp
    # järgmine päev
    return algus <= kellaaeg or kellaaeg < lopp
