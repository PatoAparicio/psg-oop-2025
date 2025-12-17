class Nadador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def nadar(self):
        print(f"{self.nombre} está nadando.")

class Volador:
    def __init__(self, nombre):
        self.nombre = nombre

    def volar(self):
        print(f"{self.nombre} está volando.")


class Pez(Nadador):
    def mostrar(self):
        print(f"\nPersonaje: {self.nombre} (Pez)")
        self.nadar()
        print("Habilidades: Nadar")

class Pajaro(Volador):
    def mostrar(self):
        print(f"\nPersonaje: {self.nombre} (Pájaro)")
        self.volar()
        print("Habilidades: Volar")

class Pato(Nadador, Volador):
    def __init__(self, nombre):
        Nadador.__init__(self, nombre)
        Volador.__init__(self, nombre) 
        
    def mostrar(self):
        print(f"\nPersonaje: {self.nombre} (Pato)")
        self.nadar()
        self.volar()
        print("Habilidades: Nadar y Volar")


pez = Pez("Nemo")
pajaro = Pajaro("Tito")
pato = Pato("Donald")

pez.mostrar()
pajaro.mostrar()
pato.mostrar()

