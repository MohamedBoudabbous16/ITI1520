﻿#Mohamed Boudabbous
#300376202
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str)-> tuple of (list of str,list of str)
    Retournes deux listes qui représentent les deux mains des cartes.
    Le donneur donne une carte à l'autre joueur, une à lui-même, et ça continue jusqu'à la fin du paquet p.
    '''
    donneur=[]
    autre=[]
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    for n in range(len(p)):
        if n%2==0:
            autre.append(p[n])
        else:
            if n%2!=0:
                donneur.append(p[n])
    return (donneur, autre)

    # AJOUTEZ VOTRE CODE ICI
    

def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    resultat=[]
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    
    m=sorted(l)
   
    for n in m:
        if not resultat or not (n.startswith(resultat[-1][:-1])):
            resultat.append(n)
        else:
            resultat.pop()
    # AJOUTEZ VOTRE CODE ICI
   
        
    random.shuffle(resultat)
    return resultat
            
    


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    for carte in p:
        print(carte, end=' ')
    print()

    


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
def entrez_position_valide(n):
    '''
    (int)->int
    Retourne un entier du clavier, de 1 à n (1 et n inclus).
    Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
    
    Précondition: n >= 1
    '''
    c =0
    
    while c < 1 or c > n:
        c = int(input("Entrez un entier entre 1 et " + str(n) + ": "))
    return c


def joue():

    '''()->None
    Cette fonction joue le jeu'''
    
    p=prepare_paquet()
    melange_paquet(p)
    tmp=donne_cartes(p)
    donneur=tmp[0]
    humain=tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main est:")
    print(affiche_cartes(humain))
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    donneur=elimine_paires(donneur)
    humain=elimine_paires(humain)

    
    compteur = 1

    
    while len(donneur) > 0 and len(humain) > 0:
        
        
        if compteur % 2 == 0:
            print("***********************************************************\nMon tour.")
            
            
            index = random.randint(0,len(humain)-1)
            carte = humain.pop(index)
            nomb_choisis = index+1
            print("J'ai pris votre",nomb_choisis,"ème carte.")
            
           
            donneur.append(carte)
            
            
            donneur = elimine_paires(donneur)
            
            
            compteur += 1
            attend_le_joueur()
            
         
        else:
            
            print("***********************************************************\nVotre tour.")
            
            print("Votre main est :")
            print(affiche_cartes(humain))
            
            print("j'ai",len(donneur),"cartes. Si 1 est la position de ma première carte et",len(donneur),"la position de ma derinère carte, laquelle de mes cartes voulez-vous? ")
            
           
            index = entrez_position_valide(len(donneur)) - 1
            
            
            carte = donneur.pop(index)
            n_choisis = index+1
            
            print("vous avez demander la",n_choisis,"ème carte")
            print("La voilà : c'est un",carte)
            
            
            humain.append(carte)
            
            print("Avec",carte," ajouté, votre main est:")
            print(affiche_cartes(humain))
            
           
            humain = elimine_paires(humain)

            print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
            print(affiche_cartes(humain))
            
            
            compteur += 1
            attend_le_joueur()

    
    if len(humain) == 0:
        print( "Tu as terminé toutes les cartes \n J'ai perdu! Vous, humain, vous avez gagné.")
    else:
        if len(donneur) == 0:
            print("J'ai terminé toutes les cartes \n Vous avez perdu! Moi, Robot, j'ai gagné.")
        
joue()


     
    

	 


