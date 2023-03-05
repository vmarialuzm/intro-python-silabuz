# Ejemplo de polimorfismo

import math

class Figura:
    def __init__(self,lados):
        self.lados=lados

    def calcArea(self):
        print("Calcula el área de la figura")
    
class Triangulo(Figura):
    def __init__(self,lados,base,altura):
        super().__init__(lados)
        self.base=base
        self.altura=altura

    def calcArea(self):
        return (self.base * self.altura)/2

class Circulo(Figura):
    def __init__(self,lados,radio):
        super().__init__(lados)
        self.radio=radio

    def calcArea(self):
        return math.pi * self.radio**2

t=Triangulo(3,10,5)
print(t.calcArea())
print(t.lados)
c=Circulo(0,1)
print(c.calcArea())
print(c.lados)