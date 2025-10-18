class Cuenta:
    def __init__(self, numero: str, titular: str, saldo_inicial: float = 0.0):
        self._numero_cuenta = numero 
        self._saldo = max(0.0, saldo_inicial) 
        self.nombre_titular = titular 
        
        print(f"Cuenta {self._numero_cuenta} de {self._nombre_titular}.")

    def depositar(self, cantidad: float) -> str:
        if cantidad > 0:
            self._saldo += cantidad
            return f"Depósito de ${cantidad:.2f}. Nuevo saldo: ${self._saldo:.2f}"
        return "Error: La cantidad a depositar debe ser positiva."

    def retirar(self, cantidad: float) -> str:
        if cantidad <= 0:
            return "Error: La cantidad a retirar debe ser positiva."
        
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            return f"Retiro de ${cantidad:.2f}. Nuevo saldo: ${self._saldo:.2f}"
        else:
            return f"Fondos insuficientes. Intentó retirar ${cantidad:.2f}. Saldo disponible: ${self._saldo:.2f}"

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero_cuenta(self) -> str:
        return self._numero_cuenta

    @property
    def nombre_titular(self) -> str:
        return self._nombre_titular

    @nombre_titular.setter
    def nombre_titular(self, nuevo_nombre: str):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre_titular = nuevo_nombre.strip()
        else:
            print("El nombre del titular no puede estar vacío.")

cuenta1 = Cuenta("1001-A", "Patricia Lopez", 500.50)

print("\nModificación de Saldo")
print(cuenta1.depositar(200.00))
print(cuenta1.retirar(100.25))
print(cuenta1.retirar(1000.00)) 
print(f"Saldo actual de {cuenta1.nombre_titular}: ${cuenta1.saldo:.2f}")

print("\nModificación del Titular de la Cuenta")

print(f"Titular actual de Cuenta: {cuenta1.nombre_titular}")

cuenta1.nombre_titular = "Patricia Lopez García"
print(f"Nuevo titular de Cuenta: {cuenta1.nombre_titular}")
