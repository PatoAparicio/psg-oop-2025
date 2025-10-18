class Celula:
    costo_division = 50.0
    def __init__(self, adn: str, tipo_celula: str, energia_inicial: float):
        self._adn = adn 
        self._energia = max(0.0, energia_inicial) 
        self.tipo = tipo_celula 
        
        print(f"Célula '{self.tipo}' . ADN: {self._adn[:5]} .Energía inicial: {self._energia:.1f}.")

    def comer(self, alimento: str) -> str:
            self._energia +=alimento
            return f"Célula comió {alimento}. Energía actual: {self._energia:.1f}"


    def dividirse(self) -> str:
        if self._energia >= self.costo_division:
            self._energia -= self.costo_division
            nueva_celula = Celula(self._adn, self.tipo, self._energia / 2.0)
            self._energia /= 2.0
            
            return f"Célula se ha dividido exitosamente. Energía: -{self.costo_division:.1f} (Costo) y repartida. Energía actual: {self._energia:.1f}\n"f"Célula hija: Tipo '{nueva_celula.tipo}', Energía inicial {nueva_celula._energia:.1f}."
        else:
            return f"No hay suficiente energía para dividirse. Se necesita {self.costo_division:.1f} y solo tiene {self._energia:.1f}."

    @property
    def adn(self) -> str:
        return self._adn

    @property
    def energia(self) -> float:
        return self._energia

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo: str):
        self._tipo = nuevo_tipo

print("Inicialización de Célula ")
celula_madre = Celula("ATCGGCTAAG", "Epitelial", 40.0)

print(f"ADN de la célula: {celula_madre.adn}")
print(f"Energía actual: {celula_madre.energia:.1f}")
print("Alimentación de célula:")
print(celula_madre.comer(50))
print("División de célula:")
print(celula_madre.dividirse())


print("Cambio de tipo de célula:")
print(f"Tipo actual: {celula_madre.tipo}")

celula_madre.tipo = "Neurona"
print(f"Nuevo tipo: {celula_madre.tipo}")
