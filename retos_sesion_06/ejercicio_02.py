from typing import List
class Unidad:
    def __init__(self, numero: str):
        self.numero = numero
    
    def mostrar_info(self) -> str:
        return f"Unidad {self.numero}."

class Departamento(Unidad):
    def __init__(self, numero: str, inquilinos: List[str]):
        super().__init__(numero)
        self.inquilinos = inquilinos
    
    def mostrar_info(self) -> str:
        inquilinos_str = ", ".join(self.inquilinos) if self.inquilinos else "Vacío"
        return f"Departamento {self.numero} | Inquilinos: {inquilinos_str}"

class Oficina(Unidad):
    def __init__(self, numero: str, telefono: str):
        super().__init__(numero)
        self.telefono = telefono
    
    def mostrar_info(self) -> str:
        return f"Oficina {self.numero} | Teléfono: {self.telefono}"

class Piso:
    def __init__(self, numero: int):
        self.numero = numero
        self._unidades: List[Unidad] = []

    def agregar_unidad(self, unidad: Unidad):
        self._unidades.append(unidad)

    def mostrar_unidades(self):
        print(f"\nPiso: {self.numero} tiene: {len(self._unidades)} Unidades")
        if not self._unidades:
            print("   (Piso vacío)")
            return
            
        for unidad in self._unidades:
            print(f"{unidad.mostrar_info()}")

class Edificio:
    def __init__(self, nombre: str, direccion: str, num_pisos: int):
        self.nombre = nombre
        self.direccion = direccion
        self._pisos: List[Piso] = [] #

        for i in range(1, num_pisos + 1):
            piso = Piso(numero=i)
            self._pisos.append(piso)

    def obtener_piso(self, numero: int) -> Piso | None:
        for piso in self._pisos:
            if piso.numero == numero:
                return piso
        return None

    def mostrar_informacion(self):
        print(f"EDIFICIO: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        for piso in self._pisos:
            piso.mostrar_unidades()
        
 
edificio_central = Edificio("Torre Andina", "Av. 16 de Julio #123", num_pisos=3)

piso_1 = edificio_central.obtener_piso(1)
if piso_1:
    piso_1.agregar_unidad(Oficina(numero="1A", telefono="2245100"))
    piso_1.agregar_unidad(Oficina(numero="1B", telefono="2245101"))
    piso_1.agregar_unidad(Departamento(numero="103", inquilinos=["Sr. Guzmán"]))

piso_2 = edificio_central.obtener_piso(2)
if piso_2:
    piso_2.agregar_unidad(Departamento(numero="201", inquilinos=["Familia Ríos", "Laura"]))
    piso_2.agregar_unidad(Departamento(numero="202", inquilinos=["Pedro"]))
    piso_2.agregar_unidad(Oficina(numero="2A", telefono="2245200"))

piso_3 = edificio_central.obtener_piso(3)
if piso_3:
    piso_3.agregar_unidad(Oficina(numero="3C", telefono="2245300"))
    piso_3.agregar_unidad(Departamento(numero="304", inquilinos=["Dr. Soto"]))

edificio_central.mostrar_informacion()