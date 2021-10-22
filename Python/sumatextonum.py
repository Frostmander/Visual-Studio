print("Ejemplo sumando números de string")
print("Introduzca un texto de SOLO NÚMEROS")

textonumeros=input()

longitud = len(textonumeros)
suma=0
for i in range(longitud):
    caracter = textonumeros[i]
    numero=int(caracter)

    suma=suma+numero

print("La suma es: " + str(suma))