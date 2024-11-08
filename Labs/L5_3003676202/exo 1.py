#Mohamed Boudabbous
#300376202
#exo 1

L1= []
# Demander à l'utilisateur d'entrer des valeurs 
print("Entrez des valeurs, ou 'fin de la liste' pour terminer:")

while True:
  n = input("Entrez, un chiffre, une fois liste compléte entrez fin de la liste: ")
  if n == 'fin de la liste':
    break
  L1.append(float(n))

print("La Liste L1 est:", L1)
def moyenne():
    somme = 0
    compteur = 0

    for element in L1:
        somme += element
        compteur += 1

    moyenne = somme / compteur
    print('La moyenne des elements de la liste est: ', moyenne)
    return moyenne


moyenne()

