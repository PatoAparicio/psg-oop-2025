import random

class PiedraPapelTijera:
    __instancia = None
    opciones = ("piedra", "papel", "tijera")

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.puntaje_jugador = 0
            cls.__instancia.puntaje_computadora = 0
        return cls.__instancia

    def iniciarPartida(self):
        opcion_computadora = random.choice(self.opciones)
        print(f"¡Juego Piedra, Papel o Tijera iniciado!")
        print("\nSelecciona tu jugada:")
        print("piedra")
        print("papel")
        print("tijera")
        opcion_jugador = input("Tu elección: ")
        if opcion_jugador not in self.opciones:
            print("Opción inválida. Intente de nuevo.")

        print(f"\nJugador elige: {opcion_jugador}")
        print(f"Computadora elige: {opcion_computadora}")

        if opcion_jugador == opcion_computadora:
            print("¡Empate!")

        elif (opcion_jugador == "piedra" and opcion_computadora == "tijera") or \
             (opcion_jugador == "papel" and opcion_computadora == "piedra") or \
             (opcion_jugador == "tijera" and opcion_computadora == "papel"):
            self.puntaje_jugador += 1
            print("¡Ganaste!")

        else:
            self.puntaje_computadora += 1
            
        self.mostrarPuntaje() 
            
    def mostrarPuntaje(self):
        print(f"\n Puntaje Actual")
        print(f"Jugador: {self.puntaje_jugador}")
        print(f"Computadora: {self.puntaje_computadora}")


    def reiniciarJuego(self):
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        print("\nEl juego ha sido reiniciado y el puntaje es cero.")
        self.mostrarPuntaje()

juego = PiedraPapelTijera()
while True:
    print("\nMenú Principal")
    print("1. Iniciar una nueva partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar el juego")
    print("4. Salir")
        
    opcion = input("Elige una opción (1-4): ")
        
    if opcion == '1':
        juego.iniciarPartida()
       
    elif opcion == '2':
        juego.mostrarPuntaje()
            
    elif opcion == '3':
        juego.reiniciarJuego()
            
    elif opcion == '4':
        print("\n¡Hasta pronto!")
        break
          
    else:
       print("Opción no válida.")