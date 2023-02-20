# 1. Por ejemplo, puedes escribir una función lambda que duplique sus argumentos lambda x: x * 2 y usarla con la función map para duplicar todos los elementos de una lista:

mi_lista = [1, 2, 3, 4, 5, 6]

lista_nueva=list(map(lambda x:x*2,mi_lista))

print(lista_nueva)

# 2. También puedes escribir una función lambda que revise si un número es positivo, lambda x: x > 0, y usarla con la función filter para crear una lista de números positivos.

mi_lista2 = [18, -3, 5, 0, -1, 12]

lista_positivos=list(filter(lambda x:x>0,mi_lista2))

print(lista_positivos)



