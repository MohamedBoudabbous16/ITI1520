#Mohamed Boudabbous
#300376202
#exo3
def somme_de_trois(x):
    if len(x)<3:
        raise ValueError("Le tuple doit avoir au moins 3 éléments")

    for i in range (len(x)-2):
        if x[i]+x[i+1]+x[i+2]==0:
            return True
t = (1,2,-3,4,-1,3)
print(somme_de_trois(t))
