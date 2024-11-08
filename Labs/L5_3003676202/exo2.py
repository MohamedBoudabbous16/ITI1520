#Mohamed Boudabbous
#300376202
#exo 2

def statistiques(notes):
  moyenne = sum(notes) / len(notes)
  minimum = min(notes)
  maximum = max(notes)

  return [moyenne, minimum, maximum]


print("Veuillez saisir les notes des étudiants (1000 pour terminer) : ")

notes = []
note = float(input("Note : "))
while note != 1000:
  notes.append(note)
  note = float(input("Note : "))

resultats = statistiques(notes)

print("Moyenne :", resultats[0]) 
print("Minimum :", resultats[1])
print("Maximum :", resultats[2])
