import pyodbc
print("Recorrer datos SQL")
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
#Necesitamos una consulta, el cursor 
#maneja tanto consultas de selección (SELECT)
#como consultas de acción, no le importa
#Creamos la consulta select
#No es conveniente utilizar el *
sql = "select dept_no, dnombre, loc from dept"
#El cursor ejecutará la consulta
cursor.execute(sql)
#Para recorrer, se utiliza un bucle FOR
for row in cursor:
    #Podemos dibujar un dato de una columna
    #Por el INDICE de la columna en la consulta
    #1 se corresponde con la columna DNOMBRE
    print(row[0])
    #Tambien podemos dibujar con una propiedad
    #de ROW que es el NOMBRE DE COLUMNA
    #SENSIBLE A MAYUS
    print(row.dnombre)
    print(row.loc)

print('\n')
cursor.execute(sql)
#Tambien podemos guardar el dato de la columna en una variable
for row in cursor:
    numero=row.dept_no
    nombre=row.dnombre
    localidad=row.loc
    print(str(numero) +" "+ nombre +" "+ localidad)


print('\n')
cursor.execute(sql)
#También podemos utilizar un bucle con la declaración de variables 
#de las columnas de la consulta.
for numero, nombre, localidad in cursor:
    print(str(numero) +" - "+ nombre +" - "+ localidad)


#En realidad, una vez que hemos recorrido el cursor
#ya no tiene registros
#No podemos acceder a las filas una vez terminado el 
#cursor
#fila = cursor.fetchone()
#print(fila)
#Siempre debemos cerrar el cursor despues de leer
cursor.close()
conexion.close()
print("Fin de programa")