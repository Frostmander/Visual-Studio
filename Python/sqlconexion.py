import pyodbc
print("Primera consulta SQL Server")
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="azure"

#CADENA CONEXION CON SEGURIDAD SQL SERVER (REMOTO)
cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

#CADENA CONEXION CON SEGURIDAD WINDOWS (ON PREMISE)
# cadenaconexion=("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
# + "; DATABASE=" + bbdd + "; Trusted_connection=yes")

try:
    print("Intentando conectar...")
    conexion = pyodbc.connect(cadenaconexion)
    print("Conectado!!!")
except pyodbc.InterfaceError:
    print("Buff, esto no va bien")
finally:
    conexion.close()