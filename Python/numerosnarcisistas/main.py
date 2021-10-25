from metodosnarcisis import *

opcion=-1
while (opcion!=0):

    mostrarMenu()
    opcion=int(input())

    if opcion==1:
               
        print("Introduce un año:")
        numero=input()
        while comprobarNum(numero)==False:
            print("Mal, introntroducelo bien:")
            numero=input()   
        
        if(anioBisiesto(int(numero))):
            print("Es bisiesto")
        else:
            print("No es bisiesto")
        
    elif opcion==2:
        print("Introduce un numero:")
        numero=input()
        while comprobarNum(numero)==False:
            print("Mal, introntroducelo bien:")
            numero=input()  
        if(numNarcisista(numero)):
            print("Es narcisista")
        else:
            print("No es narcisista")

    elif opcion==3:
        print("Introduce tu fecha de nacimiento:")
        numero=input()
        while comprobarFecha(numero)==False:
            print("Mal, introduce xx/xx/xxxx o xx-xx-xxxx:")
            numero=input()
        numero=getAnioFecha(numero)
        rangoBisiestos(numero)

    else:
        print("¡Adios!")
