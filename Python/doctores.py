import pyodbc
from doctor import Doctor
from hospital import Hospital

servidor = "LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario = "SA"
password = "azure"

class DoctoresClase:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor 
        + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

    def mostrarHosp(self):
        cursor=self.conexion.cursor()
        sql="select hospital_cod, nombre from hospital" 
        cursor.execute(sql)
        hospitales=[]
        for row in cursor:
            hosp=Hospital()
            hosp.hospitalcod=row[0]
            hosp.nombre=row[1]
            hospitales.append(hosp)
        cursor.close()
        return hospitales

    def insertarDoc(self, codh, apellido, especialidad, salario):
        cursor=self.conexion.cursor()
        sql="insert into doctor values (?,(select max(doctor_no)+1 from doctor),?,?,?)"
        cursor.execute(sql, (codh, apellido, especialidad, salario))
        filas=cursor.rowcount
        cursor.commit()
        cursor.close()
        return filas

    def modificarDoc(self, id, salario):
        cursor=self.conexion.cursor()
        sql="update doctor set salario=salario+? where doctor_no=?" 
        cursor.execute(sql, (salario, id))
        filas=cursor.rowcount
        cursor.commit()
        cursor.close()
        return filas

    def eliminarDoc(self, id):
        cursor=self.conexion.cursor()
        sql="delete from doctor where doctor_no=?" 
        cursor.execute(sql, (id))
        filas=cursor.rowcount
        cursor.commit()
        cursor.close()
        return filas
    
    def buscarDoc(self, id):
        cursor=self.conexion.cursor()
        sql="select hospital_cod, doctor_no, apellido, especialidad, salario from doctor where doctor_no=?" 
        cursor.execute(sql, (id))
        row=cursor.fetchone()
        if not row:
            cursor.close()
            return None
        else:
            doctor=Doctor()
            doctor.hospitalcod=row.hospital_cod
            doctor.doctorno=row.doctor_no
            doctor.apellido=row.apellido
            doctor.especialidad=row.especialidad
            doctor.salario=row.salario
            cursor.close()
            return doctor

    def mostrarDocs(self):
        cursor=self.conexion.cursor()
        sql="select hospital_cod, doctor_no, apellido, especialidad, salario from doctor" 
        cursor.execute(sql)
        doctoreslist=[]
        for row in cursor:
            doctor=Doctor()
            doctor.hospitalcod=row.hospital_cod
            doctor.doctorno=row.doctor_no
            doctor.apellido=row.apellido
            doctor.especialidad=row.especialidad
            doctor.salario=row.salario
            doctoreslist.append(doctor)
        cursor.close()
        return doctoreslist