class Hospital:
    hospitalcod=0
    nombre=""

    def __str__(self):
        return (str(self.hospitalcod) + " - " + self.nombre)