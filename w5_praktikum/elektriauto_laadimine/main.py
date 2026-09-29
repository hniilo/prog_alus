
'''

- - - - - -
Lisa readme'sse:
1. Hinnajärgi optimeeritud elektriauto laadimisaegade leidmine
   1. seadmestiku defineerimine (auto, võrguühendus, tarbimisharjumused)
   2. hinnapäring
   3. andmetöötlus
      1. päringu tulemuse hinna järgi sorteerimine
      2. sobilike kellaaegade filtreerimine
         1. tarbmimisharjumustest sobilike kellaaegade filtreerimine
         2. laadimistüübi sõltuvus. Esialgu ainult üks laadimise viis)
- - - - - -

Alusta failist lugemisega ja siis liigu veebi päringute juurde. Lisa algandmete fail!

1. Uuri, kust saab päeva või tunni või 15 minuti elektrihinda pärida
    * API dokumentatsioon: https://dashboard.elering.ee/assets/swagger-ui/index.html
    * 'https://dashboard.elering.ee/api/nps/price?start=2020-05-31T20%3A59%3A59.999Z&end=2020-06-30T20%3A59%3A59.999Z'
    * 'https://dashboard.elering.ee/api/nps/price/EE/latest'
    * 'https://dashboard.elering.ee/api/nps/price/EE/current'
    * UTC tsoon

2. Mis moodi Pythonis veeb / api päringuid tehakse? Lisa koodi näide
3. Mis tüüpi objekt tagastatakse päringust?
    * mis atribuudid on objektil olemas?
4. Kuidas saada päringust andmed kätte?
5. Kuidas salvestada andmed faili?
6. Kuidas andmeid failist lugeda? Õiged tüübi teisendused
7. aja andmetüüp



x. Elektriauto laadimise optimeerimine eramaja näitel
    x.0 : Nädala kava laadimise kohta (abstraktsioon: sarnased vs erinevad päevad)
        * mis tundidel päevas autot saab laadida?
        * kuidas defineerida ja millist andmestruktuuri kasutada, et kirjeldada nädala ja tundide seosed?
        * mis hinnapiirist alates ei lubata laadida?
    x.2 : Mis laadimist on võimalik kasutada? tava- või kiirlaadimine?
        * peakaitsme suurus?
        * kogutarbe arvestamine (saun, pliit, ahi, soojuspump, elektriboiler)?
            ** millistel juhtudel on võimalik auto laadimine maksimaalse võimsusega?
    x.3 : Elektribörsi hindade päring ja andmetöötlus
        * API päring ja andmete salvestamine (muutuja, lokaalne fail arvutis, objekt)
            * Mis andmestruktuur?
        * Andmetöötlus:
            ** filtreeri saadaval olevad tunnid
            ** järjesta odavad tunnid

    x.4 : parendused
        * laadimine võiks toimuda hommiku tundidel enne sõitmist
            * külmal perioodil aku soojendamine võimaldab pikemat läbisõitu
        * võrgutasu arvestamine mudelis
'''