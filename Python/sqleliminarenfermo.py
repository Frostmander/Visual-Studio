import pyodbc
from conexionhospital import conexionHospital

print(("Introduce el nº de inscripcion:"))
inscripcion=input()

connection = conexionHospital()
respuesta=connection.eliminarEnfermo(inscripcion)
print("Registros eliminados: " + str(respuesta))

print(("Introduce el nº de inscripcion para modificar:"))
ins=int(input())
print(("Introduce el nuevo apellido:"))
ape=input()
respuesta2 = connection.modificarEnfermo(ape,ins)
print("Registros eliminados: " + str(respuesta2))