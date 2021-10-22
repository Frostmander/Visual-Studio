#Importar librerias
from math import trunc

#Pedir DNI al usuario
print("Validar DNI")
print("Introduzca su número DNI")
dni = input()

#Validar si solo ha introducido numeros
while dni.isdigit() == False:
    print("Debe introducir solo números")
    print("Introduzca su número DNI")
    dni = input()

numerodni=int(dni)

resultado = (numerodni-(trunc(numerodni/23)*23))


tabladni="TRWAGMYFPDXBNJZQVHLCKET"
letra = tabladni[resultado]
print("Su letra es: " + letra)
