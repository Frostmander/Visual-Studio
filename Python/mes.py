import random
class Mes:

    mesNom = ""
    temMax = 0
    temMin = 0

    def temperaturaMedia(self,):
        return (self.temMax + self.temMin)/2
    
    def __str__(self):
        return (self.mesNom + ", Máxima: " + str(self.temMax) + ", Mínima: " + str(self.temMin) + ", Media: " + str(self.temperaturaMedia()) )