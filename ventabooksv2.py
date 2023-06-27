
import funcventabookv2 as fu
while True:
    print("===== VENTABOOKS =====")
    print("1. Guardar libro")
    print("2. Buscar libro")
    print("3. Imprimir documentos")
    print("4. Salir")

    opcion = input("Ingrese el número de opción que desea ejecutar: ")

    if opcion == "1":
        fu.opcion_guardar_libro()
    elif opcion == "2":
        fu.opcion_buscar_libro()
    elif opcion == "3":
        fu.opcion_imprimir_documentos()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")