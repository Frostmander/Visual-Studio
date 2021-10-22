print("Validar ISBN")
print("Introduce ISBN:")
isbn=input()

logitud=len(isbn)
suma=0
mult=0

if (logitud != 10 or isbn.isdigit() == False):
    print("Número incorrecto")

else:
    for i in range(logitud):
        caracterisbn=isbn[i]
        numeroisbn=int(caracterisbn)
        mult=numeroisbn*(i+1)
        suma=suma+mult

    if (suma%11 == 0):
        print("El número es correcto")
    else:
        print("Número incorrecto")

print("Fin de programa")