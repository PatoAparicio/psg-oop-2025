class BeatBox:
    __instancia = None
    efecto_disponibles = ("eco", "reverb", "distorsión")
 
    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.pista_actual = "Ninguna pista cargada"
            cls.__instancia.volumen = 0
            cls.__instancia.efecto_activo = "Ninguno"
            print("Bienvenidos a la Consola BeatBox")
        return cls.__instancia

    def seleccionar_pista(self, nombre_pista):
        self.pista_actual = nombre_pista
        print(f"Pista cargada: '{nombre_pista}'.")

    def ajustar_volumen(self, accion):
        accion = accion.lower()
        
        if accion == 'subir':
            self.volumen = self.volumen + 1
        elif accion == 'bajar':
            self.volumen =(self.volumen - 1)
        else:
            print("Acción de volumen no válida.")
            return

        print(f"Nivel actual: {self.volumen}.")
        
    def aplicar_efecto(self, efecto):
        efecto = efecto.lower()
        if efecto in self.efecto_disponibles:
            self.efecto_activo = efecto
            print(f"Efecto aplicado: {efecto}.")
        else:
            print(f"Efecto inválido.")
        

    def mostrar_estado(self):
        print(f"ESTADO ACTUAL DE BEATBOX")
        print(f"Pista: {self.pista_actual}")
        print(f"Volumen: {self.volumen}")
        print(f"Efecto: {self.efecto_activo}")


def obtener_input(mensaje):
    return input(mensaje)


consola = BeatBox()

while True:
        print("\nMenú de Consola BeatBox")
        print("1. Ingresar Pista de Audio")
        print("2. Ajustar Volumen (Subir/Bajar)")
        print("3. Aplicar Efecto de Sonido")
        print("4. Mostrar Estado Actual")
        print("5. Salir")
        
        opcion = obtener_input("Elige una opción (1-5): ")
        
        if opcion == '1':
            nombre = obtener_input("Ingresa el nombre de la pista: ")
            consola.seleccionar_pista(nombre)
        
        elif opcion == '2':
            accion = obtener_input("Ajustar: ¿subir o bajar volumen?: ")
            consola.ajustar_volumen(accion)
            
        elif opcion == '3':
            print(f"Opciones: eco, reverb, distorsión")
            efecto = obtener_input("Ingresa el efecto a aplicar: ")
            consola.aplicar_efecto(efecto)
            
        elif opcion == '4':
            consola.mostrar_estado()
            
        elif opcion == '5':
            print("\nConsola BeatBox apagada.")
            break
            
        else:
            print("Opción inválida. Seleccione un número del 1 al 5.")