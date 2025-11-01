En su trayecto diario al trabajo, las personas pueden abordar distintos minibuses. Cada minibus está identificado por un número de ruta y sigue un recorrido compuesto por varias paradas (ubicaciones). Por otro lado, cada pasajero tiene un nombre y una ubicación de destino a la que desea llegar.
Los pasajeros pueden subir o bajar del minibus en cualquier parada, pero bajo las siguientes condiciones:
Un pasajero solo puede subir si el recorrido del minibus incluye su destino entre las paradas programadas.
Un pasajero solo puede bajar si la parada actual del minibus coincide con su destino.
Las paradas son circulares: al llegar al final del recorrido, el minibus invierte su lista de paradas y regresa en sentido contrario.
Diseñar las clases necesarias para representar Minibus y Pasajero.
Toma en cuenta las siguientes características:Un minibus tiene una lista de paradas programadas (ejemplo: ["Arce", "Prado", "Perez"]).
Un minibus puede transportar múltiples pasajeros.
Simular el movimiento del minibus entre paradas y las acciones de subida y bajada de pasajeros.

Requisitos:
- Minibus tiene un número de ruta y una lista de paradas.
- Pasajero tiene un nombre y una ubicación de destino.
- El destino del pasajero debe estar en el recorrido programado del Minibus.
- La parada actual del Minibus debe coincidir con el destino del pasajero.
- Al llegar al final de las paradas, el Minibus invierte su lista de paradas para regresar.

Objetos:
- Pasajero
- Minibus

Características:
- Pasajero:
 - nombre: String
 - destino: String

- Minibus:
 - ruta (int)
 - paradas_programadas (list de str)
 - pasajeros_a_bordo (list de Pasajero)
 - parada_actual (int)
 - direccion_recorrido (int)
    
Acciones:
- Minibus:
 - mostrar_ubicacion()
 - parada_actual()
 - recorrido()
 - subir_pasajero(pasajero)
 - bajar_pasajero()
  
```mermaid
classDiagram
    class Pasajero {
        -nombre : str
        -destino : str
    }

    class Minibus {
        -ruta : int
        -paradas_programadas : list<str>
        -pasajeros_a_bordo : list<Pasajero>
        -direccion_recorrido : int
        +parada_actual() : str
        +recorrido() : str
        +mostrar_estado() : str
        +subir_pasajero(pasajero) : str
        +bajar_pasajero() : str
        +obtener_ubicacion() : str
        
    }
    
    Minibus o-- Pasajero 
