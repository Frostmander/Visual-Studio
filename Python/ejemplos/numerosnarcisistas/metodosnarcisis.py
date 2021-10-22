def mostrarMenu():
    print("0- Salir")
    print("1- Bisiesto")
    print("2- Narcisista")
    print("3- Bisiestos desde tu fecha")
    print("Selecciona una opción")


def anioBisiesto(anio):
    if(anio%4==0 and (anio%100!=0 or anio%400==0)):
        return True
    else:
        return False
    

def numNarcisista(textoNum):

    longitud=len(textoNum)
    suma=0
    for i in range(longitud):
        caracter=textoNum[i]
        numero=int(caracter)
        potencia= pow(numero,longitud)
        suma=suma+potencia  
   
    if(suma==int(textoNum)):
        return True
    else:
        return False


def rangoBisiestos (fecha):

    for i in range(fecha,2021):
        if anioBisiesto(i)==True:
            print(i)

