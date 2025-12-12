class Cocinero:
    recetas_disponibles = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, ingredientes):
        self.ingredientes = set(ingredientes)
        self.productividad = 0
        print(f"El cocinero tiene los siguientes ingredientes: {self.ingredientes}")

    def preparar_receta(self, receta):
        if receta not in self.recetas_disponibles:
            print(f"La receta '{receta}' no está definida en el sistema.")
            return False

        ingredientes_requeridos = self.recetas_disponibles[receta]
        ingredientes_faltantes = ingredientes_requeridos - self.ingredientes
        
        if ingredientes_faltantes:
            print(f"Faltan ingredientes para '{receta}': {ingredientes_faltantes}")
            return False
        
        self.productividad += 1
        print(f"Receta '{receta}' preparada exitosamente")
        print(f"Productividad del cocinero: {self.productividad}")
        return True
    
    @staticmethod
    def productividad_total(cocineros):
        total = sum(c.productividad for c in cocineros)
        return total


# Instanciar Cocineros
cocinero_1 = Cocinero(["harina", "agua", "sal"])
cocinero_1.preparar_receta("pan")
cocinero_1.preparar_receta("pizza")

cocinero_2 = Cocinero(["harina", "agua", "sal", "tomate", "queso"])
cocinero_2.preparar_receta("pan")
cocinero_2.preparar_receta("pizza")

# Calcular productividad total
cocineros = [cocinero_1, cocinero_2]
productividad_agregada = Cocinero.productividad_total(cocineros)
print(f"\nProductividad total de la cocina: {productividad_agregada}")



