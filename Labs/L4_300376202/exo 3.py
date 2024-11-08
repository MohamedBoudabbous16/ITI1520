#Mohamed Boudabbous
#300376202
#exercice 3
import random
def devine():
    n=random.randint(1,10)
    compteur=0
    v=int(input('Entrez un nombre entre 1 et 10'))
    if v<n:
        print('n est plus grand')
    elif v>n:
        print('n est plus petit')
    while v != n:
        v=int(input('entrez un autre nombre'))
        compteur=compteur+1
        if v<n:
            print('n est plus grand')
        elif v>n:
            print('n est plus petit')
    
    else:
        if v==n:
            compteur=compteur+1
            print ('succées','vous avez réalisé', compteur, 'essais pour le trouver')
     

devine()
