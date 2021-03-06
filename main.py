import random
from tqdm import tqdm
from colorama import Fore, Back, Style
from time import sleep  #Ejemplo de uso despues del for sleep(0.02)

numero_caracteres = int(input(Fore.GREEN + 'Ingresa el numero de caracteres que deseas para la contraseña :'))
print("El numero de caracteres es: " + str(numero_caracteres)) #Se casteo o se convirtio la variable

numero_contrasenas = int(input(Fore.YELLOW + 'Ingresa el numero de contraseñas a generar:'))
print("se generaran contraseñas" + str(numero_contrasenas))


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
    simbolos = ['!','"','#','$','%','&','/','(',')','=','?','*','[',']','{','}','_','-',':',';',',','.','|','^','~']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = []

    for i in range(numero_caracteres):#Dato dado por el usuario
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    print(Fore.RED + 'Espere un momento \n')
    sleep(0.5)
    print(Fore.YELLOW + 'Generando Passwords ...')
    c = open('archivo.txt', 'a')#generar un archivo y si ya existe sobre escribir en el
    #Buscar soporte para idioma español con simbolos especiales o multi idioma
    can_clave = numero_contrasenas 
    for i in tqdm(range(can_clave)):
        contrasena = generar_contrasena()
        c.write(contrasena + '\n')
    c.close()

    print(Fore.GREEN + '\nProceso Finalizado Happy Hacking :D')


if __name__ == '__main__':
    run()