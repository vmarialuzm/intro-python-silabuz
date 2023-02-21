# Cree una función con anotaciones, que tome una palabra y duplique sus letras y las retorne en una lista.

def duplicar_letras(palabra:str)->list:
    palabra_duplicada:list=[]
    for letra in palabra:
        for i in range(0,2):
            palabra_duplicada.append(letra)
        
    return palabra_duplicada

palabra:str=input("Ingrese una palabra: ")
print(duplicar_letras(palabra))
