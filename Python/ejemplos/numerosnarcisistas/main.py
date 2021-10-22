from metodosnarcisis import *

opcion=-1
while (opcion!=0):

    mostrarMenu()
    opcion=int(input())

    if opcion==1:
        print("Introduce un numero:")
        numero=int(input())
        if(anioBisiesto(numero)):
            print("Es bisiesto")
        else:
            print("No es bisiesto")
        
    elif opcion==2:
        print("Introduce un numero:")
        numero=input()
        if(numNarcisista(numero)):
            print("Es narcisista")
        else:
            print("No es narcisista")

    elif opcion==3:
        print("Introduce tu año de nacimiento:")
        numero=int(input())
        rangoBisiestos(numero)

    elif opcion==0:
        print("¡Adios!")
        break

    else:
        print("Numero incorrecto")
