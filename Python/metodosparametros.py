#Ejemplo de método de ejecución
def saludo(nombre, apellido):
    print("Bienvenido, " + nombre + " " + apellido)

#Ejemplo de método que devuelve un valor
def convertirTexto(texto):
    return texto.upper()



print("Dime tu nombre")
var1=input()
print("Dime tu apellido")
var2=input()
saludo(var1, var2)

print("Escribe algo para ponerlo en MAYUS")
var3=input()
print(convertirTexto(var3))



