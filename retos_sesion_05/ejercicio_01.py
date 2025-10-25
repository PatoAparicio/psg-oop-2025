class Vehiculo:
    def __init__(self, medio: str, velocidad: float = 0.0):
        self._velocidad = velocidad 
        self._medio = medio

    @property
    def velocidad(self) -> float:
        return self._velocidad

    @property
    def medio(self) -> str:
        return self._medio

    @medio.setter
    def medio(self, nuevo_medio: str):
        if isinstance(nuevo_medio, str):
            self._medio = nuevo_medio
        else:
            print("Agregue el medio de desplazamiento.")

    def _incrementar_velocidad(self, incremento: float):
        self._velocidad += incremento
        return f"Velocidad incrementada en {incremento:.1f} km/h."

class Bicicleta(Vehiculo):
    def __init__(self, velocidad: float = 0.0):
        super().__init__("Terrestre", velocidad)
        print(f"Medio: {self.medio}  Velocidad: {self.velocidad:.1f} km/h")

    def pedalear(self, incremento: float) -> str:
        velocidad_actual = self._incrementar_velocidad(incremento)
        return f"Pedaleando, aumentó la velocidad en {self.velocidad:.1f} km/h."


class Avion(Vehiculo):
    def __init__(self, velocidad: float = 0.0):
        super().__init__("Aéreo", velocidad)
        print (f"Medio: {self.medio}  Velocidad: {self.velocidad:.1f} km/h")

    def volar(self, incremento: float) -> str:
        velocidad_actual = self._incrementar_velocidad(incremento)
        return f"Se aumentó la velocidad en {self.velocidad:.1f} km/h."
print("\nIniciación Bicicleta")
bici = Bicicleta(10.0)
print("\nIniciación Avión")
avion = Avion(100.0)
print("\nModificación de Velocidad")
print(bici.pedalear(2.5)) 
print(bici.pedalear(1.0))

print(avion.volar(10.0)) 
print(avion.volar(5.0)) 
print("\nModificación Medio de Desplazamiento")
print(f"Medio inicial de la bicicleta: {bici.medio}")
bici.medio = "Marítimo" 
print(f"Nuevo medio de la bicicleta: {bici.medio}")
