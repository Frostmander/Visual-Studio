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

#Ejecución del programa
opcion=-1
while opcion!=0:
    print("--------------------------------")
    mostrarMenu()
    opcion=int(input())
    continuar="s"
    if opcion == 1:
        while continuar=="s":
            print("Dame dos numeros")
            num1=int(input())
            num2=int(input())
            operacion=sumarNum(num1,num2)
            print(str(num1) + "+" + str(num2) + "= " + str(operacion))
            print("¿Deseas usar otros números?(s/n)")
            continuar=input()
    elif opcion == 2:
        while continuar=="s":    
            print("Dame dos numeros")
            num1=int(input())
            num2=int(input())
            operacion=restarNum(num1,num2)
            print(str(num1) + "-" + str(num2) + "= " + str(operacion))
            print("¿Deseas usar otros números?(s/n)")
            continuar=input()
    elif opcion == 3:
        while continuar=="s": 
            print("Dame dos numeros")
            num1=int(input())
            num2=int(input())
            operacion=dividirNum(num1,num2)
            print(str(num1) + "/" + str(num2) + "= " + str(operacion))
            print("¿Deseas usar otros números?(s/n)")
            continuar=input()
    elif opcion == 4:
        while continuar=="s": 
            print("Dame dos numeros")
            num1=int(input())
            num2=int(input())
            operacion=multiplicarNum(num1,num2)
            print(str(num1) + "*" + str(num2) + "= " + str(operacion))
            print("¿Deseas usar otros números?(s/n)")
            continuar=input()
    elif opcion == 0:
        break
    else:
        print("Opcion incorrecta")
    
print("Adios!")