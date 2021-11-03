import pyodbc
print("Buscador departamentos")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
conexion = pyodbc.connect(cadenaconexion)

#Vamos a pedir el número de departamento
print("Introduzca número departamento a buscar")
numero = input()
#Vamos a utilizar el número para CONCATENAR la consulta sql
#Deberíamos capturar el número como String para concatenarlo con 
#el String Sql

sql = "select dept_no, dnombre, loc from dept where dept_no=" + numero
cursor = conexion.execute(sql)
row = cursor.fetchone()

if (not row):
    print("No existe el departamento")
else:
    print(row.dnombre + ", " + row.loc)
cursor.close()
conexion.close()
print("Fin de programa")
