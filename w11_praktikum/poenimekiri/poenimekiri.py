'''
Toakaaslased kohtusid poes, neil oli ühine ostunimekiri ja kummalgi oli korvis osa ostunimekirjas olevatest esemetest.
Et teada saada, mida veel vaja on, panevad nad korvid kokku.


Failide vorming
Iga fail on tekstifail (UTF-8), kus on üks ese rea kohta. Samad esemed ei kordu.

Tühje ridu ja ridade alguses/lõpus olevaid tühikuid ei arvestata.
Tähesuurust eristatakse (Piim ja piim on erinevad esemed).


Funktsioonid:
loe_nimekiri(failinimi) – loeb failist esemed ja tagastab nende esemete hulga.
leia_puuduvad(nimekiri, ostukorv1, ostukorv2) – tagastab sellise esemete hulga, mis on nimekirjas, aga pole kummaski korvis.
leia_korduvad(nimekiri, ostukorv1, ostukorv2) – tagastab selliste esemete hulga, mis on nimekirjas ja on mõlemas korvis.
Mõtle, milliseid hulgaoperatsioone (&, |, -) saaks kasutada.

Programm küsib kolm failinime, loeb failid ja väljastab täpselt kaks rida:

Sisesta ostunimekirja faili nimi: nimekiri.txt
Sisesta esimese toakaaslase ostukorvi faili nimi: ostukorv1.txt
Sisesta teise toakaaslase ostukorvi faili nimi: ostukorv2.txt
Mõlemas korvis puuduvad esemed nimekirjast on {'Õli', 'Jahu', 'Suhkur'}
Mõlemas korvis on olemas nimekirjast {'Munad'}
Hulga elementide järjekord ei pea olema sama mis näites. Kui programmi töö käigus väljastatav hulk on tühi, väljasta "{}" mitte "set()"

'''

def loe_nimekiri(faili_nimi):
    with open(faili_nimi, encoding="utf-8") as f:
        for rida in f:
            if rida.strip():
                yield rida.strip()

def lisa_hulka(hulk, nimekiri):
    for produkt in nimekiri:
        hulk.add(produkt)

jaagu_nimekiri = loe_nimekiri("jaak_nimekiri.txt")
koidu_ehalend_nimekiri = loe_nimekiri("koidu-ehalend.txt")

yhis_nimekiri = set()

lisa_hulka(yhis_nimekiri, jaagu_nimekiri)
lisa_hulka(yhis_nimekiri, koidu_ehalend_nimekiri)

print(yhis_nimekiri)

jaagu_set = set([el for el in loe_nimekiri("jaak_nimekiri.txt")])
koidu_ehalend_set = set([el for el in loe_nimekiri("koidu-ehalend.txt")])

print("ühend", jaagu_set.union(koidu_ehalend_set))
print("ühend", jaagu_set | koidu_ehalend_set)


print("ühisosa", jaagu_set.intersection(koidu_ehalend_set))
print("ühisosa", jaagu_set & koidu_ehalend_set)

print("vahe", jaagu_set.difference(koidu_ehalend_set))
print("vahe", jaagu_set - koidu_ehalend_set)