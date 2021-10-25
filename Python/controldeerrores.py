def mostrarDoble():
    try:    
        print("Dame un número")
        numero= int(input())
        print("El doble es:" + str(numero*2))
    except ValueError:
        print ("Error, debes introducir un número")
        mostrarDoble()

print("Programa principal de control de errores:")
mostrarDoble()