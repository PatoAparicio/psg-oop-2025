class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

animal1 = Animal("León", "mamífero", "Sabana africana")
animal2 = Animal("Elefante", "mamífero", "Bosques de Asia")
animal3 = Animal("Cocodrilo", "reptil", "Ríos de América")
animal4 = Animal("Águila", "ave", "Montañas rocosas")
print("Animales registrados:")
print("Mamífero 1: ",animal1.origen, animal1.especie, animal1.tipo, animal1.lugar)
print("Mamífero 2: ",animal2.origen, animal2.especie, animal2.tipo, animal2.lugar)
print("Reptíl: ",animal3.origen, animal3.especie, animal3.tipo, animal3.lugar)
print("Ave: ",animal4.origen, animal4.especie, animal4.tipo, animal4.lugar)