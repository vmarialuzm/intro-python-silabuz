#Problema1

#Problema2
for num in range(100,200):
    print(num)

#Problema3
for num in range(5,21,3):
    print(num)

#Problema4
num=int(input("Ingrese un número entero positivo: "))

for i in range(num,2*num):
    print(i)

#Problema5
multiplosTres=[]

for num in range(0,101):
    if num % 3 == 0:
        multiplosTres.append(num)
print(f"La sumatoria de los múltiplos de 3 en el rango de 0 a 100 es: {sum(multiplosTres)}")

#Problema6
vocales=["a","e","i","o","u"]
frase=input("Ingresa una frase: ").lower()
contador=0

for letra in frase:
    if letra in vocales:
        contador+=1
print(f"La cantidad de vocales que hay en la frase es: {contador}")        

