#Mohamed Boudabbous
#300376202
#exo 3
def produit_matrices(m,n):
    lignes_m=len(m)
    colonnes_n=len(n[0])
    P=[]
    for i in range(lignes_m):
        P.append([])
        for j in range(len(n[0])):
            P[i].append(0)
            for k in range (len(n)):
                P[i][j]+=m[i][k]*n[k][j]
    return P
m = produit_matrices([[1,2,3],[4,5,6]],[[1,2],[3,4],[5,6]])
print(m)
