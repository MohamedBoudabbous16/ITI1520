#Mohamed Boudabbous   #Salim Mohamed ALLAL
#300376202            #300369621
#Question 1:
def triangle(n):
    if n == 0:
        return
    triangle(n-1)
    print("*" * n)
#Question 2:
def etoiles(n):
    if n == 0:
        return
    print("*" * n)
    if n>1:   
        etoiles(n-1)
        print("*" * n)
#Question 3:
def prodListePos_rec(lst, n):
    if n == 0:
        return 1
    elif lst[n-1] > 0:
        return lst[n-1] * prodListePos_rec(lst, n-1)
    else:
        return prodListePos_rec(lst, n-1)

def prodLRec1(lst):
    if len(lst) == 0:
        return 1
    elif lst[0] > 0: 
        return lst[0] * prodLRec1(lst[1:])  
    else:
        return prodLRec1(lst[1:])
