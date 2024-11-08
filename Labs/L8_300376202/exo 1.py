#Mohamed Boudabbous
#300376202
#exo 1

print("Entrez les nombres avec des espaces entre les colonnes.")
print("Une rangee par ligne, et une ligne vide a la fin.")
matrice = []
while True:
  ligne = input()
  if not ligne:
    break
  valeurs = ligne.split()
  rangee = [int(val) for val in valeurs]
  matrice.append(rangee)

def transp(m):
  lignes= len(m)
  colonnes=len(m[0])
  MT=[]
  
  for j in range(colonnes):
    r=[]
    for i in range(lignes):
      r.append(m[i][j])
    MT.append(r)
  return MT

print(transp(matrice))
