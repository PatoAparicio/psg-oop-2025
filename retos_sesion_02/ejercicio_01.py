class Animal:
    origen = "feral"
    def __init__(self, especie, tipo, lugar):
        self.especie = especie
        self.tipo = tipo
        self.lugar = lugar

leon = Animal("León", "mamífero", "Sabana africana")
elefante = Animal("Elefante", "mamífero", "Bosques de Asia")
cocodrilo = Animal("Cocodrilo", "reptil", "Ríos de América")
aguila = Animal("Águila", "ave", "Montañas rocosas")
print("Animales registrados:")
print(f"Mamífero: Nombre: {leon.especie} | Tipo: {leon.tipo} | Origen: {leon.origen} | Encontrado en: {leon.lugar}")
print(f"Mamífero: Nombre: {elefante.especie} | Tipo: {elefante.tipo} | Origen: {elefante.origen} | Encontrado en: {elefante.lugar}")
print(f"Mam+ifero: Nombre: {cocodrilo.especie} | Tipo: {cocodrilo.tipo} | Origen: {cocodrilo.origen} | Encontrado en: {cocodrilo.lugar}")
print(f"Mam+ifero: Nombre: {aguila.especie} | Tipo: {aguila.tipo} | Origen: {aguila.origen} | Encontrado en: {aguila.lugar}")