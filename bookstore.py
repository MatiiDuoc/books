import funcbookstore as funcbook

while True:
    print("""
     ----------------------------
    |Sistema de gestion de libros|
     ----------------------------
     1.- Agregar un nuevo libro
     2.- Listar libros
     3.- Modificar libros
     4.- Eliminar libro
     5.- Salir del sistema
    """)
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 5:
        pass
    elif opcion == 1:
        print("Agregar un nuevo libro")
        c = int(input("Ingrese el codigo del libro: "))
        t = input("Ingrese el titulo del libro: ")
        p = int(input("Ingrese el precio del libro: "))
        funcbook.addBook(c,t,p)
    elif opcion == 2:
        print("Listar los libros agregados")
        funcbook.listBook()
    elif opcion == 3:
        print("Modificar un libro")
        cb = int(input("Ingrese el codigo del libro que deseas modificar: "))
        funcbook.codigoBook(cb)
        title = input("Ingrese el nuevo titulo del libro: ")
        funcbook.updatebook(title)
    elif opcion == 4:
        pass