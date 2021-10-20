print("Introduce 3 números")
num1=int(input())
num2=int(input())
num3=int(input())
suma= num1+num2+num3

if (num1 == num2 and num1 == num3):
    print("Los tres números son iguales")
elif (num1 >= num2 and num1 >= num3):
    print("El mayor es:",num1)
    if(num2<=num3):
        print("El menor es", num2)
    else:
        print("El menor es", num3)
elif (num2 >= num1 and num2 >= num3):
    print("el mayor es:", num2)
    if(num1<=num3):
        print("El menor es", num1)
    else:
        print("El menor es", num3)
else:
    print("El mayor es:",num3)
    if(num2<=num1):
        print("El menor es", num2)
    else:
        print("El menor es", num1)

print("La suma de los tres es:",suma)

if (num1>=num2 and num1<=num3):
    print("El intermedio es:",num1)
elif (num2>=num1 and num2<=num3):
    print("El intermedio es:",num2)
else:
    print("El intermedio es:", num3)