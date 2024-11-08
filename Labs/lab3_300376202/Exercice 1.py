#Moahmed Boudabbous
#300376202
#exercice 1
age= int(input("veuillez tapez votre age svp: "))

age_acceptee = age>=18 and age<=55
if age_acceptee:
    print("transaction acceptée")
else:
    print("transaction refusée")
    
