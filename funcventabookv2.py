import random

libros = []

def opcion_guardar_libro():
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    precio = float(input("Ingrese el precio del libro: "))

    if len(codigo) == 0 or len(titulo) < 4 or precio < 0:
        print("Datos inválidos. Verifique los requisitos.")
        return

    for libro in libros:
        if libro[0] == codigo:
            print("El código del libro ya existe.")
            return

    libros.append([codigo, titulo, autor, precio])
    print("Libro guardado con éxito.")

def opcion_buscar_libro():
    codigo = input("Ingrese el código del libro a buscar: ")

    for libro in libros:
        if libro[0] == codigo:
            print("Información del libro:")
            print(f"Código: {libro[0]}")
            print(f"Título: {libro[1]}")
            print(f"Autor: {libro[2]}")
            print(f"Precio: {libro[3]}")
            return

    print("Libro no encontrado.")

def opcion_imprimir_documentos():
    if len(libros) == 0:
        print("No hay libros registrados.")
        return

    opcion = input("Ingrese el número del documento que desea imprimir (1. Críticas del libro, 2. Detalle de ventas): ")

    if opcion == "1":
        print("Críticas del libro:")
        for libro in libros:
            print(f"Código: {libro[0]}, Título: {libro[1]} - Crítica/Critica constructiba: {random.choice(['Excelente', 'Bueno', 'Regular', 'Malo', 'Muy malo', 'Pesimo', 'No recomendado'])}")
    elif opcion == "2":
        print("Detalle de ventas realizadas:")
        for libro in libros:
            print(f"Código: {libro[0]}, Título: {libro[1]} - Ventas: {random.randint(1, 10)}")
    else:
        print("Opción inválida.")


