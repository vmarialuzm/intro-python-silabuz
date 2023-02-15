# Realizar un programa para que el usuario adivine un número del 1 al 1000. Cada vez que el usuario escriba un número le dirás si el número a adivinar es mayor o menor que el ingresado. Una vez lo adivine le indicaremos cuantas veces le tomó acertar.

import random

# Quiero que un entero
number = random.randint(1, 1000)
print("trampa", number)
contador=0

while True:
    num = int(input("Ingrese un numero: "))

    if num == number:
        contador+=1
        print("Adivinaste el numero", num,"te tomó acertar" ,contador,"veces")
        break

    elif num < number:
        contador+=1
        print("Debes ingresar un numero mayor")

    else:
        contador+=1
        print("Debes ingresar un numero menor")




