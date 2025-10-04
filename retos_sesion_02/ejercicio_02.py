class Vino:
    def __init__(self, nombre, tipo, cepa, año_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.año_produccion = año_produccion

class Queso:
    def __init__(self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad  
        self.sal = sal

# Instanciar vinos
vino1 = Vino("Malbec Reserve", "Tinto", "Malbec", 2020)
vino2 = Vino("Chardonnay Premium", "Blanco", "Chardonnay", 2021)
vino3 = Vino("Cabernet Sauvignon", "Tinto", "Cabernet Sauvignon", 2019)
vino4 = Vino("Rosé Fresco", "Rosado", "Garnacha", 2022)

# Instanciar quesos
queso1 = Queso("Manchego", "Ovino", 12, True)
queso2 = Queso("Brie", "Blando", 3, False)
queso3 = Queso("Gouda Ahumado", "Semi-duro", 6, True)

print("VINOS:")
print("Vino 1: ",vino1.nombre, vino1.tipo, vino1.cepa, vino1.año_produccion)
print("Vino 2: ",vino2.nombre, vino2.tipo, vino2.cepa, vino2.año_produccion)
print("Vino 3: ",vino3.nombre, vino3.tipo, vino3.cepa, vino3.año_produccion)
print("Vino 4: ",vino4.nombre, vino4.tipo, vino4.cepa, vino4.año_produccion)

print("QUESOS:")
print("Queso 1: ",queso1.nombre, queso1.variedad, queso1.edad, queso1.sal)
print("Queso 2: ",queso2.nombre, queso2.variedad, queso2.edad, queso2.sal)
print("Queso 3: ",queso3.nombre, queso3.variedad, queso3.edad, queso3.sal)