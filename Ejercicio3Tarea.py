#3. Numeros primos, suma de digitos y frecuencia

def primo(numero):

    if numero<2:
        return False

    for i in range(2,numero):

        if numero%i==0:
            return False

    return True

def suma_digitos(numero):

    suma=0

    while numero>0:
        suma=suma+numero%10
        numero=numero//10

    return suma

def frecuencia(numero,digito):

    contador=0

    for i in str(numero):

        if i==str(digito):
            contador=contador+1

    return contador

def factorial(numero):

    resultado=1

    for i in range(1,numero+1):
        resultado=resultado*i

    return resultado

mayor=0

numero=int(input("Ingrese un numero primo: "))

while primo(numero):

    print("La suma de digitos es: ",suma_digitos(numero))

    digito=int(input("Ingrese un digito: "))

    print("La frecuencia es: ",frecuencia(numero,digito))

    if numero>mayor:
        mayor=numero

    numero=int(input("Ingrese un numero primo: "))

print("El factorial del mayor numero es: ",factorial(mayor))