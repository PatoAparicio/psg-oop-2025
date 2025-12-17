class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.__numero_cuenta = numero 
        self.__saldo = max(0.0, saldo) 
        self.nombre_titular = titular 
        
        print(f"Cuenta {self.__numero_cuenta} de {self.nombre_titular}. Cuenta con saldo de: ${self.__saldo:.2f}")

    def set_deposito(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito de ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}"
        return "Error: La cantidad a depositar debe ser positiva."

    def set_retiro(self, cantidad):
        if cantidad <= 0:
            return "Error: La cantidad a retirar debe ser positiva."
        
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro de ${cantidad:.2f}. Nuevo saldo: ${self.__saldo:.2f}"
        else:
            return f"Intentó retirar ${cantidad:.2f}. Fondos insuficientes.  Saldo disponible: ${self.__saldo:.2f}"

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def nombre_titular(self):
        return self._nombre_titular

    @nombre_titular.setter
    def nombre_titular(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre_titular = nuevo_nombre.strip()
        else:
            print("El nombre del titular no puede estar vacío.")


cuenta = Cuenta("1001-A", "Patricia Lopez", 500.50)

print("\nModificación de Saldo")
print(cuenta.set_deposito(200.00))
print(cuenta.set_retiro(100.25))
print(cuenta.set_retiro(1000.00)) 
print(f"Saldo actual de {cuenta.nombre_titular}: ${cuenta.saldo:.2f}")

print("\nModificación del Titular de la Cuenta")

print(f"Titular actual de Cuenta: {cuenta.nombre_titular}")

cuenta.nombre_titular = "Patricia Lopez García"
print(f"Nuevo titular de Cuenta: {cuenta.nombre_titular}")
