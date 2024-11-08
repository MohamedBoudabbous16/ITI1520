#Mohamed Boudabbous
#300376202
#exo2
def histo_n(x):
    global d
    d={}
    for c in x:
        d[c]=d.get(c,0)+1
    print(d)
    return(d)

t = (1,2,-3,3,4,-3,3,3)
histo_n(t)
#programme principal:
d_tries=list(d.items())
d_tries.sort()
print(d_tries)
