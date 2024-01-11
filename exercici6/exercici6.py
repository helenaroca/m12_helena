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
# ############################### 

# ###############################
separador(2,"Beatles")

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

for i in range(2):  # Puedes ajustar el rango según la cantidad de miembros que desees agregar
    nombre = input("Ingrese el nombre del miembro de la banda (Stu Sutcliffe, y Pete Best, individualmente): ")
    beatles.append(nombre)

print(beatles)

print("eliminar Stu i Pete")

del beatles[-1]
del beatles[-1]

print(beatles)

print("Inserir Ringo Starr")

beatles.insert(0, "Ringo Starr")

print(beatles)
# ############################### 

# ###############################
separador(3,"ordenamiento borbuja")
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambiar elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]

valores = []
while True:
    valor = input("Ingrese un valor (o escriba 'fin' para finalizar): ")
    
    if valor.lower() == 'fin':
        break
    
    # Añadir el valor a la lista
    try:
        valores.append(int(valor))
    except ValueError:
        print("Por favor, ingrese un valor numérico o escriba 'fin' para finalizar.")

print ("a ordenar", valores)

ordenamiento_burbuja(valores)

print("ordenat", valores)
# ############################### 

# ###############################
separador(4,"ninguna repetición")
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
print("la lista")

print(my_list)

unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)
#crea una lista temporal llamada unique_list e itera sobre la lista original (my_list). Si el elemento no está presente en la lista temporal, se agrega a ella.

print("La lista con elementos únicos:")

print(unique_list)
# ############################### 

# ###############################
separador(5,"primitiva")
nombres_loteria = []

for i in range(6):
    usuari = input("6 nombres ganadores de la primitiva: ")
    nombre = usuari
    nombres_loteria.append(nombre)

nombres_loteria.sort()

nombres_loteria.reverse()

print(nombres_loteria)
# ############################### 

# ###############################
separador(6,"Asignaturas")
asignaturas = ["Mates", "Fisq", "quim", "hist", "leng"]
asig_rep = []
for notas in asignaturas:
    print(notas)
    nota = float(input("Que nota has sacado? "))
    if nota < 5:
        asig_rep.append(notas)
print(asig_rep)
# ############################### 

# ###############################
separador(6,"palindromo")
normal = input("digues una paraula ")

inversa = normal [::-1]
if inversa == normal:
    print("ES palíndromo")
else:
    print("NO es palíndromo")



