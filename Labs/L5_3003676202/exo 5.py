#Mohamed Boudabbous
#300376202
#exo 4
import math

def ecart_type(x):
  
  moyenne = sum(x) / len(x)
  
  s_eca_car = 0
  for xi in x:
    ei = xi - moyenne
    s_eca_car += ei**2

  var = s_eca_car/ (len(x) - 1)  

  ecart_type = math.sqrt(var)

  return ecart_type
notes = []
note = float(input("Note : "))
while note != 1000:
  notes.append(note)
  note = float(input("Note : "))

print("Ecart-type :", ecart_type(notes))
