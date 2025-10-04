class Perro:
    def __init__(self, nombre, edad, genero, raza, vacunado, propietario):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.raza = raza
        self.vacunado = vacunado
        self.propietario = propietario

bobby= Perro("Bobby", 2, "macho", "Mestizo", False, "Patricia")
negra = Perro("Negra", 5, "hembra", "Chapi", True, "Giovanni")

# Mostrar atributos
print(bobby.nombre)
print(bobby.genero)
print(bobby.edad)
print(bobby.vacunado)
print(bobby.propietario)

print(negra.nombre)
print(negra.genero)
print(negra.edad)
print(negra.vacunado)
print(negra.propietario)