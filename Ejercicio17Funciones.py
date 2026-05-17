#17. Validar DNI

def validar_dni(dni):

    if len(dni)==10:
        return True

    else:
        return False

dni=input("Ingrese el DNI: ")

if validar_dni(dni):
    print("DNI valido")

else:
    print("DNI no valido")