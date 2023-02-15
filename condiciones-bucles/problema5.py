# Leer nombre de invitados y agregarlos a una lista si han traido regalo.
# Tener la opción de detener la adición de invitados.
# Finalmente imprimir los invitados que llevaron regalo

#Mí solución
trajeronRegalo=[]

while True:
    invitado=input(f"¿Cuál es tu nombre?: ")
    regalo=input(f"¿Haz traido regalo? Si/No: ").lower()

    if regalo == "si":
        trajeronRegalo.append(invitado)

    pregunta=input(f"¿Deseas seguir agregando invitados? Si/No: ").lower()
    if pregunta == "si":
        continue
    else:
        print(f"La lista de invitados que trajo regalo es: {trajeronRegalo}")
        break

#Solución del profesor 
invitados = []

while True:
    nombre = input("Ingrese su nombre: ")
    trajo_regalo = input("Trajo regalo? S/N: ")

    if trajo_regalo.upper() == "S":
        trajo_regalo = True
    else:
        trajo_regalo = False

    invitados.append({
        'nombre': nombre,
        'trajo_regalo': trajo_regalo
    })

    acabar = input("Deseas acabar y lista los invitados con regalo? S/N: ")

    if acabar.upper() == "S":
        print("Invitados buena onda que si traen regalos. !!!")
        for invitado in invitados:
            if invitado['trajo_regalo']:
                print(invitado['nombre'])
        break
