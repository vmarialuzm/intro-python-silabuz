#Definición de clase
class Persona:
    def __init__(self,name,age):
        self.nombre=name
        self.edad=age

    def saluda(self,msg):
        return f"Hola {msg}, mi nombre es {self.nombre} y tengo {self.edad} años"

luiza=Persona("Luiza",20)
print(luiza.saluda("Marcelo"))

    