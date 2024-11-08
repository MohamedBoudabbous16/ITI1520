#Mohamed Boudabbous
#300376202
#exercice 2
def cherche_m(l,v):
    nPas=0
    for n in l:
        for i in n:
            nPas+=1
            if i ==v:
                print('Nombre de pas ',nPas)
                return True
    print('Nombre de pas ',nPas)
    return False
M = [[1,2,10],[7,5,6], [8,8,9,10]]
print(cherche_m(M,5))
