def kontrollitav(vanuse_kontroll):
    vanused = {14: "süüdiv",
               16: "KOV",
               18: ["RK", "EP", "ÕLU"],
               21: "kasiino",
               24: "A-kat",
               40: "President"
               }
    for vanus_nimekirjast in vanused.keys():
        if vanuse_kontroll >= vanus_nimekirjast:
            print(vanused[vanus_nimekirjast])
    
nimi = input("Mis su nimi on?")
sünniaasta = int(input("Mis su sünniaasta on?"))
vanus = 2026 - sünniaasta

kontrollitav(vanus)