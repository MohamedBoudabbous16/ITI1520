#Mohamed Boudabbous
#300376202
#exo3
s = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''


nS = s.replace('.',' ')
nS=nS.replace(',',' ')
nS=nS.replace(';',' ')
nS=nS.replace('\n',' ')

print (nS)
nS=nS.strip()
print (nS)
nS=nS.lower()
print (nS)
print(nS.count('de'))
nS=nS.replace('était','est')
print(nS)

