print("Dame un número")

num1=int(input())

print("Dame otro número")

num2=int(input())


if num1 == num2:
    print("Son iguales")
elif num1 > num2:
    print(num1, "es mayor")
else:
    print(num2, "es mayor")