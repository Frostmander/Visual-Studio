import pyodbc
print("Incrementar salario")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

print("Introduce el oficio:")
oficio=input()
print("Introduce la cantidad a incrementar:")
incremento=input()

cursor=conexion.cursor()
sql="update emp set salario=salario+" + incremento + " where oficio='" + oficio + "'"
cursor.execute(sql)
cursor.commit()
print("Empleados afectados: " + str(cursor.rowcount))
cursor.close()

cursor=conexion.cursor()
sql="select apellido, oficio, salario from emp where oficio='" + oficio + "'"
cursor.execute(sql)
for row in cursor:
    print(row.apellido + ", " + row.oficio + ", " + str(row.salario))
cursor.close()


conexion.close()