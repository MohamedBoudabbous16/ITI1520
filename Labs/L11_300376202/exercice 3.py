#Mohamed Boudabbous
#300376202
#exercice 3

def pgcd(x, y):
    if x < y:
        return pgcd(y, x)
    if x % y == 0:
        return y
    
    return pgcd(y, x % y)

#programme principal:
print(pgcd(1234,4321))
print(pgcd(8192,192))
