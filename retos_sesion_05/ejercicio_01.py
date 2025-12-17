class Vehiculo:
    def __init__(self, medio, velocidad_inicial=0):
        self.medio = medio 
        self._velocidad = velocidad_inicial
    
    @property
    def velocidad(self):
        return self._velocidad

class Bicicleta(Vehiculo):
    def __init__(self, medio="terrestre", velocidad_inicial=0):
        super().__init__(medio, velocidad_inicial)
        
    def pedalear(self, incremento):
        self._velocidad += incremento
        print(f"Bicicleta pedaleando. Velocidad: {self.velocidad} km/h")

class Avion(Vehiculo):
    def __init__(self, medio="aéreo", velocidad_inicial=0):
        super().__init__(medio, velocidad_inicial)
        
    def volar(self, incremento):
        self._velocidad += incremento * 10
        print(f"Avión volando. Velocidad: {self.velocidad} km/h")


bici = Bicicleta()
avion = Avion()

print(f"Bicicleta:  Medio: {bici.medio}, Velocidad Inicial: {bici.velocidad}")
bici.pedalear(15)
bici.pedalear(5)

print("-" * 20)
print(f"Avión: Medio: {avion.medio}, Velocidad Inicial: {avion.velocidad}")
avion.volar(5)
avion.volar(10)

bici.medio = "asfalto"
print(f"Medio de Bicicleta actualizado: {bici.medio}") 
