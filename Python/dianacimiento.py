from math import trunc

print("Tu día de nacimiento: ")
dia=int(input())
print("Tu mes de nacimiento: ")
mes=int(input())
print("Tu año de nacimiento: ")
anio=int(input())

if mes==1 :
    mes=13
    anio=anio-1

if mes==2:
    mes=14
    anio=anio-1

num1= trunc(((mes + 1) * 3) / 5)
num2= trunc(anio/4)
num3= trunc(anio/100)
num4= trunc(anio/400)

num1= dia + (mes * 2) + anio + num1 + num2 - num3 + num4 + 2
num2= trunc(num1/7)
num3= num1-(num2*7)

if num3==0 :
    print("Naciste en sábado") 

if num3==1 :
    print("Naciste en domingo") 

if num3==2 :
    print("Naciste en lunes") 

if num3==3 :
    print("Naciste en martes") 

if num3==4 :
    print("Naciste en miercoles") 

if num3==5 :
    print("Naciste en jueves") 

if num3==6 :
    print("Naciste en viernes") 
