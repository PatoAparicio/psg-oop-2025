class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
    
    def __str__(self):
        return f"{self.nombre} (Destino: {self.destino})"

class Minibus:
    
    def __init__(self, numero_ruta, paradas_programadas: list):
        self.numero_ruta = numero_ruta
        self.__paradas_programadas = list(paradas_programadas)
        self.__pasajeros = []  
        self.__parada_actual_idx = 0
        self.__direccion_adelante = True 

    @property
    def parada_actual(self):
        if self.__paradas_programadas:
            return self.__paradas_programadas[self.__parada_actual_idx]
        return "Ruta Vacía"

    def __invertir_ruta(self):
        self.__direccion_adelante = not self.__direccion_adelante
        print(f"\nRuta {self.numero_ruta} invertida. Sentido: {'Adelante' if self.__direccion_adelante else 'Atrás'}")

    def subir_pasajero(self, pasajero: Pasajero):        
        if pasajero.destino in self.__paradas_programadas:
            self.__pasajeros.append(pasajero)
            print(f"{pasajero.nombre} subió en {self.parada_actual}. Destino: {pasajero.destino}")
            return True
        else:
            print(f"{pasajero.nombre} no puede subir. Destino {pasajero.destino} no está en la ruta.")
            return False

    def avanzar(self):
        if not self.__paradas_programadas:
            print("El minibús no tiene paradas definidas.")
            return

        pasajeros_a_bajar = []
        for p in self.__pasajeros:
            if p.destino == self.parada_actual:
                pasajeros_a_bajar.append(p)
        
        for p in pasajeros_a_bajar:
            self.__pasajeros.remove(p)
            print(f"⬇️ {p.nombre} bajó en {self.parada_actual} (Destino alcanzado).")

        if self.__direccion_adelante:
            siguiente_idx = self.__parada_actual_idx + 1
            es_final = siguiente_idx >= len(self.__paradas_programadas)
        else:
            siguiente_idx = self.__parada_actual_idx - 1
            es_final = siguiente_idx < 0
    
        if es_final:
            self.__invertir_ruta()
            if self.__direccion_adelante:
                 self.__parada_actual_idx = 1 
            else:
                self.__parada_actual_idx = len(self.__paradas_programadas) - 2 
        else:
            self.__parada_actual_idx = siguiente_idx

        print(f"\nRUTA {self.numero_ruta} | EN PARADA: {self.parada_actual} | A BORDO: {len(self.__pasajeros)}")
        if not self.__pasajeros:
             print("   (Minibus vacío)")


    def mostrar_pasajeros(self):
        if self.__pasajeros:
            print(f"\nPasajeros a bordo ({len(self.__pasajeros)}):")
            for p in self.__pasajeros:
                print(f"- {p}")
        else:
            print("\nNo hay pasajeros a bordo.")
            

RUTA = ["Arce", "Prado", "Perez", "Final de Ruta"]
minibus_401 = Minibus("401", RUTA)

pasajero_1 = Pasajero("Ana", "Prado")
pasajero_2 = Pasajero("Luis", "Final de Ruta")
pasajero_3 = Pasajero("Pedro", "Perez")
pasajero_invalido = Pasajero("Zoe", "Terminal")

print(f" RUTA {minibus_401.numero_ruta}")
print(f"Parada inicial: {minibus_401.parada_actual}") 

minibus_401.subir_pasajero(pasajero_1)
minibus_401.subir_pasajero(pasajero_2)
minibus_401.subir_pasajero(pasajero_invalido) 

minibus_401.avanzar()
minibus_401.subir_pasajero(pasajero_3)

minibus_401.avanzar()

minibus_401.avanzar() 
minibus_401.avanzar() 

minibus_401.avanzar() 

minibus_401.mostrar_pasajeros()