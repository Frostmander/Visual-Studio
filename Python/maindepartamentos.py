from pyodbc import Connection, connect
from conexiondepartamentos import conexionDepartamento
from departamento import Departamento

opcion=-1
while opcion!=5:
    print("----Menu----")
    print("1-Añadir departamento")
    print("2-Eliminar departamento")
    print("3-Modificar departamento")
    print("4-Buscar departamento")
    print("5-Mostrar todos los departamentos")
    print("6-Salir")
    opcion=int(input())

    conexion = conexionDepartamento()
    if opcion==1:
        print("Introduce el nº:")
        numero=int(input())
        print("Introduce el nombre del departamento:")
        nombre=input()
        print("Introduce la localidad:")
        localidad=input()
        respuesta=conexion.insertarDep(numero,nombre,localidad)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==2:
        print("Introduce el nº:")
        numero=int(input())
        respuesta=conexion.eliminarDep(numero)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==3:
        print("Introduce el nº:")
        numero=int(input())
        print("Introduce el nuevo nombre:")
        nombre=input()
        print("Introduce la nueva localidad:")
        localidad=input()
        respuesta=conexion.modificarDep(numero, nombre, localidad)
        print("Registros afectados: " + str(respuesta))
        print("\n")
    elif opcion==4:
        print("Introduce nº departamento:")
        numero=int(input())
        consulta=conexion.buscarDep(numero)
        if (not consulta):
            print("No existe el departamento")
        else:
            print(consulta)
        print("\n")
    elif opcion==5:
        departamentos = conexion.todosDep()
        for dept in departamentos:
            print(dept)
    elif opcion==6:
        print("Adios")
        print("\n")
    else:
        print("Opción incorrecta")
        print("\n")