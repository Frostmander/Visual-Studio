print("Ejemplo metodos string")
texto = "Hola python"

#Probando con métodos
print("Mayusculas: " + texto.upper())
print("Sustituir o-@: " + texto.replace("o","@"))
print("Primera letra: " + texto[0])
print("Longitud texto " + str(len(texto)))
print("Buscar letra P: " + str(texto.find("p")))
print("Buscar siguiente letra p: " + str(texto.find("o",0)))

#Busca la posicion de la primera letra o
posicion = texto.find("o")
#Buscamos a partir de la primera letra o
print("Buscar siguiente letra o: " + str(texto.find("o",posicion+1)))

#Buscando desde el final
print("Posicion desde el final de la letra o: " + str(texto.rfind("o")))


print("¿Empieza con la A?: " + str(texto.startswith("A")))
print("¿Empieza con la H?: " + str(texto.startswith("H")))

print("Texto números: " + str(texto.isdigit()))
print("Texto letras: " + str(texto.isalpha()))

subcadena= texto[2:]
print("Posicion 2 en adelante: " + subcadena)
subcadena= texto[2:6]
print("Posicion 2 hasta 6 : " + subcadena)

longitud = len(texto)
for i in range(longitud):
    letra=texto[i]
    print(str(i)+ ": " + letra)

print("Escribe algo: ")
aux = input()
if (aux.isdigit()):
    print("Es un númnero")
else:
    print("No es un número")