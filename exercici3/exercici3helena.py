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
separador(1, "Escribir un programa que pregunte el nombre del usuario")

nombre = input("Quin és el teu nom? ")
print("Hola",nombre,"!")##per ficar una variable separar-ho amb comes

# ###############################
separador(2, "crear variables i sumar les pomes")

juan=3
maria=5
adan=6
print(juan,maria,adan, sep=",")##como sumar las manzanas
total_manzanas=(juan+maria+adan)
print(total_manzanas)
peras=(adan-maria*juan)
print(peras, "Las peras del suelo")##inventada total

# ###############################
separador(3, "No se debe cambiar el código existente peró que pase de km a millas i diceversa ")

umillas= int(input("Dime un número de millas: "))
ukilometros= int(input("Dime un número de kilometros: "))

miles_to_kilometers = umillas * 1.61 ##1milla són 1.61km
kilometers_to_miles = ukilometros / 1.61

print(umillas, "Millas son", round(miles_to_kilometers, 2), "kilómetros")
print(ukilometros, "Kilómetros son", round(kilometers_to_miles, 2), "millas")

# ###############################
separador(4," 3x3 - 2x2 + 3x - 1 el resultado debe ser asignado a y"
)

x = float(input("Introduce un valor para x: "))

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

print("El resultado de la expresión es:", y)
# ###############################
separador(5, "Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.")

horas= int(input("Cuantas horas has trabajado? "))
coste= int(input("Cuanto te pagan por hora? "))
sueldo= horas*coste
print("Has cobrado", sueldo, "manzanas")

# ###############################
separador(6, "Escribir un programa que lea un entero positivo")

enterUsuari = int(input("Escriu un enter: "))

total = 0
for n in (range(1, enterUsuari + 1 )):
     print("-------------------")
     print(f"total: {total}")
     print(f"n: {n}")
     print(f"{total}+= {n}")

     total += n/2

print(f"El total es {total}")

# ###############################
separador(7, "Escribir un programa  que pida al usuario su peso y estatura")

kg = float(input("dime tu peso en kg: "))
metros = int(input("dime tu estatura en metros: "))
imc = kg/metros**2
print(f"tu imc es de {imc}")
 # ###############################
separador(8, "Escribir un programa que pregunte al usuario una cantidad a invertir")

invertir = float(input("cantidad a invertir: "))
interes = int(input("interes anual: "))
anys = int(input("nuero de años: "))
interes_dec= interes/100
capital = invertir * (1 + interes_dec)**anys
print(f"el capital és {capital}")

 # ###############################
separador(9, "escribe un programa que imprima una ip")

uno = int(input("di un numero entre 0-255: "))
dos = int(input("di un numero etre 0-255: "))
tres = int(input("di un numero entre 0-255: "))
cuatro = int(input("di un numero entre 0-255: "))
print( uno,dos,tres,cuatro, sep=".")
 # ###############################

separador(10, "La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado")

print ("Part 1:")
hour =int(input("Hora de inicio: "))
mins =int(input("Minuto de inicio: "))
dura =int(input("Duración del evento (minutos): "))
hour_dura = dura // 60
mins_dura = dura % 60
final_h = (hour + hour_dura + (mins + mins_dura) // 60) % 24
final_m = (mins + mins_dura) % 60
dia =int(input("Día: "))
final_d = dia + (hour + hour_dura) // 24
print(f"El evento a comenzando el dia {dia}/{final_d} a las {hour:02d}:{mins:02d} y a durado {dura} minutos, por tanto terminará el dia {final_d} a las {final_h:02d}:{final_m:02d}")