import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"

class conexionHospital:
    def __init__(self):
        #Self hace referencia a la clase que estamos creando
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
        + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

    def eliminarEnfermo(self, inscripcion):
        cursor = self.conexion.cursor()
        sql="delete from enfermo where inscripcion=?"
        cursor.execute(sql, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarEnfermo(self, apellido, inscripcion):
        cursor = self.conexion.cursor()
        sqlupdate = "update enfermo set apellido=? where inscripcion=?"
        cursor.execute(sqlupdate, (apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados

