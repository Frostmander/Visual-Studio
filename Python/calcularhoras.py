print("Calcular salario trabajadores")
print("Introduzca número de ohras trabajadas")
numerohoras = int(input())
print("Introduzca precio hora")
preciohora = int(input())
print("Introduzca número de kilometros")
kilometros = int(input())

#Debemos calcular las horas extra
#Salario base y el salario extra

horasextra = 0
salariobase = 0
salarioextra = 0
dietas = ""
retencion = ""

if (numerohoras > 36):
    horasextra = numerohoras - 36
    salariobase = preciohora * 36
    salarioextra = horasextra * (preciohora + 2)
else:
    horasextra = 0
    salarioextra = 0
    salariobase = numerohoras * preciohora

if (kilometros < 100):
    dietas = "Dieta local"
elif (kilometros >= 100 and kilometros <= 500):
    dietas = "Dietas nacional"
else:
    dieta = "Dieta internacional"

salariototal = salariobase + salarioextra 

if (salariototal <= 250):
    retencion = "No tiene retención"
elif (salariototal >= 251 and salariototal <= 800):
    retencion = "Retención 20%"
else:
    retencion = "Retención 40%"

print("Numero horas: " + str(numerohoras))
print("Precio hora: " + str(preciohora))
print("Kilometros: " + str(kilometros))
print("Horas extra: " + str(horasextra))
print("Salario extra: " + str(salarioextra))
print("Salario base: " + str(salariobase))
print("Salario total: " + str(salariototal))
print(dietas)
print(retencion)



