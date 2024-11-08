#Mohamed Boudabbous
#300376202
#exercice 1
def nub_rec(A,n):
    if n == 0:
        return True
    
    if not isinstance(A[n-1], int):
        return False
    
    if not (0 <= A[n-1] <= 9):
        return False
    
    return nub_rec(A,n-1)
#programme prioncipal
A = [1, 2, 3, 4, 5] 
N = len(A)

if nub_rec(A, N):
  print("Tous les éléments sont des chiffres de 0 à 9")
else:
  print("Il y a des éléments qui ne sont pas des chiffres de 0 à 9")
  
B = ['m', 2, 3, 4, 5]
C = len(B)

if nub_rec(B, C):
  print("Tous les éléments sont des chiffres de 0 à 9")
else:
  print("Il y a des éléments qui ne sont pas des chiffres de 0 à 9")

R = [11, 2, 3, 4, 5]
V = len(R)

if nub_rec(R, V):
  print("Tous les éléments sont des chiffres de 0 à 9")
else:
  print("Il y a des éléments qui ne sont pas des chiffres de 0 à 9")
