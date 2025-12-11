class Vino:
    def __init__(self, nombre, tipo, cepa, anio_produccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.anio_produccion = anio_produccion

class Queso:
    def __init__(self, nombre, variedad, edad, lleva_sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad  
        self.lleva_sal = lleva_sal

# Instanciar vinos
vino_1 = Vino("Malbec Reserve", "Tinto", "Malbec", 2020)
vino_2 = Vino("Chardonnay Premium", "Blanco", "Chardonnay", 2021)
vino_3 = Vino("Cabernet Sauvignon", "Tinto", "Cabernet Sauvignon", 2019)
vino_4 = Vino("Rosé Fresco", "Rosado", "Garnacha", 2022)

# Instanciar quesos
queso_1 = Queso("Manchego", "Ovino", 12, True)
queso_2 = Queso("Brie", "Blando", 3, False)
queso_3 = Queso("Gouda Ahumado", "Semi-duro", 6, True)

print("VINOS:")
print(f"Nombre: {vino_1.nombre} | Tipo: {vino_1.tipo} | Cepa: {vino_1.cepa} | Año: {vino_1.anio_produccion}")
print(f"Nombre: {vino_2.nombre} | Tipo: {vino_2.tipo} | Cepa: {vino_2.cepa} | Año: {vino_2.anio_produccion}")
print(f"Nombre: {vino_3.nombre} | Tipo: {vino_3.tipo} | Cepa: {vino_3.cepa} | Año: {vino_3.anio_produccion}")
print(f"Nombre: {vino_4.nombre} | Tipo: {vino_4.tipo} | Cepa: {vino_4.cepa} | Año: {vino_4.anio_produccion}")

print("QUESOS:")
print(f"Nombre: {queso_1.nombre} | Variedad: {queso_1.variedad} | Edad (meses): {queso_1.edad} | Con Sal: {queso_1.lleva_sal}")
print(f"Nombre: {queso_2.nombre} | Variedad: {queso_2.variedad} | Edad (meses): {queso_2.edad} | Con Sal: {queso_2.lleva_sal}")
print(f"Nombre: {queso_3.nombre} | Variedad: {queso_3.variedad} | Edad (meses): {queso_3.edad} | Con Sal: {queso_3.lleva_sal}")