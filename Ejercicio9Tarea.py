#9. Identificador de socios

def validar_dni(dni):

    if len(dni)==10:
        return True

    else:
        return False

nombre=input("Ingrese el nombre: ")

while nombre!="":

    dni=input("Ingrese el DNI: ")

    while validar_dni(dni)==False:

        dni=input("Ingrese un DNI valido: ")

    partes=nombre.split()

    primer_nombre=partes[0]

    apellido=partes[-1]

    identificador=primer_nombre+str(len(apellido))+dni[:3]

    print("Identificador: ",identificador)

    nombre=input("Ingrese el nombre: ")