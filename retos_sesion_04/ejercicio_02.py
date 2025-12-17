class Celula:
    def __init__(self, adn, tipo_celula, energia):
        self.__adn = adn 
        self.__energia = max(0.0, energia) 
        self.__tipo_celula = tipo_celula 
        
        print(f"Célula '{self.__tipo_celula}' . ADN: {self.__adn[:5]} .Energía inicial: {self.__energia:.1f}.")

    @property
    def adn(self):
        return self.__adn

    @property
    def energia(self):
        return self.__energia

    @property
    def tipo_celula(self):
        return self.__tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        self.__tipo_celula = nuevo_tipo
        print(f"Tipo de célula actualizado a: {nuevo_tipo}")

    def comer(self, cantidad):
        self.__energia += cantidad
        print(f"La célula come. Energía actual: {self.__energia}")

    def dividirse(self, costo):
        if self.__energia >= costo:
            self.__energia -= costo
            print(f"La célula se divide. Costo: {costo}. Energía restante: {self.__energia}")
            return True
        else:
            print(f"División fallida: Energía insuficiente ({self.__energia}).")
            return False

print("--- Creando una Célula ---")
celula = Celula("ATGC", "Epitelial", 100)
print(f"ADN inicial: {celula.adn}")
print(f"Tipo inicial: {celula.tipo_celula}")
print(f"Energía inicial: {celula.energia}")

print("\n--- Modificando Tipo de Célula ---")
celula.tipo_celula = "Neuronal" 
print(f"Tipo actualizado: {celula.tipo_celula}")
print("\n--- Modificando Energía ---")
celula.comer(50) 
celula.dividirse(30) 
celula.dividirse(200) 