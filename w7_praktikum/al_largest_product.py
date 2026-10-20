def str_list_product(sisend_str_list):
    korrutis = 1
    for str_number in sisend_str_list:
        korrutis *= int(str_number)
    return korrutis


def largest_product(serie, n=4):
    korrutiste_list = []
    arv_str = str(serie)
    for str_number in range(len(arv_str)):
        # Lõikame meid huvitava n-kohalise stringi jupi välja suurest stringist.
        n_kohaline_string = arv_str[str_number:str_number + n]

        # Kontrollime, et lõigatud alamstring on alati n-koha suurune.
        # Erijuhtum on suure stringi lõpus lõikamisega
        if len(n_kohaline_string) == n:
            # Kutsume abifunktsiooni välja, mis muudab lühikese stringi
            # kõik elemendid int-tüüpi ja siis leiab nende korrutise.
            # Abifuntsioon tagastab stringi elementide korrutise ja see
            # lisatakse korrutiste_list'i järjendisse
            korrutiste_list.append(str_list_product(n_kohaline_string))
    # LEIA ja TAGASTA maksimum väärtus korrutiste_list'i elementidest
    return max(korrutiste_list)


from_project_euler = int(
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

print(largest_product(from_project_euler, 4))
assert largest_product(from_project_euler, 4) == 5832
