#from metodosexternosmatematicas import mostrarMenu, sumarNum <--- importa los que le digas
#import metodosexternosmatematicas <--- importa todo, necesitas poner el nombre de la libreria para cada metodo
from metodosexternosmatematicas import * #<-- importa todo

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