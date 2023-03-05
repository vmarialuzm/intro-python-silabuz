# Ejemplo de composicion

class Animal:
    def __init__(self,especie,peso):
        self.especie=especie
        self.peso=peso
        self.hueso1=Hueso("Femur","largo")   
    
    def comer(self):
        print("Este animal está comiendo")

    def compuesto(self):
        print("Tiene un hueso llamado",self.hueso1.nombre,"tipo",self.hueso1.tipo)


class Hueso:
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo


animal=Animal("vertebrado",20)
animal.comer()
animal.compuesto()


  