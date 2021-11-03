from coche import Coche
from deportivo import Deportivo


car = Coche()
car.marca = "Hyundai"
car.modelo = "i10"
car.arrancar()
car.acelerar()

supercar = Deportivo()
supercar.marca = "Ferrari"
supercar.modelo = "F40"
supercar.acelerar()

# print(supercar.marca + " " + supercar.modelo)

# opcion=-1
# while(opcion != 0):
#     print("-------------------")
#     print("0-Salir")
#     print("1-Arrancar")
#     print("2-Acelerar")
#     print("3-Frenar")
#     print("4-Detener coche")
#     print("Elige")
#     print("-------------------")
#     opcion=int(input())
#     if opcion==1:
#         car.arrancar()

#     elif opcion==2:
#         car.acelerar()

#     elif opcion==3:
#         car.frenar()

#     elif opcion==4:
#         car.detener()
    
#     elif opcion==0:
#         print("Adios cochecito")
#     else:
#         print("Opción incorrecta")