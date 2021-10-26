class Persona:
    nombre = ""
    apellidos = ""
    fechanacimiento = 0
    pais = ""

    def __str__(self):
        return self.nombre + " " + self.apellidos + ", Pais " + self.pais + ", Edad " + str(self.getEdad())

    def __init__(self):
        #Inicia la variables, todas las personas seran por defecto de Japón
        self.pais = "Japón"

    def getNombreCompleto(self):
        #Nuestro código
        return self.nombre + " " + self.apellidos

    def getEdad(self):
        return 2021-  self.fechanacimiento
    
    def getDescripcion (self, midescripcion):
        return self.getNombreCompleto() + ", " + midescripcion