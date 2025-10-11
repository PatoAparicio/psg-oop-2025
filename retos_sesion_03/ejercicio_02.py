class Cocinero:
    productividad_receta=10
    receta_list = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, nombre, receta, productividad, ingredientes):
        self.nombre=nombre
        self.productividad = productividad
        self.receta=receta
        self.ingredientes = set(ingredientes) 
        print(f"El cocinero {nombre} tiene los siguientes ingredientes: {ingredientes}")

    # Métodos de Instancia
    def verificar_ingredientes(self, receta: str) -> bool:
        if receta not in self.receta_list:
            print(f"La receta '{receta}' no está definida en el sistema.")
            return False

        ingredientes_requeridos = self.receta_list[receta]
        ingredientes_faltantes = ingredientes_requeridos - self.ingredientes
        
        if not ingredientes_faltantes:
            return True
        else:
            print(f"Faltan ingredientes: {ingredientes_faltantes}")
            print(f"No se pudo preparar la receta '{receta}'")
            return False

    def preparar_receta(self, receta) -> str:
        tiene_ingredientes = self.verificar_ingredientes(receta)
        if tiene_ingredientes:
            self.productividad += self.productividad_receta
            print(f"Receta '{receta}' preparada exitosamente")
            print(f"El cocinero {self.nombre} tiene {self.productividad} de productividad")
            return f"Receta '{receta}' preparada exitosamente"

        else:
            return f"No se pudo preparar la receta '{receta}'"

    #Método de Clase (@classmethod)

    @classmethod
    def obtener_lista_recetas(cls):
        return list(cls.receta_list.keys())

    # --- Método Estático (@staticmethod) ---

    @staticmethod
    def calcular_productividad_total(cocineros):
        productividad_total = sum(c.productividad for c in cocineros)
        return productividad_total

# Instanciar Cocineros
cocinero1 = Cocinero("Chef Ramiro","pan",  10, ["harina", "agua", "sal"])
cocinero1.preparar_receta("pan")
cocinero1.preparar_receta("pizza")


cocinero2 = Cocinero("Chef Sonia","pan",  100, ["harina", "agua", "sal", "tomate", "queso"])
cocinero2.preparar_receta("pan")
cocinero2.preparar_receta("pizza")

cocinero3 = Cocinero("Chef Sam","pan",  0, [])
cocinero3.preparar_receta("galleta")
cocinero3.preparar_receta("pizza")

cocineros = [cocinero1, cocinero2, cocinero3]
productividad_total = Cocinero.calcular_productividad_total(cocineros)
print(f"Productividad total de todos los cocineros: {productividad_total}")


