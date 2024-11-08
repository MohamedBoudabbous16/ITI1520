#Mohamed Boudabbous
#300376202
#devoir2
#Exerice 1:
def patinage(epaisseur,temp):
    """
    (float,float->bool)
    temperature en  °C et epaisseur en cm
    cette fonction prend l'epaisseur de la couche de glace en cm et la température
    moyenne dans les derniers 10 jour, et si les conditions de patinage sont satisfait:
    epaisseur d’au moins 30 cm de la coouche de galce et  température moyenne d'au moins -10°C des derniers 10 jours
    pensdant les 10 derniers jours alors elle affiche True, si non elle affiche False 
    """
    if (epaisseur>=30 and temp<=-10):
        return True
        print ('True')
    else:
        return False
        print ('False')


#Exercice 2:
def alphaNote(n):
    """
    (float->string)
    prend une valeur numérique (note) comme
    entrée et retourne une note alphabétique sous forme de chaine de
    caractéres (string)
    """
    if (n>=90 and n<=100):
        print('A+')
    elif (n>=85 and n<=89):
        print ('A')
    elif (n>=80 and n<=84):
        print ('A-')
    elif (n>=75 and n<=79):
        print ('B+')
    elif (n>=70 and n<=74):
        print ('B')
    elif (n>=65 and n<=69):
        print ('C+')
    elif (n>=60 and n<=64):
        print ('C')
    elif (n>=55 and n<=59):
        print ('D+')
    elif (n>=50 and n<=54):
        print ('D')
    elif (n>=40 and n<=49):
        print ('E')
    elif (n>=0 and n<=39):
        print ('F')

#Exercice 3:
def alphaNoteVerif():
    """
    (None->None)
    Vérifie la validité d'une note nulérique en faissant appel à la
    fonction alphaNote()
    """
    n=float(input('Entrez la note finale numérique (de 0 à 100 avec 0 et 100 inclus): '))
    while (n>100 or n<0):
        n=float(input('Entrez la note finale numérique (de 0 à 100 avec 0 et 100 inclus): '))     
    if (n>=0 and n<=100):
        alphaNote (n)
        if n<50:
            print('Echoue')
        else:
            print('Reussi')
#Exercice 4:
def boucles(n):
    """
    (int->None)
    au début elle imprime chaque deuxieme valeur,
    de 1 à n (pour les nombres paires, n n’est pas inclus)
    et après ça de n à 1 (pour lesnombres paires, 1 n’est pas inclus).
    """
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 2
    print()
    
    if n % 2 == 0:
        i = n
    else:
        i = n 

    while i >= 1:
        print(i, end=" ")
        i -= 2
    print()

#Exercice 5:
def facteursDeN(n):
    """
    (int->bool)
    Imprime tous les facteurs de sauf 1 et n et imprime la somme de ces facteurs.
    
     n est Un entier positif (normalement)
    
    renvoie True si la somme des facteurs est inférieure à n, False sinon.
     bool
    """
    F=[]
    S=0
    for l in range(2,n):
        if n%l == 0:
            F.append(l)
            S=S+l
    print ('Facteurs de ',n,'=',F,'\n','Somme des Facteurs = ', S)
    if S<n:
        print (True)
        return True
    else:
        print(False)
        return False
        

#Exercice 6:
import math
def carreParfait(x):
    """
    (int->bool)
    Vérifie si x est un carré parfait et affiche sa racine carré si c'est le cas
    
    x: est de type entier.
    retorne True si x est un carré parfait, False sinon.
    """
    while x<0:
        x= int (input ('Entrez un entier positif: '))
    if (x>=0):
        y=math.isqrt(x)
        if y*y==x:
            print (x," est un carré parfait et ",y,"est sa racine carré")
            print (True)
            return True
           
        else:
            print (x," n'est pas un carré parfait")
            print(False)
            return False

#Exercice 7:
def maFun1(n):
    """
     (int)->float
     le clavier lit un nombre, si il est positif ou nul, l'interpréteur
     python calcule le résultat et l'affiche, et retourne res
     sinon il demande de réentrer une valeur positve ou nulle
    """
    
    while(n<0):
        n=int(input('Entrez un entier naturel positif: '))
    if n>=0:
        res=((-1)**n)/((2*n)+1)
        print(res)
        
      
#Exercice 8:


def maFun_bis(n):
  """
  (int->float)
  entre un nombre et calcule la somme des séries de Leibniz pour ce nombre.
  """
  c = 0
  for i in range(n):
    c += ((-1)**n)/((2*n)+1)
  c *= 4
  print(c)
  return c
  
print(patinage(30, -10))
print(patinage(25.4, -15))
print(patinage(33, -15))
print(patinage(35, -5))


alphaNote(100)
alphaNote(89)
alphaNote(56)
alphaNote(30)

alphaNoteVerif()
alphaNoteVerif()

boucles (13)
boucles (10)

facteursDeN(12)
facteursDeN(9)
facteursDeN(5)

carreParfait(16)
carreParfait(15)

maFun1(0)
maFun1(1)
maFun1(10)
maFun1(2)

maFun_bis(10)
maFun_bis(100)
maFun_bis(1000)
maFun_bis(10000)

   
   













        
        
        
