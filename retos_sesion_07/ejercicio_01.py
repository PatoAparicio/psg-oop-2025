class Martillo:
    def __init__(self, peso: float, material_cabeza: str):
        self._peso = peso 
        self._material_cabeza = material_cabeza
    
    def usar(self) -> str:
        return f"Martillo de ({self._material_cabeza}) utilizado para CLAVAR."
    
    def info(self) -> str:
        return f"Martillo | Peso: {self._peso} kg | Material: {self._material_cabeza}"

class Destornillador:
    def __init__(self, tipo_punta: str, material_mango: str):
        self._tipo_punta = tipo_punta
        self._material_mango= material_mango
    
    def usar(self) -> str:
        return f"Destornillador {self._tipo_punta} utilizado para AJUSTAR tornillos."
        
    def info(self) -> str:
        return f"Destornillador | Punta: {self._tipo_punta} | material del mango: {self._material_mango}"

class LlaveInglesa:
    def __init__(self, apertura_max: float, material: str):
        self._apertura_max = apertura_max 
        self._material = material
    
    def usar(self) -> str:
        return f"Llave Inglesa {self._material} utilizada para APRETAR tuercas."
        
    def info(self) -> str:
        return f"Llave Inglesa | Apertura Máx: {self._apertura_max} mm | Material: {self._material}"

def carpintero(herramienta):
    print(f"Carpintero usa:")
    print(f"Herramienta: {herramienta.info()}")
    resultado = herramienta.usar()
    
    print(f"Acción: {resultado}")

martillo = Martillo(peso=0.8, material_cabeza="Acero")
destornillador = Destornillador(tipo_punta="Plana", material_mango="Plástico")
llave = LlaveInglesa(apertura_max=30.0, material="Cromo Vanadio")

carpintero(martillo)
carpintero(destornillador)  
carpintero(llave)