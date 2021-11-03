from mes import Mes
import random

nombremeses=["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE","NOVIEMBRE", "DICIEMBRE",  ]
meses=[]

for i in range(0, 11):
    mimes=Mes()
    mimes.mesNom= nombremeses[i]
    mimes.temMax=random.randint(20,35)
    mimes.temMin=random.randint(5,20)
    meses.append(mimes)
    
print("Meses creados " + str(len(meses)))


for mes in meses:
    print(mes)