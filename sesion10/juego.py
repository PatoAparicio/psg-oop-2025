class Arma:
    def atacar(self):
        print("Atacando con un arma")

class Espada(Arma):
    def atacar(self):
        print("🗡️ Atacando con una espada")

class Arco(Arma):
    def atacar(self):
        print("🏹 Atacando con un arco")

class Herramienta:
    def fabricar(self):
        pass

class Martillo(Herramienta):
    def fabricar(self):
        return Espada()

class Sierra(Herramienta):
    def fabricar(self):
        return Arco()
    
class Armero:
    def fabricar_arma(self, tipo):
        if tipo == "espada":
            return Martillo().fabricar()
        if tipo == "arco":
            return Sierra().fabricar()
        raise ValueError("❌ Arma no disponible. Intente de nuevo")