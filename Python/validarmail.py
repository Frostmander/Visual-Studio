print("Introduce tu email: ")
mail=str(input())

arroba = mail.find("@")
punto = mail.find(".")

if (mail.find("@")==-1):
    print("Error, necesita una @")

elif (mail.find(".")==-1):
        print("Error, necesita un .")

elif (mail.startswith("@") or mail.endswith("@") or mail.startswith(".") or mail.endswith(".")):
    print("Error, no puede comenzar o acabar con @ o .")

elif(mail.find("@") != mail.rfind("@")):
    print("Email con mas de una @")
#buscar @ con un bucle
#longitud = len(mail)
#contador=0
#for i in range(longitud):
#    letra=mail[i]
#    if (letra=="@"):
#        contador+=1
#        if (contador>1):
#            print("Error, tiene mas de una @")
#            break

elif (mail.find(".",arroba+1)==-1):
    print("Error, no tiene punto despues de @")

else :
    if(len(mail[punto+1:])<2 or len(mail[punto+1:])>4):
        print("Error, el dominio debe tener entre 2 y 4 letras")
    else:
        print("Email correcto!!!!!!!")