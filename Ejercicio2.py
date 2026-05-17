#2. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra=input("Ingrese una palabra: ")
vocales=['a','e','i','o','u']

for vocal in vocales:
    contador=0
    for letra in palabra.lower():
        if letra==vocal:
            contador+=1
            print("La vocal ",vocal,"aparece",contador,"veces")