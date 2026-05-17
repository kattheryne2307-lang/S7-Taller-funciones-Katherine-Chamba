#1. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resultado=[]

for i in range(len(alfabeto)):
    posicion =i
    if posicion % 3!=0:
        resultado.append(alfabeto[i])

    print("La lista resultante es: ",resultado)