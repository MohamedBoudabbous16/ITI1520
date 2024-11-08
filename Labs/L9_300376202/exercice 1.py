#Mohamed Boudabbous
#300376202
#exercice 1
import random
def cherche(l,v):
    nPas=0
    for i in l:
        nPas+=1
        if i ==v:
            print('Nombre de pas ',nPas)
            return True
    print('Nombre de pas ',nPas)
    return False
N=100
l3=[]
for i in range (N):
    v= random.randrange(1,N+1)
    l3.append(v)
print(l3)

print(cherche(l3,78))    
    
