#Mohamed Boudabbous
#300376202
#exercice 3
def cherche_r(l,v):
    nPas=0
    occurence=0
    for n in l:
        for i in n:
            nPas+=1
            if i ==v:
                occurence+=1
    print('Nombre de pas ',nPas)
    return occurence
M = [[1,2,10],[7,5,6], [8,8,9,10]]
print(cherche_r(M,10))
