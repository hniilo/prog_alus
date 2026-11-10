'''
Juku otsustas osa võtta aialinnuvaatlusest ja läks tunniks ajaks õue.
Ta kirjutas nähtud lindude liikide ja arvude kaupa faili linnud.txt.
Igas reas on liik ja arv teineteisest eraldatud komaga.
Eeldame, et liigid mitmel real ei kordu.

tihane,7
varblane,5
rohevint,1
leevike,6
vares,2

Kirjuta funktsioon linnud_sõnastikku, mille argumendiks on failinimi ja mis tagastab sõnastiku, kus kirjete võtmeteks on linnunimed ja väärtusteks lindude arvud.

Näiteks:
>> linnud_sõnastikku("linnud.txt")
{'tihane': 7, 'varblane': 5, 'rohevint': 1, 'leevike': 6, 'vares': 2}


Kirjuta programm, mis:
* küsib kasutajalt faili nime;
* loeb funktsiooni linnud_sõnastikku abil sellest failist andmed ja koostab sõnastiku;
* küsib kasutajalt arvu;
* väljastab eraldi ridadel kõik linnuliigid, keda Juku nägi rohkem kui näidatud arv kordi, ning nende arvud sulgudes;
* väljastab Juku nähtud lindude koguarvu.

Näiteks võib programmi väljund olla:
Sisesta failinimi: linnud.txt
Sisesta arv: 5
tihane (7)
leevike (6)
Juku nägi väljas 21 lindu.'''