#Mohamed Boudabbous
#300376202
#exercice4
def factoriel():
    n=int(input('Entrez un nobre positif'))
    if n == 0:
        print(1)
    if n<0:
        print('erreur')
    else:
        F = 1
        for k in range(1,n+1):
            F = F*k
        print(F)
factoriel()
   
