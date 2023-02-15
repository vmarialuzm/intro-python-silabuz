# 1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(asignaturas)

# 2. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for asignatura in asignaturas:
    nota=int(input(f"La nota que ha sacado en {asignatura} es: "))
    notas.append(nota)

for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} has sacado {nota[i]}")

# 4. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

lista=[]
for i in range(1,7):
    numeros=int(input(f"El número ganador {i} es: "))
    lista.append(numeros)
print(f"Los números ganadores son {sorted(lista)}")

# 5. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

for i in range(10,0,-1):
    print(i, end=", ")

# 6. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas=[]

for asignatura in asignaturas:
    nota=int(input(f"¿ Cuál es la nota que sacaste en {asignatura}?: "))
    if nota >= 11:
        aprobadas.append(asignatura)

for asignatura in aprobadas:
    asignaturas.remove(asignatura)

print(f"Las asignaturas que el ususario tiene que repetir {asignaturas}")


# 7. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario=["a","b","c","d","e","f","g","h","i","j"]

for i in range(len(abecedario),1,-1):
    if i % 3 == 0:
        abecedario.pop(i-1)

print(f"La lista resultante es: {abecedario}")

# 8. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra=input("Ingrese una palabra: ")
palabra_inversa=palabra
palabra=list(palabra)
palabra_inversa=list(palabra_inversa)
palabra_inversa.reverse()

if palabra==palabra_inversa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

# 9. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra=input("Ingrese una palabra: ").lower()
vocales=["a","e","i","o","u"]

for vocal in vocales:
    print(f"El número de veces que aparece la vocal {vocal} es {palabra.count(vocal)}")


# 10. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios=[50, 75, 46, 22, 80, 65, 8]
print(f"El menor de los precios es: {min(precios)}")
print(f"El mayor de los precios es: {max(precios)}")





