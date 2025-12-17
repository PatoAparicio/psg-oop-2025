En su trayecto diario al trabajo, las personas pueden abordar distintos minibuses. Cada minibus está identificado por un número de ruta y sigue un recorrido compuesto por varias paradas (ubicaciones). Por otro lado, cada pasajero tiene un nombre y una ubicación de destino a la que desea llegar.
Los pasajeros pueden subir o bajar del minibus en cualquier parada, pero bajo las siguientes condiciones:
Un pasajero solo puede subir si el recorrido del minibus incluye su destino entre las paradas programadas.
Un pasajero solo puede bajar si la parada actual del minibus coincide con su destino.
Las paradas son circulares: al llegar al final del recorrido, el minibus invierte su lista de paradas y regresa en sentido contrario.
Diseñar las clases necesarias para representar Minibus y Pasajero.
Toma en cuenta las siguientes características:Un minibus tiene una lista de paradas programadas (ejemplo: ["Arce", "Prado", "Perez"]).
Un minibus puede transportar múltiples pasajeros.
Simular el movimiento del minibus entre paradas y las acciones de subida y bajada de pasajeros.

## Análisis
Requisitos:
- Un minibús debe registrar un número de ruta y una lista de paradas programadas
- Un pasajero debe registrar un nombre y un destino.
- El minibús se mueve entre paradas (avanzar) y la inversión de ruta (ruta circular).
- Un pasajero solo puede subir si su destino está en las paradas programadas.
- Un pasajero solo puede bajar si la parada actual del minibús coincide con su destino.

Objetos:
- Pasajero
- Minibus

Características:
- Minibus:
 - ruta (int)
 - paradas_programadas (list de str)
 - pasajeros_a_bordo (list de Pasajero)

- Pasajero:
 - nombre: String
 - destino: String

Acciones:
- Minibus:
 - mostrar_pasajeros()
 - avanzar()
 - subir_pasajero(pasajero)
  
- Pasajero: (No tiene acciones)
  
## Diseño:
Clases:
- Minibus:
  - Nombre: Minibus
  - Atributos:
    - ruta (int)
    - paradas_programadas (list de str)
    - pasajeros_a_bordo 
  - Métodos:
    -  mostrar_pasajeros()
    - avanzar()
    - subir_pasajero(pasajero)
  
- Pasajero::
  - Nombre: Pasajero:
  - Atributos: 
    - nombre: String
    - destino: String
  - Métodos:
    - (No tiene acciones)


```mermaid
classDiagram
   class Pasajero {
        +nombre: String
        +destino: String
    }
    class Minibus {
        +numero_ruta: String
        -paradas_programadas: List[String]
        -pasajeros: List[Pasajero]
        -parada_actual_idx: int
        -direccion_adelante: bool
        +subir_pasajero(pasajero: Pasajero)
        +avanzar()
        +mostrar_pasajeros()
        -invertir_ruta()
    }
    
    Minibus o-- Pasajero
