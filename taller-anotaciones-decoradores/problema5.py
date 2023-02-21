# Cree una función decoradora deco1 que muestre el siguiente flujo, para cualquier número ingresado, por ejemplo para el número 30:

def deco1(funcion_parametro):
    def funcion_interior(a):
        print("Hola, estoy decorando esta función.")
        funcion_parametro(a)
        print("Terminé de decorar")
    return funcion_interior

@deco1
def mostrar(n)->None:
    print("Ingresaste el número",n)


mostrar(30)