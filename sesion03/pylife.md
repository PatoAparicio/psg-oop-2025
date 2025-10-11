Crearemos un juego similar a Sims llamado `PyLife`
Las personas creadas tienen un nombre y
pueden saludar diciendo su nombre
Ahora las personas pueden dormir una cantidad de horas
En el juego ahora las personas pueden
tener hambre y comer para saciarla
Cuando duerme la persona despierta con hambre


# Análisis

Requisitos:
- Crear personas
- Las personas tienen un nombre
- Las personas pueden saludar
- Tiene un constructor que crea personas con nombre
- Las personas pueden dormir
- Las personas pueden comer
- Al despertar tienen hambre

Objetos:
- Persona

Características:
- Persona: Nombre, hambre

Acciones:
- Persona: Saludar, dormir, comer

```mermaid
classDiagram
    class Persona {
        String nombre
        bool hambre
        saludar()
        dormir(horas)
        comer(comida)
    }


    print ("======")
class Perro:
    factor_edad = 7 # Atributo de clase
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def ladrar(self): # Método de instancia
        print(f"{self.nombre} dice: ¡Guau!")

    def crecer(self, tiempo): # Método de instancia
        self.edad += tiempo
        print(f"{self.nombre} ha crecido {tiempo} años")

    @classmethod # Nuevo Método de clase
    def nacer(cls, nombre):
        print(f"{nombre} ha nacido como un cachorro")
        return cls(nombre,0)

    @classmethod # Nuevo Método de clase
    def edad_a_humano(cls, perro):
        print(f"En años humanos, {perro.nombre}")
        print(f"tiene {perro.edad * cls.factor_edad} años")

rex = Perro.nacer("Rex")
rex.ladrar()
rex.crecer(2)
rex.crecer(2)
Perro.edad_a_humano(rex)