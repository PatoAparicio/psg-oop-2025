# Productos
class Helado:
    def __init__(self, envase):
        self.envase = envase

    def comer(self):
        print("Comiendo helado")

class HeladoVainilla(Helado):
    def comer(self):
        print(f"Vainilla 🍦 en {self.envase}")

class HeladoChocolate(Helado):
    def comer(self):
        print(f"Chocolate 🍦 en {self.envase}")

# Maquinas
class Maquina:
    def preparar(self, envase):
        pass
class MaquinaVainilla(Maquina):
    def preparar(self, envase):
        return HeladoVainilla(envase)
class MaquinaChocolate(Maquina):
    def preparar(self, envase):
        return HeladoChocolate(envase)

# Factory Central (decide qué fábrica usar)
class Encargado:
    def preparar_helado(self, sabor, envase):
        if sabor == "vainilla":
            return MaquinaVainilla().preparar(envase)
        if sabor == "chocolate":
            return MaquinaChocolate().preparar(envase)
        raise ValueError("❌ Helado no disponible. Intente de nuevo")

# Cliente (No conoce las fábricas, solo pide el helado)
while True:
    print("\n🍨 Pedidos de Helado 🍨") 
    print("1. Vainilla en Cono")
    print("2. Vainilla en Vaso")
    print("3. Chocolate en Cono")
    print("4. Chocolate en Vaso")
    print("5. Salir")
        
    opcion = input("Elige una opción (1-5): ")
    
    encargado = Encargado()
    helado_preparado = None 
    try:
        if opcion == '1':
            helado_preparado = encargado.preparar_helado("vainilla", "cono")
            helado_preparado.comer()
        
        elif opcion == '2':
            helado_preparado = encargado.preparar_helado("vainilla", "vaso")
            helado_preparado.comer()
            
        elif opcion == '3':
            helado_preparado = encargado.preparar_helado("chocolate", "cono")
            helado_preparado.comer()

        elif opcion == '4':
            helado_preparado = encargado.preparar_helado("chocolate", "vaso")
            helado_preparado.comer()
            
        elif opcion == '5':
            print("\n👋 ¡Hasta pronto!")
            break
            
        else:
            print("❌ Opción no válida.")
        
    except ValueError as e:
        print(f"Error: {e}")