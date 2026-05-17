#13. Sumar digitos y suma total

def suma_digitos(numero):

    suma=0

    while numero>0:
        suma=suma+numero%10
        numero=numero//10

    return suma

total=0

numero=int(input("Ingrese un numero: "))

while numero!=0:

    print("La suma de digitos es: ",suma_digitos(numero))

    total=total+numero

    numero=int(input("Ingrese un numero: "))

print("La suma total es: ",total)
print("La suma de digitos del total es: ",suma_digitos(total))