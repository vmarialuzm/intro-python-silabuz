#Leer números del usuario, hasta que el usuario ingrese el 0.Luego mostrar la suma de todos los números ingresados.

numbers = []  # lista vacia

while True:
    num = int(input("Ingresa un numero: "))

    if num == 0:
        print(f"La suma de los numeros es {sum(numbers)}")
        break

    numbers.append(num)