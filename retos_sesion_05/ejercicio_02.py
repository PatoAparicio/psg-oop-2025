class Nadador:
    def nadar(self) -> str:
        return "Desplazamiento en el agua."

class Volador:
    def volar(self) -> str:
        return "Desplazamiento en el aire."

class Pez(Nadador):
    def mostrar(self) -> str:
        habilidades = [self.nadar()]
        return f"Tipo: Pez\n   Habilidad principal: {habilidades[0]}"

class Pajaro(Volador):
    def mostrar(self) -> str:
        habilidades = [self.volar()]
        return f"Tipo: Pájaro\n   Habilidad principal: {habilidades[0]}"

class Pato(Nadador, Volador):
    def mostrar(self) -> str:
        habilidades = [self.nadar(), self.volar()]
        return f"Tipo: Pato\n   Habilidades: \n   1. {habilidades[0]}\n   2. {habilidades[1]}"

print("DEMOSTRACIÓN DE HABILIDADES")

pez = Pez()
pajaro = Pajaro()
pato = Pato()


print(" PEZ")
print(f"Pez acción: {pez.nadar()}\n")
print(pez.mostrar())


print("PÁJARO")
print(f"Pájaro acción: {pajaro.volar()}\n")
print(pajaro.mostrar())


print(" PATO")
print(f"Pato nadando: {pato.nadar()}")
print(f"Pato volando: {pato.volar()}")
print(pato.mostrar())


