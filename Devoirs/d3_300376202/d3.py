#Mohamed Boudabbous
#300376202
#d3

#exo1


def compte100(l):
    """
   prend  une liste de nombres et retourne
   le nombre d'éléments supérieurs a 100 trouvés dans la liste
    list->int
    """
    somme = 0
    for n in l:
        if n > 100:
            somme += 1
    return somme
print(compte100([1,102,-3.5, 104]))

print(compte100([1,99,-3.5,-7]))

print(compte100([]))

#exo2
def sommeListeDiv2(l):
    """
    prend une liste de nombres et retourne un entier qui représenete
    ola somme des éléments de la liste qui se diviseent par 2 
    list->int
    """
    somme = 0
    for n in l:
        if n % 2 == 0:
            somme += n
    return somme
print(sommeListeDiv2([1,4,3,8,5]))

print(sommeListeDiv2([]))
print(sommeListeDiv2([4,-10,7]))

sommeListeDiv2([4,-10,7])

#exo3
def triples(chaine):
    """
    prend en paramétre une chaine de caractères
    et retourne True 'il y a au moins
    une séquence de 3 caractères consécutifs égaux, False sinon
    str->bool
    """
    if len(chaine) < 3:
        return False
       
    for n in range(len(chaine) - 2):
        if chaine[n] == chaine[n+1] == chaine[n+2]:
            return True
    else:
        return False
      

print(triples("abc"))

print(triples("abbbcdeeggggg"))

print(triples("abc2eee"))

print(triples("a23xxxxx"))

print(triples("abaacd"))
#exo4
def momo(chaine=str):
    """
    prend en paramétre une  chaine de caractères à transformer
    et retourne une nouvelle chaine de caractères qui contient
    les caractères de la chaine donnée une fois chacun
    en même ordre, et avec leur nombre de répétitions
    str->str
    """
    
    if len(chaine) == 0:
        return ""
        
    else:
        resultat = chaine[0]
        compteur = 1
        for n in range(1, len(chaine)):
            if chaine[n] == chaine[n-1]:
                compteur += 1
            else:
                resultat += str(compteur) + chaine[n]
                compteur = 1
        resultat += str(compteur)
        return resultat
print(momo("a"))

print(momo("aabbbccccx"))

print(momo("aaa1111"))

print(momo("aaabcaax"))
print(momo(""))

#exo5
def noDup(l=str):
    """
    Prend en paramétre une chaine de caractères à transformer et retourne la nouvelle chaine de caractères
    qui contient les caractères de la chaine donnée une fois chacun
    (sans répétitions des caractères consécutifs), en même ordre, sans répétitions
    str->str
    """
    c=""
    for n in l:
        if c=="" :
            c+=n
        else:
            if n!=c[-1]:
                c+=n
    return c

print(noDup("a"))
print(noDup("aabbbccccx"))
print(noDup("aaa1111"))
print(noDup("aaabcaax"))


