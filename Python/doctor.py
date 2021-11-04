class Doctor:
    hospitalcod=0
    doctorno=0
    apellido=""
    especialidad=""
    salario=0

    def __str__(self):
        return (str(self.hospitalcod) + " - " + str(self.doctorno) + " - " + self.apellido + " - " + self.especialidad + " - " + str(self.salario))