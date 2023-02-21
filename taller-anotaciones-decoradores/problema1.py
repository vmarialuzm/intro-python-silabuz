# Implementar la función get_avg que calcule el promedio de una lista de números:

def funcion_decoradora(funcion_parametro):
    def funcion_auxiliar(numbers):
        print("Inicio del cálculo del promedio de la lista de números.")
        print(funcion_parametro(numbers))
        print("El cálculo ha finalizado.")
    return funcion_auxiliar


@funcion_decoradora
def get_avg(numbers:list)->float:
    return sum(numbers)/len(numbers)


lista_numbers = [10, 40, 20, 45, 25, 35, 15]
get_avg(lista_numbers)
