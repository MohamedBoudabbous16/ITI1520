#Mohamed Boudabbous   #Salim Mohamed ALLAL
#300376202            #300369621
#devoir4
def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    for i in range(9):
        if grille[row][i] == num:
            return False
    return True

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    # A COMPLETER
    for i in range(9):
        if grille[i][col] == num:
            return False
    return True

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''

    # A COMPLETER
    r=(row//3)*3
    c=(col//3)*3
    for i in range(r,r+3):
        for j in range(c,c+3):
            if grille[i][j] == num:
                return False
            
    return True

def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''
    
   # A COMPLETER
    for row in grille:
       for cell in row:
           if cell == 0:
               return False
    return True
  
def verifierValide(grille, row, col, num):
   ''' (list, int, int, int) ->  bool
   * verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
   * Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
   '''
   
   # A COMPLETER
   r=verifierLigne(grille, row, num) and verifierCol(grille, col, num) and verifierSousGrille(grille, row, col, num) 
   return r
   

