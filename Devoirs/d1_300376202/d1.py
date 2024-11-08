#Mohamed Boudabbous
#300376202
#Exercice 1
def tempsVoyage(distance, vitesse):
    """
(float,floa)->float
donne au final le temps du voyage en minutes
    """
    print ('la distance est en Km et la vitesse est en km/h')
    temps=(distance/vitesse)*60
    print ('le voyage a duré', temps, 'minutes')
    return temps

tempsVoyage(400,100)
tempsVoyage(20.6,60)
#Exercice 2
def noteFinale(labos, devoirs, quiz, examenpartiel,examenfinal):
    """
(float,float,float,float,float)->float
Au final ce programme affiche la moyenne génerale
    """
    noteFinale=labos*0.1+devoirs*0.25+quiz*0.05+examenpartiel*0.2+examenfinal*0.4
    print ('la note finale de cet étudiant est de', noteFinale)
    return noteFinale


noteFinale(8,6,7,3,1)
noteFinale(9,5,8,3,4)
noteFinale(7,10,10,9,8)
noteFinale(5,5,3,2,1)

noteFinale(100,100,100,100,100)
noteFinale(50,90.5,60,80,70)
#Exercice 3
def bibformat(auteur, titre, ville, maisonEdition, annee):
    """
    (str,str,str,str,int)->str
    le résultat final est une chaine de caractére sous une forme spécifiée telque:
    'auteur (annee). titre. ville: maisonEdition'
    """
    variable =f"'{auteur} ({annee}). {titre}. {ville}: {maisonEdition}'"
    print ( variable)

bibformat("Antoine de Saint Exupery", "Le petit prince", "Paris", "Jeunesse", 1943)
#Exercice 4
def bibformat2(auteur, titre, ville, maisonEdition, annee):
    variable =f"{auteur} ({annee}). {titre}. {ville}: {maisonEdition}"
    print ( variable)
    return variable
def  bibformatPrint():
    """
()->string
recueille des données d'un livre pour les afficher sous forme d'une ligne
    """
    auteur= input("SVP entez l'auteur: ")
    titre= input("SVP entez le titre: ")
    ville= input("SVP entez la ville: ")
    maisonEdition= input("SVP entez la maison d'edition: ")
    annee= input("SVP entez l'annee de publication: ")
    bibformat2(auteur, titre, ville, maisonEdition, annee)
bibformatPrint()
#Exercice 5
from math import log10
def logFun(x):
    """
    résout l'équation suivante pour un x dejà fixé: 10**(4y)=x+3
    si x est un nombre strictement positif de type float, la fonction renvoie la valeur de y
    , c'est à dire la solution de l'équation
    sinon, ce programme affiche 'vous devez entrer un nombre strictement positif'
    (number)->number  puisqu'on peut entrer un chiffre sous expression scientifique....
    """
    if x>0:
        y = (log10(x + 3))/4
    else :
        print ('vous devez entrer un nombre strictement positif')
    print ('La solution de lequation pour x=', x, "est", y)
    return y
logFun(7)
logFun(20)
logFun(999999997)
logFun(0.1)
logFun(9997)
#Exercice 6
def anneeBis(an): # pour cette partie il faut copier ses lignes (anneeBis(1904)
#anneeBis(1928)
#anneeBis(1950)
#anneeBis(1990)
#anneeBis(1932)
#dans la console d'exécution
    """
(int)->bool
l'an doit etre supérieur à 1582
si année bisextile retourne true
si année pas bissextile retourne false
    """
    if (an%4 == 0 and not (an%100 == 0)):
        return True
        print (True)
    if an%400 == 0:
        return True
        print (True)
    else:
        return False
        print (False)
anneeBis(1904)
anneeBis(1928)
anneeBis(1950)
anneeBis(1990)
anneeBis(1932)



