# 1. Crear una lista con las letras de una palabra:

palabra=input("Ingrese una palabra: ")
lista=[letra for letra in palabra]
print(lista)

# 2. Crear una lista con las potencias de 2 de los primeros 10 números:

lista_potencias=[i**2 for i in range(1,11)]
print(lista_potencias)

# 3. Crear una lista con todos los múltiplos de 2 entre 0 y 10:

lista_múltiplos=[i for i in range(0,11) if i % 2 == 0]
print(lista_múltiplos)

# 4. Crear una lista de pares a partir de otra lista creada con las potencias de 2 de los primeros 10 números:

lista_combinada=[i**2 for i in range(1,11) if i % 2 ==0]
print(lista_combinada)

# 5. Usando comprensión de listas, podemos crear una nueva lista con las mismas cadenas pero con su primera letra en mayúscula (es decir, aplicar el método capitalize() de las cadenas).

lista_nombres=["luz","jorge","marco","ana"]
lista_capitalize=[nombre.capitalize() for nombre in lista_nombres]
print(lista_capitalize)

# 6. Siguiendo la misma sintaxis que antes, vamos a crear una nueva lista doubled_numbers que contenga el doble de cada uno de los números de numbers.

numbers=[1,3,5,7,9]
doubled_numbers=[number*2 for number in numbers]
print(doubled_numbers)

# 7. Crea una lista con números del 1 al 100 que sean múltiplos de 5.

multiplos_cinco=[i for i in range(1,101) if i % 5 == 0]
print(multiplos_cinco)

# 8. Crea una lista points que contiene (en forma de tuplas de dos elementos) la posición de todos los puntos bidimencionales entre las coordenadas (0, 0) y (5, 10).

#Método 1
points=[]
for x in range(0,6):
    for y in range(0,11):
        points.append((x,y))
print(points)

#Método 2
points2=[(x,y) for x in range(0,6) for y in range(0,11)]
print(points2)

# 9. Este fragmento genera un diccionario (doubles) donde las claves son números enteros del 1 al 10 y los valores, el doble de cada una de esas claves.

doubles={i:2*i for i in range(1,11)}
print(doubles)

# 10.generar una tupla usando el método de comprensión.

doubles2=tuple(2*i for i in range(1,11))
print(doubles2)
