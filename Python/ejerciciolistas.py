def mostrarNombres():
    print("----------------------------")
    longitud = len(nombres)
    for i in range(longitud):
        name = nombres[i]
        print(str(i) + ".-" + name)
    print("----------------------------")

def mostrarMenu():
    print("0-Salir")
    print("1-Nuevo nombre")
    print("2-Eliminar nombre (posición)")
    print("3-Comenzar de nuevo")
    print("Elige")

def guardarNombres():
    respuesta=" "
    while respuesta.upper() != "OK":
        print("Introduce un nombre: ('OK' PARA SALIR)")
        respuesta = input()
        if respuesta.upper() != "OK":
            nombres.append(respuesta)
        


nombres = []
respuesta=-1

guardarNombres()
mostrarNombres()

opcion=-1
while opcion!=0:

    try:
        mostrarMenu()
        opcion=int(input())


        if opcion==1:
            print("Introduce nombre: ")
            nombre=input()
            nombres.append(nombre)
            mostrarNombres()
        elif opcion==2:
            print("Indica la posicion del nombre a borrar: ")
            indice=int(input())
            nombres.pop(indice)
            mostrarNombres()
        elif opcion==3:
            print("Lista borrada. Introduce nuevos valores")
            nombres.clear()
            guardarNombres()
            mostrarNombres()
        elif opcion == 0:
            print("Hasta luego")
        else:
            print("Opcion incorrecta")
    except IndexError:
        print("Indice no válido")
    except ValueError:
        print("Debe introducir números")

print("¡Adios!")