def dividirNum():
    try:    
        print("Dame un número")
        numero1= int(input())
        print("Dame otro número")
        numero2= int(input())
        print("El doble es:" + str(numero1/numero2))
    except ValueError:
        print ("Error, debes introducir un número")
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
    except:
        print("Error general")
    finally:
        print("Siempre me ejecuto")

print("Programa principal de control de errores:")
dividirNum()