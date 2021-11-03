import pyodbc
print("Eliminar enfermo")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

cursor=conexion.cursor()
sql="select apellido, inscripcion from enfermo"
cursor.execute(sql)
print(("---------ENFERMOS---------"))
for row in cursor:
    print(row.apellido + ", " + str(row.inscripcion))
cursor.close()

print(("Introduce el nº de inscripcion:"))
inscripcion=input()

cursor=conexion.cursor()
sql="delete from enfermo where inscripcion=?"
cursor.execute(sql, (inscripcion))
cursor.commit()
cursor.close()

cursor=conexion.cursor()
sql="select apellido, inscripcion from enfermo"
cursor.execute(sql)
print(("---------ENFERMOS---------"))
for row in cursor:
    print(row.apellido + ", " + str(row.inscripcion))
cursor.close()
conexion.close()