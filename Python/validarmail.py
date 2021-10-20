print("Introduce tu email: ")
mail=str(input())

if (mail.startswith("@")):
    print("Error, no puede comenzar con @")
    
if (mail.endswith("@") or mail.endswith(".")):
    print("Error, no puede acabar con @ o .")

arroba = mail.find("@")
punto = mail.find(".")

if (punto<0 or arroba<0):
    print("Error, necesita un punto y una @")

longitud = len(mail)
contador=0
for i in range(longitud):
    letra=mail[i]
    if (letra=="@"):
        contador+=1
        if (contador>1):
            print("Error, tiene mas de una @")
            break

PuntoDesArroba = mail.find(".",arroba+1)
if (PuntoDesArroba<0):
    print("Error, no tiene punto despues de @")

dominio=mail[punto+1:]

if(len(dominio)<2 or len(dominio)>4):
    print("Error, el dominio tiene demasiadas letras")