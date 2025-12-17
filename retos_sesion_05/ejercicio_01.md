Una empresa de transporte desea desarrollar una simulación que represente el comportamiento de sus distintos vehículos.
Todo vehículo posee las siguientes características:

velocidad: Es un dato protegido. Puede consultarse, pero solo modificarse mediante acciones específicas.
medio: Representa el entorno en el que se desplaza el vehículo (por ejemplo, terrestre, acuático, aéreo). Puede consultarse y modificarse libremente.
Existen dos tipos de vehículos con características específicas:

Bicicleta: Incrementar su velocidad mediante la acción de pedalear.
Avión: Incrementar su velocidad mediante la acción de volar.

## Análisis
Requisitos:
- El vehículo tiene velocidad y medio.
- La velocidad es protegida y medio es público.
- La Bicicleta debe pedalear para aumentar la velocidad.
- El Avión debe volar para aumentar la velocidad.

Objetos:
- Vehiculo (Clase Padre)
- Bicicleta (Hereda de Vehículo)
- Avion (Hereda de Vehículo)
  
Características:
- Vehiculo:
 - velocidad
 - medio

- Bicicleta y Avion: (No tienen atributos propios)
    
Acciones:
- Vehiculo:
  - get_velocidad()
- Bicicleta:
  - pedalear(incremento)
- Avion:
  - volar(incremento)
  
## Diseño:
Clases:
- Vehiculo:
  - Nombre: Vehiculo
  - Atributos:
    - velocidad
    - medio
  - Métodos:
    - get_velocidad()
  
- Bicicleta:
  - Nombre: Bicicleta
  - Atributos: No tienen atributos propios.
  - Métodos:
    - pedalear(incremento)

- Avion:
  - Nombre: Avion
  - Atributos: No tienen atributos propios.
  - Métodos:
    - volar(incremento)

```mermaid
classDiagram
    class Vehiculo {
        #velocidad: Int
        +medio: String
        get_velocidad()
    }
    class Bicicleta {
        +pedalear(incremento)
    }
    class Avion {
        +volar(incremento)
    }
    Vehiculo <|-- Bicicleta
    Vehiculo <|-- Avion