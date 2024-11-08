#Mohamed Boudabbous
#300376202
#exo1

def histo():
    l=str(input('Entrez une chaine de caractére : '))
    global d
    d={}
    for c in l:
        d[c]=d.get(c,0)+1
    #d_tries=d.items()
    print(d)
    return(d)
histo()
#programme principal:
d_tries=list(d.items())
d_tries.sort()
print(d_tries)
