#Ejemplo de herencia

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

class Carro(Vehiculo):
    def __init__(self,marca,modelo,estado):
        super().__init__(self,marca,modelo)
        self.estado=estado

