#Moahmed Boudabbous
#300376202
#exercice 3
compteur=0
def est_Divisible(n):
    if (n%2==0 and n%3==0):
        compteur=1
    elif (n%2==0 or n%3==0):
        compteur=2
    else:
        compteur =0
    if compteur==1:
        print(n, 'est divisible par 2 et par 3')
    elif compteur==2:
        print(n, 'est divisible par 2 ou par 3')
    elif compteur== 0:
        print(n, 'pas divisible ni par 2 ni par 3')
    



entier= int(input("Entrez un entier Svp"))
est_Divisible(entier)


