# Escriba un programa que dada una entrada numérica por el usuario, ingrese a una función que duplique el valor y sea retornado en forma de string o cadena. Utilice tipos tanto para las variables como para las funciones.

def duplicar_numero(num:int)->str:
    return str(num*2)

num:float=float(input("Ingrese un número: "))
print(duplicar_numero(num))
