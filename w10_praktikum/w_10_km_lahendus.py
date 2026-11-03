# def mu_fun(arv):
#     return  arv * 7
#
# mu_lambda = lambda arv: arv * 7
#
# print(mu_fun(3))
# print(mu_lambda(3))

# ei sobi, sest iga aasta kohta on vaja uut muutujat
km_maar_2005 = 18.0

# ei sobi, sest puudub kehtima hakkamise aasta
km_maar = [22.0, 18.0, 24.0]

#
km_aastad = [2025, 2005, 2016, 2026]
km_maarad = [22.50, 18.0, 22.0, 24.0]


km_maar_nested = [
    [2025, 22.5],
    [2005, 18.0],
    [2016, 22.0],
    [2026, 24.0],
    [2019, 12.0],
]


for element in range(len(km_maar_nested)):
    print(km_maar_nested[element][0])

'''
list.sort()
sorted(list)
'''
kehtiv_aasta = 2019
km_maar_nested.sort(key=lambda el: el[0])

kehtiv_maar = 0
for aasta_maar in km_maar_nested:
    if kehtiv_aasta >= aasta_maar[0]:
        kehtiv_maar = aasta_maar[1]

print("Aastal", kehtiv_aasta, "oli kehtiv maksumäär:", kehtiv_maar)

print("km_maar_nested:", km_maar_nested)


for maksu_muutus in km_maar_nested:
    print("Muutumis aasta: ", maksu_muutus[0])
    print("Uus määr: ", maksu_muutus[1])


def loe_read(failinimi, kodeering="utf-8"):
    with open(failinimi, encoding=kodeering) as f:
        next(f, None)
        for rida in f:
            yield rida.rstrip("\n")


toodete_arv = 0
toode_rida = []
vanad_mm = {}

otsas_toode = {}
eks_toode = {}


def lisa_toode(nimekiri, toode):
    nimekiri[toode[0]] = {
        'nimetus': toode[1],
        'hind_km_ta': toode[2],
        'laoseis': toode[3],
        'km_maar': toode[4]
    }


#
# def kontrolli_eks_toode(nimekiri, toode):
#     # kas max?
#     if nimekiri.get("max_t")["hind"] < toode[2]:
#         # lisa_toode()
#         pass

# kas min?

# for rida in loe_read("./tooted.csv"):
# for rida in loe_read("/home/helar/projects/emu/teaching/mi_2030_programmeerimise_alused/prog_alus/w10_praktikum/data/tooted_cpy.csv"):
# for rida in loe_read("./data/tooted_cpy.csv"):
for rida in loe_read("./tooted.csv"):
    ['inventari_nr', 'nimetus', 'hind_km_ta', 'laoseis', 'km_maar']
    ['INV-101894', 'Veebikaamera Lite', '60.19', '240', '22']
    toode_rida = rida.split(";")
    toodete_arv += 1
    vanad_mm[toode_rida[4]] = vanad_mm.get(toode_rida[4], 0) + 1

    toote_kogus_int = int(toode_rida[3])
    if toote_kogus_int <= 0:
        lisa_toode(otsas_toode, toode_rida)

    # kontrolli_eks_toode(eks_toode, toode_rida)

print()
