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

def day_of_year(year, month, day):
#
# Escribe tu código nuevo aquí.
#

print(day_of_year(2000, 12, 31))
