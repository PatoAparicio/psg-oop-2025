En la simulación de un bosque los arboles pueden crecer
tienen una especie y pueden ser frutales o no.
Nacen desde una semilla, y crecen con el tiempo
Cuando llegan a 10 metros de altura pueden dar frutos
Todos los arboles cuando tiene más de 15 metros mueren


# Análisis

Requisitos:
- Crear un árbol
- Lo árboles pueden crecer
- Los árboles tienen una especie
- Los árboles pueden ser frutales o no
- Los árboles nacen desde semillas y crecen con el tiempo.
- Los árboles pueden dar fruto
- Los árboles mueren

Objetos:
- árboles

Características:
- Árbol: especie, altura, frutal, vivo
   - 

Acciones:
- Árbol: nacer, crecer, dar_frutos, morir

```mermaid
classDiagram
    class Árbol {
        String especie
        float altura
        Bool frutal
        Bool vivo
        germinar(especie)
        crecer(altura)
        dar_frutos()
        morir (arbol)
    }