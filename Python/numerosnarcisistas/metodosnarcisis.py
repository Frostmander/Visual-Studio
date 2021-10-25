def mostrarMenu():
    print("0- Salir")
    print("1- Bisiesto")
    print("2- Narcisista")
    print("3- Bisiestos desde tu fecha")
    print("Selecciona una opción")


def anioBisiesto(anio):
    #Metodo para averiguar si el año es bisiesto o no
    if(anio%4==0 and (anio%100!=0 or anio%400==0)):
        return True
    else:
        return False
    

def numNarcisista(textoNum):

    #Metodo para averiguar si un numero es "narcisista"
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

    #Metodo para averiguar el rango de años bisiestos que hay desde el año introducido hasta el actual
    import datetime
    
    fechahoy= datetime.date.today()
    anioactual=fechahoy.year
    for i in range(fecha,anioactual):
        if anioBisiesto(i)==True:
            print(i)

def getAnioFecha(textofecha):
    #Metodo para averiguar el año apartir de una fecha con formato 00/00/0000 o 00-00-0000
    if (textofecha.find("/")!=-1):
        textofecha = textofecha.replace("/","@")
    else:
        textofecha = textofecha.replace ("-", "@")
    ultimaarroba = textofecha.rfind("@")
    anio = textofecha[ultimaarroba +1:]
    return int(anio)


def comprobarNum(numero):
    if (numero.isdigit()==True):
        return True
    else:
        return False

def comprobarFecha(fecha):
    if ((fecha[2]=="/" and fecha[5]=="/") or (fecha[2]=="-" and fecha[5]=="-")):
        return True
    else:
        return False