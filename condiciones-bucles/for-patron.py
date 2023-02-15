# 1. Realizar una tabla de multiplicar

numero=int(input("Ingresa un número: "))

for i in range(1,13):
    print(f"{i}x{numero}={i*numero}")


# 2. Crear un bucle que cuente los números pares hasta el 100

contador=0
for i in range(1,101):
    if i % 2 == 0:
        contador+=1
print(f"La cantidad de numeros pares es: {contador}")


# 3. Imprimir el siguiente patrón

print("Solucion 1:")

for i in range(1, 6):
    print(i * "*")

for j in range(4, 0, -1):
    print(j * "*")

print("Solucion 2:")

for index in range(1, 10):
    if index < 6:
        print(index * "*")
    else:
        print((10 - index) * "*")