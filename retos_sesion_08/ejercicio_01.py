class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador =int(numerador)
        self.denominador = int(denominador)
    
    def __str__(self) -> str:
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, otro):
        nuevo_num = self.numerador * otro.denominador + otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __sub__(self, otro):
        nuevo_num = self.numerador * otro.denominador - otro.numerador * self.denominador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __mul__(self, otro):
        nuevo_num = self.numerador * otro.numerador
        nuevo_den = self.denominador * otro.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def __truediv__(self, otro):
        nuevo_num = self.numerador * otro.denominador
        nuevo_den = self.denominador * otro.numerador
        return Fraccion(nuevo_num, nuevo_den)
    
    def __eq__(self, otro):  
        if isinstance(otro, Fraccion):
            return self.numerador == otro.numerador and self.denominador == otro.denominador
        return False
    
    def __gt__(self, otro):  
        if isinstance(otro, Fraccion):
            return self.numerador * otro.denominador > otro.numerador * self.denominador
        return False
    
    def __lt__(self, otro):  
        if isinstance(otro, Fraccion):
            return self.numerador * otro.denominador < otro.numerador * self.denominador
        return False
    
    def __ne__(self, otro): 
        if isinstance(otro, Fraccion):
            return self.numerador != otro.numerador or self.denominador != otro.denominador
        return True
 
    
fraccion1 = Fraccion(4, 5)
fraccion2 = Fraccion(1, 2)
print(f'{fraccion1} | {fraccion2}')
print(fraccion1 + fraccion2) 
print(fraccion1 - fraccion2)  
print(fraccion1 * fraccion2)
print(fraccion1 / fraccion2)
print(fraccion1 == fraccion2) 
print(fraccion1 < fraccion2)  
print(fraccion1 > fraccion2)
print(fraccion1 != fraccion2)
