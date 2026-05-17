#2. Crear una función doblar valor que multiplique los elementos de una lista

def doblarLista(lista):
    nueva_lista=[]
    for i in lista:
        doble=i*2
        nueva_lista.append(doble)
    return nueva_lista
numeros = [1,2,3,4,5]
resultado=doblarLista(numeros)
print("Lista original: ",numeros)
print("Lista doblada: ",resultado)

