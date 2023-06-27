import funcv2book as fu

while True:
    fu.limpiarPantalla()
    fu.printv("Sistema de ventabooks")
    fu.printv("********************")
    print("1.- Guardar")
    print("2.- Buscar")
    print("3.- Certificados")
    print("0.- Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 0:
        print("Adios!")
        break
    elif opcion == 1:
        fu.printv("Guardar un libro")
    elif opcion == 2:
        fu.printv("Buscar un libro")
    elif opcion == 3:
        fu.printv("Certificados")
        print("1.- Criticas")
        print("2.- Detalles")
        cert = int(input("Seleccione: "))
        if cert == 1:
            fu.printv("Certificado de criticar")
        elif cert == 2:
            fu.printv("Certificado de detalles")
        else:
            fu.printr("Opcion no valida")
    else:
        fu.printr("Opcion no valida!")

