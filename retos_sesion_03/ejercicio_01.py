class atleta:
    energia_hamburguesa = 20
    fuerza_entrenamiento = 5
    energia_entrenamiento = 15
    energia_descansar = 30
    def __init__(self, nombre, energia, fuerza, ):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza

    def entrenar(self):
        self.fuerza += self.fuerza_entrenamiento
        print(f"El Atleta {self.nombre} entrenó tiene la fuerza de: {self.fuerza} ")
        self.energia -= self.energia_entrenamiento
        print(f"El Atleta {self.nombre} entrenó tiene la energia de: {self.energia} ")

    
    def comer(self): 
        self.energia += self.energia_hamburguesa
        print(f"El Atleta {self.nombre} comió tiene la energia de: {self.energia} ")
    
    def descansar(self):
        self.energia += self.energia_descansar
        print(f"El Atleta {self.nombre} descansó tiene la energia de: {self.energia} ")
    

# Instanciar atleta
atleta1 = atleta("Marco", 80, 50)
atleta2 = atleta("Rita", 40, 65)

atleta1.entrenar() 
atleta1.descansar()
atleta1.comer()

atleta2.entrenar() 
atleta2.descansar()
atleta2.comer()
