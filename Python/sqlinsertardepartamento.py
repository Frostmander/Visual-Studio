import pyodbc
print("Insertar departamento")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"
conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

#Número sera una estring por que se va a concatenar posteriormente
print("Introduzca un número")
numero=input()
print("Introduzca un nombre")
nombre=input()
print("Introduzca un localidad")
localidad=input()

cursor = conexion.cursor()
sql = "insert into dept values (" + numero + ",'" + nombre + "','" + localidad + "')"
print(sql)
cursor.execute(sql)
#Para las consultas de accion afecten a la bbdd debemos hacer un commit
cursor.commit()
#Imprimimos rowcount para averiguar si tenemos contenido en la propiedad
#Rowcount indica el numero de filas afectadas
print("Rowcount: " + str(cursor.rowcount))
cursor.close()

#Reutilizamos el cursor para hacer una consulta
#Pero hay que volver a abrir
cursor=conexion.cursor()
sql="select dept_no, dnombre, loc from dept"
cursor.execute(sql)
print("-----------------Departamentos-----------------")
for row in cursor:
    print(row.dnombre + ", " + row.loc)
cursor.close()


conexion.close()
print("Fin de programa")