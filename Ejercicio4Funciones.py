#4. Validar correo electrónico

def validar(correo):
    if "@" in correo:
        return True
    else:
        return False

correo=input("Ingrese su correo: ")

if validar(correo):
    print("Correo valido")
else:
    print("Correo no valido")