#Moahmed Boudabbous
#300376202
#exercice 4
a=float(input('Entrez le premier coeff: '))
b= float(input('Entrez le deuxiéme coeff: '))
c= float(input('Entez le 3eme coeff: '))
delta= (b*b)-4*a*c
rac_delta=delta**(1/2)
if delta==0:
    x1=(-b)/(2*a)
    print("l'équation a une seule solution: ", x1)
elif delta>0:
    x1=(-b+(rac_delta))/(2*a)
    x2=(-b-(rac_delta))/(2*a)
    print("l'équation a 2 solutions: ", x1,'et ', x2 )
elif delta<0:
    print("l'équation n'a pas de solutions")
""""
voilà ce que m'a donne le programme
Entrez le premier coeff: 1.23456789
Entrez le deuxiéme coeff: 2.4691356
Entez le 3eme coeff: 1.23456789
l'équation n'a pas de solutions

===== RESTART: C:/Users/bouda/OneDrive/Desktop/ITI 1520/lab 3/Exercice 4.py ====
Entrez le premier coeff: 5
Entrez le deuxiéme coeff: 6
Entez le 3eme coeff: 7
l'équation n'a pas de solutions

===== RESTART: C:/Users/bouda/OneDrive/Desktop/ITI 1520/lab 3/Exercice 4.py ====
Entrez le premier coeff: 1
Entrez le deuxiéme coeff: 2
Entez le 3eme coeff: 1
l'équation a une seule solution:  -1.0

===== RESTART: C:/Users/bouda/OneDrive/Desktop/ITI 1520/lab 3/Exercice 4.py ====
Entrez le premier coeff: 1
Entrez le deuxiéme coeff: 5
Entez le 3eme coeff: 1
l'équation a 2 solutions:  -0.20871215252208009 et  -4.7912878474779195




mon programme ne donne pas la bonne réponse pour le premier essai probablement à
cause des chiffres aprées la virgule, pendant les calculs python ne pourra plus les compter exactement
cependant il semble correcte pour des entiers.
""""
    

