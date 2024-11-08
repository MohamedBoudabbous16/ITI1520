#Mohamed Boudabbous
#300376202
#exo5

def espaces(s):
    if len(s) < 2:
        return s
    else:
        result = s[0]
        for i in range(1, len(s)):
            result += ' ' + s[i]
        return result


chaine = 'important'
resultat = espaces(chaine)
print(resultat)
