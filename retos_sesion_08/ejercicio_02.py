class Destino:
    def __init__(self, nombre, costo):
        self.nombre = str(nombre)
        self.costo = float(costo)

    def __str__(self):
        return f"{self.nombre} ➡ {self.costo} USD"

    def __repr__(self):
        return f"[{self.destino}] ➡ [{self.costo}] USD"

class Catalogo:
    def __init__(self):
        self.destinos = []

    def __str__(self):
        resultado = ["🗺 Destinos 🗺"]
        i = 1
        for destino in self.destinos:
            resultado.append(f"{i}. {destino}")
            i += 1
        return "\n".join(resultado)

    def __len__(self):
        return len(self.destinos)

    def __getitem__(self, indice):
        return self.destinos[indice]

    def __setitem__(self, indice, valor):
        self.destinos[indice] = valor

    def __delitem__(self, indice):
        del self.destinos[indice]

    def __iter__(self):
        return iter(self.destinos)
 
catalogo = Catalogo()
catalogo.destinos.append(Destino("Colombia", 850.0))
catalogo.destinos.append(Destino("Ecuador", 900.0))
catalogo.destinos.append(Destino("Uruguay", 1000.0))
catalogo.destinos.append(Destino("Chile", 800.0))
print(catalogo)
print("\nLongitud del catálogo:", len(catalogo))
print("Destino en índice 1:", catalogo[0])
catalogo[1] = Destino("Ecuador", 1100.0)
print("\nDespués de modificar Ecuador:")
print(catalogo)
del catalogo[0]
print("\nDespués de eliminar Colombia:")
print(catalogo)
print("\nIterando sobre destinos:")
for destino in catalogo:
    print(destino)
