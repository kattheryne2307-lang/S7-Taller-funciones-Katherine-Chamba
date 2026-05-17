#14. Numero primo

def primo(numero):

    if numero<2:
        return False

    for i in range(2,numero):

        if numero%i==0:
            return False

    return True

numero=int(input("Ingrese un numero: "))

if primo(numero):
    print("Es primo")

else:
    print("No es primo")