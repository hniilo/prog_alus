def pyramiid_reverse(korgus, symbol):
    pyr_asc = []
    for i in range(korgus):
        pyr_asc.append((korgus - i-1)* " " + (i * 2 + 1) * symbol + (korgus - i-1)* " ")
    
    for el in reversed(pyr_asc):
        print(el)


def pyramiid(korgus, sumbol):
    pyr = []
    for i in range(korgus):
        pyr.append((korgus - i-1)* " " + (i * 2 + 1) * sumbol + (korgus - i-1)* " ")
    return pyr

pyr_asc = pyramiid(7, '*')
pyr_len = len(pyr_asc)
for el in range(pyr_len):
    print(pyr_asc[el] + "|" + pyr_asc[-el-1] + "|" + pyr_asc[el])
                
                
                
                
                
                
                
                