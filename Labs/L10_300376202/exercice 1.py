#Mohamed Boudabbous
#300376202
#exercice 1
class Temps:
  '''classe temporelle'''

  def __init__(self, h=12, m=0, s=0):
    '''(Temps)-> None'''
    self.setTemps(h, m, s)

    
  def setTemps(self, h, m=0, s=0):
    '''(Temps)-> None'''
  
    if h < 0 or h > 23:
      h = 0
    if m < 0 or m > 59:  
      m = 0
    if s < 0 or s > 59:
      s = 0
  
    self.heure = h
    self.minute = m 
    self.seconde = s


  def affiche_heure(self):
    '''(Temps)-> None'''
    print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde)) 

  def __repr__(self):
    '''(Temps)-> str'''
    return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

  def __eq__(self, autre):
    '''(Temps)-> bool'''
    return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde
  
  def estAvant(self, autre):
    if self.heure<autre.heure:
      return True
    elif self.heure==autre.heure and self.minute<autre.minute:
      return True
    elif self.heure==autre.heure and self.minute<autre.minute:
      return True
    elif self.heure==autre.heure and self.minute==autre.minute and self.secondes<autre.minute:
      return True
    else:
      return False
  def durée(self, autre):
    h=abs(self.heure-autre.heure)
    m=abs(self.minute-autre.minute)
    s=abs(self.seconde-autre.seconde)
    return Temps(h, m, s)

t1 = Temps(12,4,0)
t2 = Temps(10,2,1)
print(t1.estAvant(t2))
print(t2.estAvant(t1))
t2.setTemps(12,45,2)
print(t1.estAvant(t2))
print(t1.durée(t2))

      
