def mostrarMenu():
    print("0- Salir")
    print("1- Bisiesto")
    print("2- Narcisista")
    print("Selecciona una opción")


def anioBisiesto(anio):
    if(anio%4==0 and (anio%100!=0 or anio%400==0)):
        valor=True
    else:
        valor=False
    return valor
    

def numNarcisista(textoNum):

    longitud=len(textoNum)
    suma=0
    for i in range(longitud):
        caracter=textoNum[i]
        numero=int(caracter)
        potencia= pow(numero,longitud)
        suma=suma+potencia  
   
    if(suma==int(textoNum)):
        valor = True
    else:
        valor = False
    return valor
