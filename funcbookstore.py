import numpy as np
import os
from colorama import Style, Fore, Back
import msvcrt

libros = np.empty([10, 3], object)
# validamos el codigo


def validCodigo(codigo):
    for i in range(10):
        if libros[i, 0] == codigo:
            return i
    return -1
# Se reciben los parametros del array y se ocuparan en la funcion de addBook


def addBook(codigo, titulo, precio):
    if None in libros:
        for i in range(10):
            if codigo == libros[i,0]:
                if len(titulo) >= 4:
                    if precio > 0:
                        for i in range(10):
                            if codigo in libros[i, 0] == None:
                                libros[i, 1] == codigo
                                libros[i, 2] == titulo
                                libros[i, 2] == precio
                                print(f"El libro {titulo}se a guardado con exito!")
                                break
                        break
                    else:
                        print("El precio del libro no puede ser negativo!")
                else:
                    print("El titulo debe de contener como minimo 4 caracteres!")
            else:
                print("El codigo ya se encuentra registrado!")
    else:
        print("No hay espacio disponible!")


def listBook():
    for i in range(10):
        if libros[i, 0] != None:
            print(
                f"Codigo:{libros[i,0]} Titulo:{libros[i,1]} Precio:{libros[i,2]}")
        else:
            print("Espacio disponible")


def searchBook(codigo):
    if codigo in libros:
        for i in range(10):
            if libros[i, 0] == codigo:
                print(
                    f"Libro encontrado: Codigo:{libros[i,0]} Titulo:{libros[i,1]} Precio:{libros[i,2]}")
                break
            else:
                print("El video no se encuentra registrado!")


def deleteBook(codigo):
    for i in range(10):
        if libros[i, 0] == codigo:
            libros[i, 0] == None
            libros[i, 1] == None
            libros[i, 2] == None
            print("Libro eliminado con exito!")
            break


def codigoBook(codigo):
    if codigo in libros:
        for i in range(10):
            if libros[i, 0] == codigo:
                # recibira el nuevo titulo del libro
                updatebook()
    else:
        print("El codigo del libro no se encuentra")


def updatebook(newtitle):
    if len(newtitle) > 4:
        codigo -= 1
        if codigo >= 0 and codigo < len(libros):
            libros[i, 1] = newtitle
            print("Titulo del libro modificado con exito")
    # break
