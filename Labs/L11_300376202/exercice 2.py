#Mohamed Boudabbous
#300376202
#exercice 2
def créer_rec(A, n):
    if n == 0:
        return
    
    A.append(n-1)
    créer_rec(A, n-1)
    
#programme principal:

L=[]
n = int(input("Entrez la valeur de n : "))
créer_rec(L, n)
print(L)
