class Instrumento:
    def __init__(self, nombre: str):
        self._nombre = nombre
        
    def tocar(self) -> str:
        return f"El {self._nombre} está siendo tocado."

    def info(self) -> str:
        return f"Instrumento: {self._nombre}"

class Guitarra(Instrumento):
    def __init__(self, numero_cuerdas: int, tipo_madera: str):
        super().__init__("Guitarra")
        self._numero_cuerdas = numero_cuerdas
        self._tipo_madera = tipo_madera
        
    def tocar(self) -> str:
        return "¡STRUM!"

    def info(self) -> str:
        return f"{super().info()} | Cuerdas: {self._numero_cuerdas} | Madera: {self._tipo_madera}"

class Piano(Instrumento):
    def __init__(self, numero_teclas: int, tipo_piano: str):
        super().__init__("Piano")
        self._numero_teclas = numero_teclas
        self._tipo_piano = tipo_piano 
        
    def tocar(self) -> str:
        return "¡PLIN!"

    def mostrar_info(self) -> str:
        return f"{super().info()} | Teclas: {self._numero_teclas} | Tipo: {self._tipo_piano}"

class Tambor(Instrumento):
    def __init__(self, tipo_percusion: str, material_parche: str):
        super().__init__("Tambor")
        self._tipo_percusion = tipo_percusion
        self._material_parche = material_parche
        
    def tocar(self) -> str:
        return "¡BOOM!"

    def mostrar_info(self) -> str:
        return f"{super().info()} | Percusión: {self._tipo_percusion} | Parche: {self._material_parche}"

def usuario(instrumento: Instrumento):
    print(f"Usuario practica: {instrumento.info()}")
    sonido = instrumento.tocar()
    print(f"El instrumento suena: {sonido}")

print("Aprendiendo a tocar instrumentos musicales:")

guitarra = Guitarra(numero_cuerdas=6, tipo_madera="Caoba")
piano = Piano(numero_teclas=88, tipo_piano="Acústico de Cola")
tambor = Tambor(tipo_percusion="Redoblante", material_parche="Mylar")

usuario(guitarra)
usuario(piano)
usuario(tambor)


