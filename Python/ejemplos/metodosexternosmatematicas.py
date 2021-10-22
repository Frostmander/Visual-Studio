#Definir métodos
def mostrarMenu():
    print("0- Salir")
    print("1- Sumar")
    print("2- Restar")
    print("3- Dividir")
    print("4- Multiplicar")
    print("Selecciona una opción")

def sumarNum(num1,num2):
    suma=num1+num2
    return suma

def restarNum(num1,num2):
    resta=num1-num2
    return resta

def dividirNum(num1,num2):
    divi=num1/num2
    return divi

def multiplicarNum(num1,num2):
    multi=num1*num2
    return multi
