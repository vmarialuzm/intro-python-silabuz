# 1. Escriba un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*):

def dibujar_caracteres(anchura,altura,caracter):
    for i in range(1,altura+1):
        for j in range(1,anchura+1):
            print(caracter,end=" ")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = input("Carácter a utilizar: ")
dibujar_caracteres(anchura,altura,caracter)

# 2.1 Escriba un programa que pida la anchura de un triángulo y lo dibuje con caracteres producto (*):

def dibujar_triangulo(anchura):
    for i in range(1,anchura+1):
        print("* "*i)

def dibujar_triangulo2(anchura):
    for i in range(anchura-1,0,-1):
        print("* "*i)

anchura=int(input("Anchura del triángulo: "))
dibujar_triangulo(anchura)
dibujar_triangulo2(anchura)

# 2.2 Escriba un programa que pida la anchura de un triángulo y dibuje una sucesión de triángulos con caracteres producto (*):

def dibujar_sucesion(anchura):
    for k in range(anchura,0,-1):
        for i in range(1,k+1):
            print("* "*i)
        for j in range(k-1,0,-1):
            print("* "*j)

anchura=int(input("Anchura del triángulo: "))
dibujar_sucesion(anchura)

# 3.1 Escriba un programa que pida un año y que escriba si es bisiesto o no.

def comprobar_año_bisiesto(año):
    return año % 400 == 0 or (año % 4 == 0  and año % 100 != 0)

print("COMPROBADOR DE AÑOS BISIESTOS")    
pregunta=int(input("Escriba un año y le diré si es bisiesto: "))

if comprobar_año_bisiesto(pregunta):
    print(f"El año {pregunta} es un año bisiesto")
else:
    print(f"El año {pregunta} no es un año bisiesto")

# 3.2 Escriba un programa que pida dos años y escriba cuántos años bisiestos hay entre esas dos fechas (incluidos los dos años):

def contar_bisiestos(año, otro_año):
    contador=0
    for i in range(año,otro_año+1):
        if comprobar_año_bisiesto(i):
            contador+=1
    return contador 

print("CONTADOR DE AÑOS BISIESTOS")
año=int(input("Escriba un año: "))
otro_año=int(input(f"Escriba otro año posterior a {año}: "))

while True:
    if otro_año<=año:
        otro_año=int(input(f"{otro_año} no es mayor que {año}. Intentelo de nuevo: "))
    else:
        break

print(f"De {año} a {otro_año} hay {otro_año-año+1} años, {contar_bisiestos(año,otro_año)} de ellos son bisiestos")

# 4.1 Escriba un programa que permita crear una lista de palabras (que puede ser vacía). Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

def crear_lista(i):
    pregunta=int(input(f"Dígame cuántas palabras tiene la lista {i}: "))
    lista_creada=[]
    for i in range(1,pregunta+1):
        palabra=input(f"Dígame la palabra {i}: ")
        lista_creada.append(palabra)
    return lista_creada

print(f"La lista creada es: {crear_lista()}")
    
# 4.2 Escriba un programa que pida cuántas listas se quieren crear y las solicite a continuación:

print("Generador de listas")
pregunta_cantidad=int(input(f"¿Cuántas listas quiere escribir? "))

for i in range(1,pregunta_cantidad+1):
    print(f"La lista {i} es: {crear_lista(i)}")

# 4.3 Modifique el programa anterior de manera que las listas se escriban al final del programa:

print("Generador de listas")
pregunta_cantidad=int(input(f"¿Cuántas listas quiere escribir? "))
print()

listas=[]
for j in range(1,pregunta_cantidad+1):
    listas.append(crear_lista(j))
    print()

for i in range(len(listas)):
    print(f"La lista {i+1} es: {listas[i]}")