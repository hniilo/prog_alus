tulemus = {
    "toodete_koguarv": 0,
    "km_toodete_arv": {},
    "laost_otsas_tooted": [],
    'eks_tooted': {
        "kalleim": {"inventari_nr": "", "nimetus": "", "hind_km_ta": ""},
        "odavaim": {"inventari_nr": "", "nimetus": "", "hind_km_ta": ""}
    },
}

km_maar_nested = [
    [2025, 22.5],
    [2005, 18.0],
    [2016, 22.0],
    [2026, 24.0],
    [2019, 12.0],
]

kehtiv_maar = -1  # negatiivne määra algväärtus aitab testida kehtiva määra leidmist
kehtiv_aasta = 2019


def sordi_km_maarad(aasta_km_list, sortimise_alus="aasta"):
    idx = 0 if sortimise_alus == "aasta" else 1

    aasta_km_list.sort(key=lambda aasta_km: aasta_km[idx])


def loe_read(failinimi, kodeering="utf-8"):
    with open(failinimi, encoding=kodeering) as f:
        next(f, None)
        for rida in f:
            yield [veerg.strip() for veerg in rida.split(";")]


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

    def liida_toodete_koguarvule_yks(toodete_koguarv="toodete_koguarv"):
        tulemus[toodete_koguarv] += 1

    def erista_km_toodete_arv(km_maar):
        tulemus["km_toodete_arv"][km_maar] += 1

    def lisa_laost_otsas_toode(nimetus):
        tulemus["laost_otsas_tooted"].append(nimetus)

    def lisa_ekstreemum_tooted(inventari_nr, nimetus, hind_km_ta):
        "lisa siia min ja max loogika"
        pass

    def tootle_rida(faili_gen):
        # for rida in faili_gen:
        for inventari_nr, nimetus, hind_km_ta, laoseis, km_maar in faili_gen:
            liida_toodete_koguarvule_yks()
            erista_km_toodete_arv(km_maar)
            lisa_laost_otsas_toode(nimetus)
            lisa_ekstreemum_tooted(inventari_nr, nimetus, hind_km_ta)
        pass

    #
    # def kontrolli_eks_toode(nimekiri, toode):
    #     # kas max?
    #     if nimekiri.get("max_t")["hind"] < toode[2]:
    #         # lisa_toode()
    #         pass

    def main():
        sordi_km_maarad(km_maar_nested)
        faili_read = loe_read("./data/tooted.csv")
        tootle_rida(faili_read)

    if __name__ == "__main__":
        main()
