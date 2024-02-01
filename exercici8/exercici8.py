def separador(exercici, descripcio = None):
    print("\n")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("# Descripció " + str(descripcio)) if descripcio else False
    print("#")
    print("#" * 25)
    print("\n")
# ############################### 

# ###############################
separador(1,"numero entre 1 i 10")
def guardar_tabla_multiplicar():
    try:
        # Solicitar al usuario un número entre 1 y 10
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        
        # Verificar que el número esté en el rango deseado
        if 1 <= numero <= 10:
            # Crear el nombre del archivo
            nombre_archivo = f"tabla-{numero}.txt"

            # Abrir el archivo en modo escritura
            with open(nombre_archivo, 'w') as archivo:
                # Escribir la tabla de multiplicar en el archivo
                for i in range(1, 11):
                    resultado = numero * i
                    archivo.write(f"{numero} x {i} = {resultado}\n")

            print(f"La tabla de multiplicar de {numero} ha sido guardada en {nombre_archivo}.")
        else:
            print("Por favor, introduce un número entre 1 y 10.")
    
    except ValueError:
        print("Error: Debes introducir un número entero.")

# Llamada a la función
guardar_tabla_multiplicar()
# ############################### 

# ###############################
separador(2,"numero entre 1 i 10")
def mostrar_tabla_multiplicar():
    try:
        # Solicitar al usuario un número entre 1 y 10
        numero = int(input("Introduce un número entero entre 1 y 10: "))
        
        # Verificar que el número esté en el rango deseado
        if 1 <= numero <= 10:
            # Crear el nombre del archivo
            nombre_archivo = f"tabla-{numero}.txt"

            try:
                # Intentar abrir y leer el archivo
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                    print(f"Tabla de multiplicar de {numero}:\n{contenido}")
            except FileNotFoundError:
                print(f"El archivo {nombre_archivo} no existe.")
        else:
            print("Por favor, introduce un número entre 1 y 10.")
    
    except ValueError:
        print("Error: Debes introducir un número entero.")

# Llamada a la función
mostrar_tabla_multiplicar()
# ############################### 

# ###############################
separador(2,"dos numeros")
def mostrar_linea_tabla():
    try:
        # Solicitar al usuario dos números entre 1 y 10
        n = int(input("Introduce el primer número entero entre 1 y 10 (n): "))
        m = int(input("Introduce el segundo número entero entre 1 y 10 (m): "))
        
        # Verificar que ambos números estén en el rango deseado
        if 1 <= n <= 10 and 1 <= m <= 10:
            # Crear el nombre del archivo
            nombre_archivo = f"tabla-{n}.txt"

            try:
                # Intentar abrir y leer el archivo
                with open(nombre_archivo, 'r') as archivo:
                    lineas = archivo.readlines()
                    # Verificar que la línea m existe en el archivo
                    if 1 <= m <= len(lineas):
                        linea_m = lineas[m - 1]  # Restamos 1 porque las listas en Python son indexadas desde 0
                        print(f"Línea {m} de la tabla de multiplicar de {n}:\n{linea_m}")
                    else:
                        print(f"La línea {m} no existe en el archivo {nombre_archivo}.")
            except FileNotFoundError:
                print(f"El archivo {nombre_archivo} no existe.")
        else:
            print("Por favor, introduce dos números entre 1 y 10.")
    
    except ValueError:
        print("Error: Debes introducir dos números enteros.")

# Llamada a la función
mostrar_linea_tabla()
# ############################### 

# ###############################
separador(2,"obrir fixer")
import pandas as pd
import requests
from io import StringIO

def obtener_pib_per_capita(url, pais):
    # Descargar el archivo TSV desde la URL y descomprimirlo
    response = requests.get(url)
    content = pd.read_csv(StringIO(response.text), delimiter='\t')

    # Filtrar el DataFrame por el país proporcionado
    datos_pais = content[content['geo'] == pais]

    # Mostrar el PIB per cápita de todos los años disponibles
    if not datos_pais.empty:
        print(f"PIB per cápita de {pais} por año:")
        for index, row in datos_pais.iterrows():
            print(f"Año: {row['time']}, PIB per cápita: {row['Value']} {row['unit']}")
    else:
        print(f"No se encontraron datos para el país {pais}.")

# URL del archivo TSV
url_pib_per_capita = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"

# Solicitar al usuario las iniciales del país
iniciales_pais = input("Introduce las iniciales del país (por ejemplo, 'ES' para España): ").upper()

# Llamar a la función para obtener y mostrar el PIB per cápita
obtener_pib_per_capita(url_pib_per_capita, iniciales_pais)
# ############################### 

# ###############################
separador(2,"listin telefonico")
import os

def crear_listin():
    # Crea el fichero listin.txt si no existe
    if not os.path.exists("listin.txt"):
        with open("listin.txt", "w"):
            pass  # Fichero creado

def consultar_telefono(nombre):
    try:
        # Lee el fichero listin.txt y busca el teléfono del cliente
        with open("listin.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(',')
                if datos[0] == nombre:
                    return datos[1]
        return f"No se encontró el teléfono para {nombre}."
    except FileNotFoundError:
        return "El fichero listin.txt no existe."

def agregar_cliente(nombre, telefono):
    try:
        # Abre el fichero listin.txt en modo append y añade el nuevo cliente
        with open("listin.txt", "a") as f:
            f.write(f"{nombre},{telefono}\n")
        return f"Cliente {nombre} añadido correctamente."
    except FileNotFoundError:
        return "El fichero listin.txt no existe."

def eliminar_cliente(nombre):
    try:
        # Lee el fichero listin.txt, crea un nuevo contenido sin el cliente a eliminar y guarda el nuevo contenido
        with open("listin.txt", "r") as f:
            lineas = f.readlines()

        with open("listin.txt", "w") as f:
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0] != nombre:
                    f.write(linea)
        return f"Cliente {nombre} eliminado correctamente."
    except FileNotFoundError:
        return "El fichero listin.txt no existe."

# Ejemplo de uso:
crear_listin()

# Consultar teléfono
nombre_a_buscar = input("Introduce el nombre del cliente para consultar el teléfono: ")
resultado_consulta = consultar_telefono(nombre_a_buscar)
print(resultado_consulta)

# Agregar nuevo cliente
nombre_nuevo_cliente = input("Introduce el nombre del nuevo cliente: ")
telefono_nuevo_cliente = input("Introduce el teléfono del nuevo cliente: ")
resultado_agregar = agregar_cliente(nombre_nuevo_cliente, telefono_nuevo_cliente)
print(resultado_agregar)

# Eliminar cliente
nombre_cliente_a_eliminar = input("Introduce el nombre del cliente a eliminar: ")
resultado_eliminar = eliminar_cliente(nombre_cliente_a_eliminar)
print(resultado_eliminar)
# ############################### 

# ###############################
separador(2,"usuari i contrasenya")
import re

def mostrar_menu():
    print("Menú:")
    print("1. Registrarse")
    print("2. Login")
    print("3. Salir")

def pedir_usuario_contraseña():
    usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")
    return usuario, contraseña

def validar_usuario(usuario):
    return len(usuario) >= 6

def validar_contraseña(contraseña):
    return len(contraseña) >= 8 and re.search("[a-z]", contraseña) and re.search("[A-Z]", contraseña)

def registrar_usuario():
    while True:
        usuario, contraseña = pedir_usuario_contraseña()

        if validar_usuario(usuario) and validar_contraseña(contraseña):
            with open("users.txt", "a") as archivo:
                archivo.write(f"{usuario},{contraseña}\n")
            print("Usuario registrado exitosamente.")
            break
        else:
            print("Error: Nombre de usuario o contraseña no válidos. Inténtalo de nuevo.")

def login():
    while True:
        usuario, contraseña = pedir_usuario_contraseña()

        with open("users.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')
                if datos[0] == usuario and datos[1] == contraseña:
                    print("Estás dentro!")
                    return

        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")

def main():
    while True:
        mostrar_menu()

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
