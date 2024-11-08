#Mohamed Boudabbous
#300376202
#exo6
def coder(s):
    if len(s) < 2:
        return s
    else:
        result = ''
        i = 0
        while i < len(s) - 1:
            result += s[i + 1] + s[i]
            i += 2
        if i < len(s):
            result += s[i]
        return result


chaine1 = 'message secret'
resultat1 = coder(chaine1)
print(resultat1)

chaine2 = 'Message'
resultat2 = coder(chaine2)
print(resultat2)
