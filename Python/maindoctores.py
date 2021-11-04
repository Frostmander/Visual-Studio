from doctores import DoctoresClase
opcion=-1
while opcion!=6:
    print("----------Menu Doctores----------")
    print("1-Insertar Doctor")
    print("2-Modificar salario")
    print("3-eliminar doctor")
    print("4-Buscar doctor")
    print("5-Mostrar doctores")
    print("6-Salir")
    opcion=int(input())

    conexion=DoctoresClase()
    if opcion==1:
        print("-----HOSPITALES-----")
        hospitales=conexion.mostrarHosp()
        for hosp in hospitales:
            print(hosp)
        print("-----Nuevos datos-----")
        print("Código Hospital:")
        codhospital=int(input())
        print("Apellido:")
        apellido=input()
        print("Especialidad:")
        especialidad=input()
        print("Salario:")
        salario=int(input())
        respuesta=conexion.insertarDoc(codhospital, apellido, especialidad, salario)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==2:
        print("-------Nuevo Salario--------")
        print("ID del Doctor:")
        coddoctor=int(input())
        print("Incremento:")
        incremento=int(input())
        respuesta=conexion.modificarDoc(coddoctor, incremento)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==3:
        print("-------Eliminar Doctor--------")
        print("ID del Doctor:")
        coddoctor=int(input())
        respuesta=conexion.eliminarDoc()(coddoctor)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==4:
        print("Introduce el ID del doctor:")
        id=int(input())
        respuesta=conexion.buscarDoc(id)
        if (not respuesta):
            print("No existe el doctor")
        else:
            print(respuesta)
        print("\n")
    elif opcion==5:
        respuesta = conexion.mostrarDocs()
        for dept in respuesta:
            print(dept)
        print("\n")
    elif opcion==6:
        print("Adios")
        print("\n")
    else:
        print("Opción incorrecta")
        print("\n")