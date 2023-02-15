# Leer números enteros hasta que el usuario coloque el 0. Luego indicar:
# a.La suma de los números positivos.
# b.La suma de los negativos.
# c.La cantidad de números registrados.

#Mí solución
positivos=[]
negativos=[]

while True:
    num = int(input("Ingresa un numero: "))
    if num>0:
        positivos.append(num)
    elif num<0:
        negativos.append(num)
    else:
        print(f"La suma de los números positivos es: {sum(positivos)}")
        print(f"La suma de los números negativos es: {sum(negativos)}")
        print(f"La cantidad de números registrados es: {len(positivos)+len(negativos)}")
        break
    
#Solución del profesor    
numerosPosi = []
numerosNega = []

while True:
    num = int(input("Ingrese un numero: "))

    if (num == 0):
        print("La suma de posi: ", sum(numerosPosi))
        print("La suma de nega: ", sum(numerosNega))
        print("La cantidad de # ingresados es",
              len(numerosPosi) + len(numerosNega))
        break

    if num > 0:
        numerosPosi.append(num)
    else:
        numerosNega.append(num)