# Teadmiste kontroll - aritmeetika, listid, sõned, tingimuslaused, sõnastikud
# Igas ülesandes on funktsiooni toorik. Kirjuta implementatsioon ja käivita fail,
# et kontrollida, kas väljund vastab kommentaaris olevale oodatavale tulemusele.


# ===== Listid, sõned ja sõnastikud =====


# 1. Pesastatud listide ühendamine for-tsükliga
def zip_lists_with_for_loop(par):
    ret = []
    for el_v in nested_lists:
        for el_s in el_v:
            ret.append(el_s)
    return ret

def zip_lists_with_for_loop_extend(par):
    ret = []
    for el_v in nested_lists:
       ret.extend(el_v)
    return ret


nested_lists = [[1, 2, 3], [4, 5, 6]]
print(zip_lists_with_for_loop(nested_lists))  # expected output: [1, 2, 3, 4, 5, 6]
print(zip_lists_with_for_loop_extend(nested_lists))  # expected output: [1, 2, 3, 4, 5, 6]


# 2. Paarisarvud listist
# Tagasta uus list, kuhu kuuluvad ainult paarisarvud (jääk 2-ga jagamisel on 0).
def paarisarvud(arvud):
    # Kirjuta siia implementatsioon
    return


# print(paarisarvud([9, 8, 7, 1, 2, 3, 4, 5, 6]))  # expected output: [8, 2, 4, 6]


# 3. Suurim arv listist (ilma max() funktsioonita)
# Käi list for-tsükliga läbi ja leia suurim element.
def suurim(arvud):
    # Kirjuta siia implementatsioon
    return


# print(suurim([3, 17, -5, 9, 12]))  # expected output: 17


# 4. Täishäälikute loendamine sõnes
# Loenda, mitu täishäälikut (a, e, i, o, u, õ, ä, ö, ü) sõnes on. Suur- ja väiketähti kohtle ühtemoodi.
def taishaalikud(sone):
    # Kirjuta siia implementatsioon
    return


# print(taishaalikud("Kalevipoeg"))  # expected output: 5
# print(taishaalikud("Õnnelik Üliõpilane"))  # expected output: 9


# 5. Sõnade esinemiste loendamine sõnastikku
# Tagasta sõnastik, kus võti on sõna ja väärtus on selle sõna esinemiste arv listis.
def loenda_sonad(sonad):
    # Kirjuta siia implementatsioon
    return


# print(loenda_sonad(["õun", "pirn", "õun", "banaan", "õun", "pirn"]))
# expected output: {'õun': 3, 'pirn': 2, 'banaan': 1}
