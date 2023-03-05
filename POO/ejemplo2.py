class Animal:
    def __init__(self,especie,peso):
        self.__especie=especie
        self.__peso=peso
    
    def __del__(self):
        print("Animal eliminado")
    
    def comer(self):
        print("Este animal está comiendo")
    
animal=Animal("Vertebrado",5)
animal.comer()
del animal