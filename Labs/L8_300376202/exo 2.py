#Mohamed Boudabbous
#300376202
#exo 2
def somme_matrices(m,n):
    lignes=len(m)
    colonnes=len(m[0])
    T=[]
    for i in range(lignes):
        r=[]
        for j in range(colonnes):
            l=m[i][j]+n[i][j]
            r.append(l)
        T.append(r)
    return T

    
m=[[1,2],[3,4]]
n=[[1,1],[1,1]]
f=somme_matrices(m,n)
print(f)
