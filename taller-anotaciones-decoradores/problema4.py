# Dada la función "calc_par_impar" que retorna un booleano, dependiendo si el número ingresado es par o impar, cree un decorador que imprima que tipo de número a recibido la función.

def funcion_decoradora(funcion_parametro):
    def funcion_interior(n):
        if funcion_parametro(n):
            print("El número es par")
        else:
            print("El número es impar")
    return funcion_interior

@funcion_decoradora
def calc_par_impar(n:int)->bool:
    return n % 2 == 0

num=int(input("Ingrese un número: "))
calc_par_impar(num)