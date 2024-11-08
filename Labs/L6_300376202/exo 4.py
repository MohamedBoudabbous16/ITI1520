#Mohamed Boudabbous
#300376202
#exo4
def compte(s,c):
    L=s.count(c)
    return L
 

def compte_2(s,c):
    i=0
    n=0
    
    if len(c)==1:
        while i<len(s):
        
            if s[i]==c:
                n+=1
            i+=1
            if i==len(s):
                break
    elif len(c)>1:
        for i in range (len(s)):
            if s[i:(len(s)-1)]==c:
                n+=1
            i+=len(c)
            if i>len(s):
                break
    return n
s=str(input('Entrez une chaine de caractére: '))
print(compte(s,'de la'))
print(compte(s,'a'))
print(compte_2(s,'de la'))
print(compte_2(s,'a'))
