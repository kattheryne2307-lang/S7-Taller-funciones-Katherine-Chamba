#12. CRUD de productos

productos=[]

def crear():
    id=int(input("Ingrese ID: "))
    nombre=input("Ingrese nombre: ")
    precio=float(input("Ingrese precio: "))
    cantidad=int(input("Ingrese cantidad: "))

    producto=[id,nombre,precio,cantidad]

    productos.append(producto)

def leer():

    for producto in productos:
        print(producto)

def actualizar():

    id=int(input("Ingrese ID a actualizar: "))

    for producto in productos:

        if producto[0]==id:

            producto[1]=input("Nuevo nombre: ")
            producto[2]=float(input("Nuevo precio: "))
            producto[3]=int(input("Nueva cantidad: "))

def eliminar():

    id=int(input("Ingrese ID a eliminar: "))

    for producto in productos:

        if producto[0]==id:
            productos.remove(producto)

opcion=0

while opcion!=5:

    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

    opcion=int(input("Ingrese una opcion: "))

    match opcion:

        case 1:
            crear()

        case 2:
            leer()

        case 3:
            actualizar()

        case 4:
            eliminar()

        case 5:
            print("Programa finalizado")