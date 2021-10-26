print("Ejemplo de listas")
print("LISTA DE NÚMEROS ENTEROS")
numeros = [20, 14, 55, 99, 77]
print("Primer número de la lista: " + str(numeros[0]))
print("---------------------------------")
print("LISTA DE STRINGS")
nombres=["Ana","Adrian","Lucía","Carlos", "Pedro"]
longitud = len(nombres)
print("Longitud de todos los nombres: " + str(longitud))
print("---------------------------------")
#Bucle para recorrer lista
for i in range(longitud):
    print(nombres[i])
print("---------------------------------")
#Bucle de referencia
for name in nombres:
    print(name)