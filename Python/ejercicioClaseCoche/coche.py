class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False

    def __init__(self):
        self.velocidad=0
        self.estado=False

    def arrancar(self):
        if(self.estado==False):
            self.estado = True
            print("Arrancando")
                        
        else:
            print("El coche ya está arrancado")

    def detener(self):
        if(self.estado==True):
            self.estado=False
            self.velocidad=0
            print("Deteniendo")
        else:
            print("El coche ya esta apagado.")


    def acelerar(self):
        if(self.estado==False):
            print("Primero debe arrancar el coche")
        else:
            print("Acelerando...")
            self.velocidad+=10
            print(self.velocidad)

    def frenar(self):
        if(self.velocidad==0):
            print("El coche esta quieto")
            
        else:
            print("Frenando...")
            self.velocidad-=10
            print(self.velocidad)

