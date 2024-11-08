#Mohamed Boudabbous
#300376202
#exercice 3
class CompteBancaire:
    def __init__(self, nom='Dupont', solde = 1000):
        self.nom=nom
        self.solde=solde
    
    def depot(self, somme):
        self.solde+=somme
    def retrait(self, somme):
        self.solde-=somme
    def affiche(self):
        print(f"Le solde du compte bancaire de {self.nom} est de {self.solde} dollars")
    def __repr__(self):
        return f"CompteBancaire({self.nom}, {self.solde})"
    
    def __eq__(self, other):
        return (self.nom == other.nom and 
                self.solde == other.solde)    
        
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()

class CompteEpargne(CompteBancaire):
    def __init__(self, nom, solde, taux=0.003):
        super().__init__(nom, solde)
        self.taux = taux
    def changeTaux(self, nouveauTaux):
        self.taux = nouveauTaux
    def capitalisation(self, nombreMois):
        ancien_solde = self.solde
        interets = ancien_solde * (1+self.taux)**nombreMois
        self.solde = interets
        print(f"Capitalisation sur {nombreMois} mois au taux mensuel de {self.taux*100} %.")
        return self.solde

c1 = CompteEpargne('Duvivier', 600)
c1.depot(350)
c1.affiche()
c1.capitalisation(12)
c1.affiche()
c1.changeTaux(0.005)
c1.capitalisation(12)
c1.affiche()
