ciudades = []

def mostrarCiudades():
    for i in ciudades:
        print(i)

def insertarCiudad():
    print("Introduzca una ciudad")
    ciudad = input()
    ciudades.append(ciudad)

def guardarFichero():
    lista = "\n".join(ciudades)
    fichero = open("ficheros/ciudades.txt", "w+")
    fichero.write(lista)
    fichero.flush
    fichero.close
    print("Datos almacenados")

def leerFichero():
    fichero = open("ficheros/ciudades.txt", "r")
    contenido = fichero.read()
    fichero.close()
    global ciudades
    ciudades = contenido.split(sep="\n")
    print("Datos cargados")

def mostrarMenu():
    print("\n")
    print("0-Salir")
    print("1-Leer ciudades, fichero")
    print("2-Guardar ciudades, fichero")
    print("3-Nueva ciudad")
    print("4-Mostrar ciudades")
    print("Elige")


opcion = -1
while (opcion != 0):

    mostrarMenu()
    opcion=int(input())

    if opcion==1:
        leerFichero()
    elif opcion==2:
        guardarFichero()
    elif opcion==3:
        insertarCiudad()
    elif opcion==4:
        mostrarCiudades()
    elif opcion==0:
        print("Hasta luego")
    else:
        print("Opcion incorrecta")