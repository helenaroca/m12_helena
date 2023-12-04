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
separador(1, "Tu tarea es escribir una calculadora de impuestos")
income = float(input("Introduce el ingreso anual: "))

if income <= 85528: tax = 0.18 * income - 556.02
else: tax = 1439.02 + 0.32 * (income - 85528)

tax = max(0, tax)

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
# ###############################

# ###############################
separador(2,"Prueba tu código con los datos que hemos proporcionado.")
any = int(input("escriu un any: "))

if any < 1582:
    print("No dentro del período del calendario Gregoriano.")
else:
    if (any % 4 != 0) or (any % 100 == 0 and any % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")
# ###############################

# ###############################
separador(3, "Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código")
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

while True:
    number_user = int(input("escriu un numero: "))
    if secret_number == number_user : 
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
# ###############################

# ###############################
separador(4, "Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar")
number = int(input("escriu un numero enter: "))
if (number % 2 == 0):
    print("par")
else:
    print("impar")
# ###############################

# ###############################
separador(5, "Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no")
edat = int(input("Quina edat tens? "))
ingresos = int(input("Quins son els teus ingresos? "))
print(edat > 16 and ingresos > 1000)
# ###############################

# ###############################
separador(6, "Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde")

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")


nombre = nombre.upper()


if (sexo == 'F' and nombre < 'M') or (sexo == 'M' and nombre > 'N'):
    grupo = 'A'
else:
    grupo = 'B'

print(f"Usted pertenece al grupo {grupo}.")
# ###############################

# ###############################
separador(7, "Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde")
renta_anual = float(input("Ingrese su renta anual en euros: "))

if renta_anual < 10000:
    tipo_impositivo = 0.05 
elif 10000 <= renta_anual <= 20000:
    tipo_impositivo = 0.15  
elif 20000 < renta_anual <= 35000:
    tipo_impositivo = 0.20  
elif 35000 < renta_anual <= 60000:
    tipo_impositivo = 0.30  
else:
    tipo_impositivo = 0.45  

print(f"Su renta anual es de {renta_anual}€ y su tipo impositivo es del {tipo_impositivo * 100}%.")
# ###############################

# ###############################
separador(8, "Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario")
puntuacion = float(input("Ingrese su puntuación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    cantidad_dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    cantidad_dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
else:
    print("Puntuación no válida. Debe ser 0.0, 0.4 o 0.6 o más.")
    exit()  

print(f"Su nivel de rendimiento es {nivel}.")
print(f"Recibirá {cantidad_dinero}€.")
# ###############################

# ###############################
separador(9, "Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar")
edad = int(input("Ingrese su edad: "))
if edad < 4:
    precio = 0
elif edad > 4 < 18:
    precio = 5
elif edad > 18:
    precio = 10
print("el precio és de", (precio))
# ###############################

# ###############################
separador(10, "Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no")
tipo_pizza = input("¿Desea una pizza vegetariana? (Sí/No): ").lower()
ingredientes_base = ["Mozzarella", "Tomate"]

if tipo_pizza == "sí":
    print("Ingredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente_elegido = input("Elige un ingrediente (1 o 2): ")
    if ingrediente_elegido == "1":
        ingredientes = ingredientes_base + ["Pimiento"]
    elif ingrediente_elegido == "2":
        ingredientes = ingredientes_base + ["Tofu"]
    else:
        print("Opción no válida. Seleccionando Pimiento por defecto.")
        ingredientes = ingredientes_base + ["Pimiento"]
else:
    print("Ingredientes no vegetarianos disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    ingrediente_elegido = input("Elige un ingrediente (1, 2 o 3): ")
    if ingrediente_elegido == "1":
        ingredientes = ingredientes_base + ["Peperoni"]
    elif ingrediente_elegido == "2":
        ingredientes = ingredientes_base + ["Jamón"]
    elif ingrediente_elegido == "3":
        ingredientes = ingredientes_base + ["Salmón"]
    else:
        print("Opción no válida. Seleccionando Peperoni por defecto.")
        ingredientes = ingredientes_base + ["Peperoni"]


print("\n¡Has elegido una pizza {}!".format("vegetariana" if tipo_pizza == "sí" else "no vegetariana"))
print("Ingredientes:")
for ingrediente in ingredientes:
    print("- " + ingrediente)
# ###############################

# ###############################
separador(11, "un programa que solicite una IP i determine qué clase es y si es pública o privada")

while True:
    byte1 = int(input("Dime el primer byte: "))
    if byte1 <= 127:
        type = "és type A"
        break
    elif byte1 <= 191:
        type = "és type B"
        break
    elif byte1 <= 223:
        type = "és type C"
        break
    elif byte1 <= 239:
        type = "és type D"
        break
    elif byte1 <= 247:
        type = "és type E"
        break
    else:
        print("Ip no válida. Seleccione otro")
while True:
    byte2 = int(input("Dime el segon byte: "))
    if byte1 == 10 :
        tipus = "privada"
        break
    elif byte1 > 172 and byte2 >= 16 and byte2 <= 31:
        tipus = "privada"
        break
    elif byte1 == 192 and byte2 == 168:
        tipus = "privada"
        break
    else:
        tipus = "pública"
        break
byte3 = int(input("Dime el tercer byte: "))
byte4 = int(input("Dime el cuarto byte: "))
print (f"la ip {byte1} {byte2} {byte3} {byte4} {type} y {tipus}")