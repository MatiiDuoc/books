from colorama import Style, Fore, Back
import numpy
import os
import msvcrt
import random

#########
#Crear arreglos
libros = numpy.empty([10,4], object)
#######
#Funciones de arreglo
def printv(texto):
    printv(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")
def printr(texto):
    printr(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")
def limpiarPantalla():
    printv("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system('cls')
#funciones del arreglo

#validarcodigo
#guaradar
#buscar
