import os
from colorama import Fore, init

# Inicializar colorama para que los colores funcionen en todos los sistemas
init(autoreset=True)

def mostrar_banner():
    banner = r"""
 ____   __   ____  _  _         ___  ____  ____   __   ____  ____ 
(  _ \ / _\ / ___)/ )( \       / __)(  _ \(  __) / _\ (_  _)(  __)
 ) _ (/    \\___ \) __ (      ( (__  )   / ) _) /    \  )(   ) _) 
(____/\_/\_/(____/\_)(_/       \___)(__\_)(____)\_/\_/ (__) (____)                                        
    """
    print(Fore.LIGHTYELLOW_EX + banner)
    print(Fore.LIGHTYELLOW_EX + "Creado para los poco conocedores de bash")
    print(Fore.LIGHTYELLOW_EX + "      Creado por: dev-Thomas")
    print(Fore.LIGHTYELLOW_EX + "      Versión: 1.0 \n      test-code")
    print("\n")

def mostrar_menu():
    print(Fore.LIGHTYELLOW_EX + "Selecciona una opción:")
    print(Fore.LIGHTYELLOW_EX + "1. Crear un archivo")
    print(Fore.LIGHTYELLOW_EX + "2. Leer un archivo")
    print(Fore.LIGHTYELLOW_EX + "3. Salir")

def crear_archivo():
    # Solicitar la extensión del archivo
    extension = input(Fore.LIGHTYELLOW_EX + "Ingresa la extensión del archivo (por ejemplo, txt, csv, json, etc.): ")
    
    # Solicitar la ruta del archivo
    ruta_directorio = input(Fore.LIGHTYELLOW_EX + "Ingresa la ruta donde deseas guardar el archivo (por ejemplo, /ruta/al/directorio/): ")
    
    # Verificar si el directorio existe, si no, crearlo
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)
    
    # Solicitar el nombre del archivo (sin extensión)
    nombre_archivo = input(Fore.LIGHTYELLOW_EX + "Ingresa el nombre del archivo (sin la extensión): ")
    
    # Combinar la ruta, el nombre y la extensión
    ruta_completa = os.path.join(ruta_directorio, f"{nombre_archivo}.{extension}")
    
    # Solicitar el contenido del archivo
    contenido = input(Fore.LIGHTYELLOW_EX + "Ingresa el contenido del archivo: ")
    
    # Crear el archivo y escribir el contenido
    with open(ruta_completa, 'w') as archivo:
        archivo.write(contenido)
    
    print(Fore.LIGHTYELLOW_EX + f"Archivo creado exitosamente en: {ruta_completa}\n")

def leer_archivo():
    ruta_archivo = input(Fore.LIGHTYELLOW_EX + "Ingresa la ruta completa del archivo que deseas leer: ")
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(Fore.LIGHTYELLOW_EX + f"Contenido del archivo '{ruta_archivo}':\n{contenido}\n")
    except FileNotFoundError:
        print(Fore.RED + f"El archivo '{ruta_archivo}' no existe.\n")

def main():
    mostrar_banner()
    while True:
        mostrar_menu()
        opcion = input(Fore.LIGHTYELLOW_EX + "Opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            leer_archivo()
        elif opcion == "3":
            print(Fore.LIGHTYELLOW_EX + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()