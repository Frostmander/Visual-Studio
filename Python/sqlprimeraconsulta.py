import pyodbc

print("Primera consulta SQL Server")
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"

#CADENA CONEXION CON SEGURIDAD SQL SERVER (REMOTO)
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

print("Intentando conectar...")
conexion = pyodbc.connect(cadenaconexion)
print("Conectado!!!")

#CURSOR se crea con una conexión abierta
cursor = conexion.cursor()
#Necesitamos una consulta, el cursor maneja tanto consultas de selección (SELECT)
#como consultas de acción, no le importa
#Creamos la consulta select
sql = "select * from dept"
#El cursor ejecutará la consulta
cursor.execute(sql)
#Podemos, por ejemplo, recuperar una fila
row = cursor.fetchone()
#Vamos a dibujar la fila
print(row)
#Vamos a escribir otra vez fetchone()
row = cursor.fetchone()
print(row)
#Cada vez que ejecutamos el método fetch
#el cursor se mueve una fila
#No podemos volver a la fila anterior,
#tendríamos que ejecutar otra vez el método
#execute() de la conexión
#Vamos a pasarnos de filas a ver que sucede
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
#Siempre debemos cerrar el cursor despues de leer
conexion.close()
print("Fin de programa")