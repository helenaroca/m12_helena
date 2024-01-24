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
'''
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

def valid_date(year, month, day):
    # Verificar si el año, mes y día son válidos
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return False
    else:
        return True

def day_of_year(year, month, day):
    # Verificar la validez de la fecha
    if not valid_date(year, month, day):
        return None

    # Calcular el día del año
    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)

    return day_count

# Ejemplo de uso
print(day_of_year(2000, 1, 31))
# ############################### 

# ###############################
separador(4.1,"teorema de pitàgores")

import math

# Función para calcular el cuadrado de un número
def quadrat(num):
    return num ** 2

# Función para calcular la raíz cuadrada de un número
def arrel(num):
    return math.sqrt(num)

# Función para aplicar el teorema de Pitágoras
def pitagoras(c, a):
    # Calcula el cuadrado de c
    c_quadrat = quadrat(c)
    
    # Calcula el cuadrado de a
    a_quadrat = quadrat(a)
    
    # Calcula la hipotenusa aplicando el teorema de Pitágoras
    hipotenusa = arrel(c_quadrat + a_quadrat)
    
    return hipotenusa

# Ejemplo de uso
catet_c = 5
catet_a = 5
resultat = pitagoras(catet_c, catet_a)

print(f"La hipotenusa del triángulo con catetos {catet_c} y {catet_a} es: {resultat}")
# ############################### 

# ###############################
separador(4.2,"primo")

numero = int(input("digues un número: "))
def is_prime (num):
     for i in range (2,num):
          if num % i == 0:
            return False
          else:
              return True
resultat = is_prime(numero)
print(resultat)

# ############################### '''

# ###############################
separador(5,"automóvil")
def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = 235.214583 / liters
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 235.214583 / miles
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


