from typing import List

class Pasajero:
    def __init__(self, nombre: str, destino: str):
        self.nombre = nombre
        self.destino = destino

class Minibus:
    def __init__(self, ruta: int, paradas_programadas: List[str]):
        self.ruta = ruta
        self.paradas_programadas = paradas_programadas
        self.pasajeros_a_bordo: List[Pasajero] = []
        
        self.parada_actual = 0
        self.direccion_recorrido = 1 
        
        print(f"Ruta {self.ruta} inicia en: {self.obtener_ubicacion()}")

    def obtener_ubicacion(self) -> str:
        return self.paradas_programadas[self.parada_actual]

    def _cambiar_direccion(self):
        self.direccion_recorrido *= -1
        direccion_str = "Regreso" if self.direccion_recorrido == -1 else "Ida"
        print(f"¡La ruta {self.ruta} está de {direccion_str}!")
        
    def avanzar(self) -> str:
        max_idx = len(self.paradas_programadas) - 1

        if (self.direccion_recorrido == 1 and self.parada_actual == max_idx) or \
           (self.direccion_recorrido == -1 and self.parada_actual == 0):
            self._cambiar_direccion()
   
        parada_anterior = self.obtener_ubicacion()
        self.parada_actual += self.direccion_recorrido
        
        return f"\nMinibus avanza de '{parada_anterior}' a '{self.obtener_ubicacion()}'."

    def subir_pasajero(self, pasajero: Pasajero) -> str:
        if pasajero.destino in self.paradas_programadas:
            self.pasajeros_a_bordo.append(pasajero)
            return f"{pasajero.nombre} subió en {self.obtener_ubicacion()}. Destino: {pasajero.destino}."
        else:
            return f"{pasajero.nombre} no puede subir. Destino {pasajero.destino} que no está en la Ruta {self.ruta}."

    def bajar_pasajero(self) -> str:
        parada_actual = self.obtener_ubicacion()
        pasajeros_bajan = []
        pasajeros_quedan = []
       
        for p in self.pasajeros_a_bordo:
            if p.destino == parada_actual:
                pasajeros_bajan.append(p.nombre)
            else:
                pasajeros_quedan.append(p) 
        self.pasajeros_a_bordo = pasajeros_quedan
        
        if pasajeros_bajan:
            nombres = ', '.join(pasajeros_bajan)
            return f"⬇{len(pasajeros_bajan)} pasajero(s) bajan en '{parada_actual}': {nombres}."
        else:
            return f"Nadie baja en '{parada_actual}'."

    def mostrar_estado(self) -> str:
        nombres_a_bordo = [p.nombre for p in self.pasajeros_a_bordo]
        pasajeros = ", ".join(nombres_a_bordo) if nombres_a_bordo else "Ninguno"
        return f"Parada: {self.obtener_ubicacion()} | Pasajeros a bordo ({len(self.pasajeros_a_bordo)}): {pasajeros}"

print("Minibús 865:")
ruta_principal = ["Arce", "Prado", "Perez", "Autopista", "Ceja"]
minibus_865 = Minibus(ruta=865, paradas_programadas=ruta_principal)

print("Pasajeros en el camino:")
p1 = Pasajero("Ana", "Perez")
p2 = Pasajero("Beto", "Autopista")
p3 = Pasajero("David", "Villa Adela")

print(p1.nombre + " quiere subir en la parada " + minibus_865.obtener_ubicacion() + " con destino a " + p1.destino)
print(p2.nombre + " quiere subir en la parada " + minibus_865.obtener_ubicacion() + " con destino a " + p2.destino)
print(p3.nombre + " quiere subir en la parada " + minibus_865.obtener_ubicacion() + " con destino a " + p3.destino)

print(minibus_865.subir_pasajero(p1)) 
print(minibus_865.subir_pasajero(p2)) 
print(minibus_865.subir_pasajero(p3)) 

print("\nRecorrido del minibús 865:")

print(minibus_865.avanzar())
print(minibus_865.bajar_pasajero())
print(minibus_865.mostrar_estado())

print(minibus_865.avanzar())
print(minibus_865.bajar_pasajero())
print(minibus_865.mostrar_estado())

print(minibus_865.avanzar())
print(minibus_865.bajar_pasajero())

print(minibus_865.avanzar())
print(minibus_865.bajar_pasajero())
print(minibus_865.mostrar_estado())

print(minibus_865.avanzar())
print(minibus_865.mostrar_estado())