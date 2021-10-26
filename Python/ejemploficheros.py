print("Ejemplo ficheros")

fichero = open("ficheros/texto.txt", "w+")
print("Escríbeme algo pichilla")
texto = input()
fichero.write(texto)
fichero.close()

archivo = open("ficheros/texto.txt", "a")
print("Dime tu nombre")
nombre = input()
archivo.write("\n" + nombre)
archivo.close()

file = open("ficheros/texto.txt", "r")
contenido = file.read()
print(contenido)
file.close()
