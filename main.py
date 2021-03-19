import random
from tqdm import tqdm
from colorama import Fore, Back, Style

#from time import sleep sleep(0.02)

def generar_contrasena():
    """generar_contraseña es una funcion que contiene listas 
    Las cuales se unifican en otra lista llamada caracteres
    en la cual en el ciclo for se genera una contraseña aleatoria de 10 caracteres
    donde el modulo random elije los caracteres y los inserta en una nueva lista la cual
    Returns:
        str contrasena: devuelve contraseña o contraseñas dependiendo del valor que tenga range
    """
    mayusculas = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #simbolos = ['!','"','#','$','%','&','/','(',')','=','?','¿']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + numeros
    contrasena = []

    for i in range(10):#Dato dado por el usuario
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    c = open('archivo.txt', 'a')#generar un archivo y si ya existe sobre escribir en el
    can_clave = 1000000 #PODRIA SER DATO QUE SE PIDA AL USUARIO

    for i in tqdm(range(can_clave)):
        contrasena = generar_contrasena()
        c.write(contrasena + '\n')
    c.close()
    print(Fore.RED + 'Proceso Finalizado')


if __name__ == '__main__':
    run()