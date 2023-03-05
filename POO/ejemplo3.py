#Ejemplo de herencia

class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base * self.altura
    
r=Rectangulo(10,5)
print("El área del rectángulo es",r.area())


class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)

c=Cuadrado(5)
print("El área del cuadrado es",c.area())
