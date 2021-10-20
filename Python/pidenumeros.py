
seguir="s"
while seguir == "s":

    print("Intrudce número")
    num=int(input())

    if (num>0):
        print("Número positivo")
    elif (num<0):
        print("Número negativo")
    else:
        print("CERO")

    print("¿Quieres continuar? (s/n)")
    seguir=str(input())

print("Hasta pronto")