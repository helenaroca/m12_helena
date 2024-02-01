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
separador(1,"Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
# ############################### 

# ###############################
separador(2,"toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Dias de cada mes
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año y el mes son válidos
    if month < 1 or month > 12 or year < 1:
        return None

    # Verificar febrero en años bisiestos
    if month == 2 and is_year_leap(year):
        return 29

    # Verificar febrero en años no bisiestos
    elif month == 2:
        return 28

    # Devolver el número de días para otros meses
    else:
        return days_per_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
# ############################### 

# ###############################
separador(3,"toma tres argumentos (un año, un mes y un día del mes)")
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Dias de cada mes
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año y el mes son válidos
    if month < 1 or month > 12 or year < 1:
        return None

    # Verificar febrero en años bisiestos
    if month == 2 and is_year_leap(year):
        return 29

    # Verificar febrero en años no bisiestos
    elif month == 2:
        return 28

    # Devolver el número de días para otros meses
    else:
        return days_per_month[month - 1]
# ############################### 

# ###############################
separador(4,"teorema de pitàgores")
def quadrat(num):
    """
    Calcula el quadrat d'un número.
    
    :param num: Número per al qual es vol calcular el quadrat.
    :return: Quadrat del número proporcionat.
    """
    return num ** 2

def arrel(num):
    """
    Calcula l'arrel quadrada d'un número.
    
    :param num: Número per al qual es vol calcular l'arrel quadrada.
    :return: Arrel quadrada del número proporcionat.
    """
    return num ** 0.5

def pitagoras(c, a):
    """
    Calcula la hipotenusa d'un triangle rectangle utilitzant el teorema de Pitàgores.
    
    :param c: Longitud del catet c.
    :param a: Longitud del catet a.
    :return: Longitud de la hipotenusa.
    """
    hipotenusa_quadrat = quadrat(c) + quadrat(a)
    hipotenusa = arrel(hipotenusa_quadrat)
    return hipotenusa

# Exemple d'ús:
catet_c = 3
catet_a = 4
hipotenusa = pitagoras(catet_c, catet_a)
print(f"Per a un triangle rectangle amb catets {catet_c} i {catet_a}, l'hipotenusa és {hipotenusa}")
# ############################### 

# ###############################
separador(5,"primo o no")

def is_prime(num):
    """
    Verifica si un número es primo o no.

    :param num: Número a verificar.
    :return: True si el número es primo, False de lo contrario.
    """
    if num <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Verifica si hay algún divisor en el rango de 2 a la raíz cuadrada del número
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Si encontramos un divisor, el número no es primo

    return True  # Si no se encontraron divisores, el número es primo

# Probamos la función con números del 1 al 20
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

print()
# ############################### 

# ###############################
separador(7,"área circulo")
import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    :param radio: Radio del círculo.
    :return: Área del círculo.
    """
    return math.pi * radio**2

def volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.

    :param radio: Radio de la base del cilindro.
    :param altura: Altura del cilindro.
    :return: Volumen del cilindro.
    """
    area_base = area_circulo(radio)
    volumen = area_base * altura
    return volumen

# Ejemplo de uso:
radio_circulo = 5
altura_cilindro = 10

area_del_circulo = area_circulo(radio_circulo)
volumen_del_cilindro = volumen_cilindro(radio_circulo, altura_cilindro)

print(f"Área del círculo con radio {radio_circulo}: {area_del_circulo}")
print(f"Volumen del cilindro con radio {radio_circulo} y altura {altura_cilindro}: {volumen_del_cilindro}")
# ############################### 

# ###############################
separador(7,"decimal a binario")
def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario.

    :param decimal: Número decimal a convertir.
    :return: Representación binaria del número decimal.
    """
    if decimal < 0:
        return "Solo se admiten números no negativos."

    if decimal == 0:
        return "0b0"

    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return "0b" + binario

def binario_a_decimal(binario):
    """
    Convierte un número binario a decimal.

    :param binario: Número binario a convertir.
    :return: Número decimal.
    """
    if not binario.startswith("0b"):
        return "Formato binario no válido."

    binario = binario[2:]
    decimal = 0
    longitud = len(binario)

    for i in range(longitud):
        bit = int(binario[i])
        exponente = longitud - i - 1
        decimal += bit * (2 ** exponente)

    return decimal

# Ejemplos de uso:
numero_decimal = 23
numero_binario = "0b10111"

resultado_binario = decimal_a_binario(numero_decimal)
resultado_decimal = binario_a_decimal(numero_binario)

print(f"{numero_decimal} en binario: {resultado_binario}")
print(f"{numero_binario} en decimal: {resultado_decimal}")
# ############################### 

# ###############################
separador(7,"treu vocals")
def es_vocal(letra):
    """
    Verifica si una letra es vocal.

    :param letra: Letra a verificar.
    :return: True si es vocal, False de lo contrario.
    """
    vocales = "aeiouAEIOU"
    return letra in vocales

def treu_vocals(palabra):
    """
    Elimina las vocales de una palabra.

    :param palabra: Palabra de entrada.
    :return: Palabra sin vocales.
    """
    return ''.join(letra for letra in palabra if not es_vocal(letra))

def treu_consonants(palabra):
    """
    Elimina las consonantes de una palabra.

    :param palabra: Palabra de entrada.
    :return: Palabra sin consonantes.
    """
    return ''.join(letra for letra in palabra if es_vocal(letra))

# Ejemplos de uso:
palabra_entrada = "HolaMundo"

palabra_sin_vocales = treu_vocals(palabra_entrada)
palabra_sin_consonantes = treu_consonants(palabra_entrada)

print(f"Palabra original: {palabra_entrada}")
print(f"Palabra sin vocales: {palabra_sin_vocales}")
print(f"Palabra sin consonantes: {palabra_sin_consonantes}")
