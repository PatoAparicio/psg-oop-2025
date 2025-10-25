Una empresa de transporte desea desarrollar una simulación que represente el comportamiento de sus distintos vehículos.
Todo vehículo posee las siguientes características:

velocidad: Es un dato protegido. Puede consultarse, pero solo modificarse mediante acciones específicas.
medio: Representa el entorno en el que se desplaza el vehículo (por ejemplo, terrestre, acuático, aéreo). Puede consultarse y modificarse libremente.
Existen dos tipos de vehículos con características específicas:

Bicicleta: Incrementar su velocidad mediante la acción de pedalear.
Avión: Incrementar su velocidad mediante la acción de volar.


Requisitos:
- Simulación que represente el comportamiento de vehículos.
- Velocidad es un dato protegido (solo se consulta directamente; se modifica mediante acciones específicas).
- Medio es público (se consulta y se modifica libremente).
- La Bicicleta incrementa su velocidad mediante la acción de pedalear.
- El Avión incrementa su velocidad mediante la acción de volar.

Objetos:
- Vehiculo (Clase Padre)
- Bicicleta (Hereda de Vehículo)
- Avion (Hereda de Vehículo)
  
Características:
- Vehiculo:
 - velocidad: Float
 - medio: String

- Bicicleta y Avion: (No tienen atributos propios)
    
Acciones:
- Vehiculo:
 - velocidad 
 - medio
- Bicicleta:
 - pedalear(esfuerzo)
- Avion:
 - volar(empuje)
  
```mermaid
classDiagram
    class Vehiculo {
        +velocidad : float 
        +medio : str
        #_incrementar_velocidad(incremento) : void
    }
    
    class Bicicleta {
        +pedalear(esfuerzo) : str
    }
    
    class Avion {
        +volar(empuje) : str
    }
