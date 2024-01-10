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

'''# ###############################
separador(1,"Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1")
# número natural
numero = int(input("Ingrese un número natural: "))

if numero <= 0:
    print("Por favor, ingrese un número natural mayor que 0.")
else:
    lista = []
    while numero != 1:
        lista.append(numero)
        numero = numero // 2 if numero % 2 == 0 else 3 * numero + 1
    lista.append(numero) 

    pasos = len(lista) - 1
    print(f"Secuencia de Collatz: {lista}")
    print(f"Se necesitaron {pasos} pasos para alcanzar 1.")
# ############################### 

# ###############################
separador(1.2,"sombrerero")
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

print (hat_list)

n3 = int(input("Di un número para poner en el centro: "))

hat_list[2] = n3

print(hat_list)

#reemplazar el número de en medio con un número entero ingresado por el usuario.
print ("eliminamos el último")

del hat_list[-1]

print(hat_list)
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

print ("Longitud")

print (len(hat_list))
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print(hat_list)
# ############################### '''

# ###############################
separador(2,"Beatles")

beatles = []

beatles.append("John Lennon", "Paul McCartney", "George Harrison")
