class Figura:
    def __init__(self,nombre,area,coordenadaX,coordenadaY):
        self.nombre=nombre
        self.area=area
        self.coordenadaX=coordenadaX
        self.coordenadaY=coordenadaY
    
    def __del__(self):
        print("objeto destruido")
    
    def mostrar_figura(self):
        print(f"La figura se llama {self.nombre} \nTiene un área de {self.area} m^2 \nE inicia en las coordenadas ( '{self.coordenadaX}', '{self.coordenadaY}' )")

figura=Figura("Círculo",30.5,-1,2)

figura.mostrar_figura()