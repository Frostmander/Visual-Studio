import pyodbc
from departamento import Departamento
servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"

class conexionDepartamento:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
        + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
    
    def insertarDep(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sql="insert into dept values (?, ?, ?)"
        cursor.execute(sql, (numero, nombre, localidad))
        afectados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return afectados

    def modificarDep (self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sql="update dept set Dnombre=?, loc=? where dept_no=?"
        cursor.execute(sql, (nombre, localidad, numero))
        afectados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return afectados

    def eliminarDep (self, numero):
        cursor = self.conexion.cursor()
        sql="delete from dept where dept_no=?"
        cursor.execute(sql, (numero))
        afectados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return afectados

    def buscarDep (self, numero):
        cursor = self.conexion.cursor()
        sql="select dept_no, dnombre, loc from dept where dept_no=?"
        cursor.execute((sql), numero)
        row=cursor.fetchone()
        if not row:
            cursor.close()
            return None
        else:
            departamento = Departamento()
            departamento.numero=row.dept_no
            departamento.nombre=row.dnombre
            departamento.localidad=row.loc
            cursor.close()
            return departamento
    
    def todosDep (self):
        cursor= self.conexion.cursor()
        sql="select dept_no, dnombre, loc from dept"
        cursor.execute(sql)
        departamentos=[]
        for row in cursor:
            dept = Departamento()
            dept.numero = row.dept_no
            dept.nombre = row.dnombre
            dept.localidad = row.loc
            departamentos.append(dept)
        cursor.close()
        return departamentos 