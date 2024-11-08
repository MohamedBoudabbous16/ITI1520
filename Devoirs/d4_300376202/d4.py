#Mohamed Boudabbous   #Salim Mohamed ALLAL
#300376202            #300369621
#devoir4
#exercice 1
def transl(d,s): #dict,string ----> string
    #prends comme entrée un dictionnaire Python d et une chaîne de caractères s, et retourne la chaîne de caractères correspondant à la clé ou à la valeur de s.
    #si s n'est pas une clé ou une valeur de d, retourne "Unknown"
    if s in d.keys():
        return d[s]
    
    elif s in d.values():
        for c, v in d.items():
            if v==s:
                return c
    else:
        r="Unknown"
        return r

d = {"apple":"pomme", "banana":"banane", "pear": "poire", "plum":"prune"}

#exercice 2
def setOp(l,v):  #list,list ----> set
    #prends comme entrée deux listes de chaînes de caractères l et v et fait la somme des deux listes en retournant un set.
    l1=set()
    for i in l:
        if i not in l1:
            l1.add(i)
    
    for i in v:
        if i not in l1:
            l1.add(i)
    return l1

#exercice 3:
def matrixMinMax(m):     #list ----> tuple
    #prends comme entrée une liste de listes de nombres m et retourne un tuple contenant les valeurs minimale et maximale de m.
    minimum = m[0][0]
    maximum = m[0][0]
    for i in  m:
        for n in i:
            if n < minimum:
                minimum=n
            if n>maximum:
                maximum=n
    r=(minimum,maximum)
    return r
            








    
