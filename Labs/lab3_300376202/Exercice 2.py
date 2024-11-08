#Moahmed Boudabbous
#300376202
#exercice 2

temp=float(input('Entrez la température:'))
activ_num=0
if temp >= 80.0:
    activ_num=1
elif (temp < 80.0 and 60.0 <= temp):
    activ_num=2
elif (temp <60 and temp>= 40):
    activ_num=3
elif (temp <40):
    activ_num=4

if activ_num==1:
    print ('Natation')
if activ_num==2:
    print ('Soccer')
if activ_num==3:
    print ('Volleyball')
if activ_num==4:
    print('Ski')



