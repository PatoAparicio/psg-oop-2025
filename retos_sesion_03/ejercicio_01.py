class atleta:
    def __init__(self, nombre, energia, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza
        print(f"Atleta: Nombre: {self.nombre} | Energia actual: {self.energia} | Fuerza actual: {self.fuerza} ")

    def entrenar(self, energia_gastada, fuerza_ganada):
        self.fuerza += fuerza_ganada
        print(f"El Atleta {self.nombre} entrenó, gastó {energia_gastada} de energía y ganó {fuerza_ganada} de fuerza ")
        self.energia -= energia_gastada
        print(f"El Atleta {self.nombre} entrenó, tiene la energia actual de {self.energia} y la fuerza actual de {self.fuerza} ")

    
    def comer(self, cantidad_hamburguesa, energia_ganada): 
        self.energia += energia_ganada
        print(f"El Atleta {self.nombre} comió {cantidad_hamburguesa} hamburguesas y tiene la energia de {self.energia} ")
    
    def descansar(self, energia_recuperada):
        self.energia += energia_recuperada
        print(f"El Atleta {self.nombre} descansó y recuperó {energia_recuperada} de energía tiene la energia de {self.energia} ")
    

# Instanciar atleta
atleta_1 = atleta("Marco", 80, 50)
atleta_1.entrenar(10,20) 
atleta_1.descansar(10)
atleta_1.comer(8,50)

atleta_2 = atleta("Rita", 40, 65)
atleta_2.entrenar(100, 50) 
atleta_2.descansar(20)
atleta_2.comer(1,20)
