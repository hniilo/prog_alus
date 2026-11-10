'''
Saaremaal, Rahuste külas, ühes väikemajas peetakse garaažimüüki.
Seal elav vanataat on otsustanud oma vinüülplaatide kogu maha müüa
Ta on aastakümneid kogunud erinevate žanrite ja aastakümnete muusikat, kuid nüüd on aeg edasi liikuda
Tal on mitu kastitäit vinüülplaate, mida ta on hoolikalt hoidnud ning on kirja pannud kõik plaadid, mida ta kunagi kogunud on.

Ridade kaupa on paberile kirja pandud iga plaadi pealkiri, žanr ja väljaandmise aasta.

Kirjuta programm, mis loeb vanataadi vinüülplaatide kogu andmed failist ja võimaldab kasutajal otsida plaate žanri või/ja aasta järgi.

Võtab sisendina faili nime.

Küsib kasutajalt žanri (jätta tühjaks, kui ei soovi žanri järgi otsida).

Küsib kasutajalt aasta (jätta tühjaks, kui ei soovi aasta järgi otsida).

Väljastab kõik plaadid, mis vastavad kasutaja sisestatud kriteeriumitele
Kui kasutaja ei sisesta ühtegi kriteeriumi, tagastab programm kõik plaadid.

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr:
>> Sisesta ajavahemik: 1970

The Beatles - Let It Be

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr: pop
>> Sisesta ajavahemik:

Michael Jackson - Thriller

###
Näide programmi tööst
>> Sisesta faili nimi: vinüülid.txt
>> Sisesta žanr:
>> Sisesta ajavahemik:

The Beatles - Let It Be
Michael Jackson - Thriller
Queen - A Night at the Opera
'''


def loe_fail(faili_nimi):
    with open(faili_nimi, encoding="utf-8") as f:
        for rida in f:
            if rida.strip():
                yield [osa.strip() for osa in rida.split(",")]


def kysi_kasutaja_sisend(kysimus):
    return input(f"{kysimus}: ")


def tingimuste_kontroll(kogumik, kasutaja_zanr=None, kasutaja_aasta=None):
    lst = []
    for pealkiri, zanr, aasta in kogumik:
        if zanr.lower() == kasutaja_zanr.lower():
            lst.append((pealkiri, zanr, aasta))
        if aasta == kasutaja_aasta:
            lst.append((pealkiri, zanr, aasta))

    return lst


def naita_kasutajale(kogumik):
    print(kogumik)


kogumik = loe_fail("kogumik.txt")
zanr = kysi_kasutaja_sisend("Mis žanri otsid?")
aasta = kysi_kasutaja_sisend("Mis aastat otsid?")
filtreeritud_kogumik = tingimuste_kontroll(kogumik, zanr, aasta)
naita_kasutajale(filtreeritud_kogumik)