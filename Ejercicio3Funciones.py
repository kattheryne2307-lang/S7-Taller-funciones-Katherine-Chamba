#3. Multiplicar elementos de una lista ingresada por teclado

def doblar_lista(lista):
    nueva=[]

    for i in lista:
        nueva.append(i)

    return nueva

lista=[]
cantidad=int(input("Ingrese la cantidad de elementos: "))
for i in range(cantidad):
    numero=int(input("Ingrese un numero: "))
    lista.append(numero)

print("La nueva lista es: ",doblar_lista(lista))