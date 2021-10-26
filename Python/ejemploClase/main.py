from persona import Persona

human = Persona()

print("Pais " + human.pais)
human.pais = "España"
print("Pais " + human.pais)

human.nombre = "Inosuke"
human.apellidos = "Hasibira"
human.fechanacimiento= 1905

print (human.getNombreCompleto())

print("Edad " + str(human.getEdad()))

print(human)


print(human.getDescripcion("cachis"))