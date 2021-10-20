print("Ejemplo números pares")

print("Número inicial")
inicio = int(input())
print("Número final")
fin = int(input())
print("Números pares:")
for i in range (inicio,fin + 1):
    if (i % 2 == 0):
        print(i)