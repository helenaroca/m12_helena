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
separador(1, "progrmama que cuente hasta 5")
import time

for i in range (1,6): # Escribe un bucle for que cuente hasta cinco.
    print(f"{i} Missisipi") # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    time.sleep(1) # Cuerpo del bucle - usar: time.sleep (1)

print("molt bé")# Escribe una función de impresión con el mensaje final.
# ############################### 

# ###############################
separador(2, "programa bucle hasta que ponga chupacabra")
while True:
    palabra = input("ingrese una palabra ")
    if palabra == "chupacabra":
        print ("has dejado el bucle con exito")
        break
# ############################### 

# ###############################
separador(3, "devorador de vocales")

user_word = input("Ingresa una palabra: ")


user_word = user_word.upper()


for letra in user_word:

    if letra in "AEIOU":

        continue

    print(letra)
# ############################### 

# ###############################
separador(4, "devorador de vocales (bonito)")

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:

    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue

    word_without_vowels += letter


print("Palabra sin vocales:", word_without_vowels)
# ############################### 

# ###############################
separador(5, "iversion cada año")

invertir = float(input("cantidad a invertir: "))
interes = int(input("interes anual: "))
anys = int(input("nuero de años: "))
interes_dec= interes/100
capital = invertir * (1 + interes_dec)**anys
print(f"el capital és {capital}")
# ############################### 

# ###############################
separador(6.1, "triangulo rectangulo")

altura = int(input("Introduce un número entero: "))

for i in range(1, altura + 1):
    print('* ' * i)
# ############################### 

# ###############################
separador(6.2, "triangulo rectangulo num")

altura = int(input("Introduce un número entero: "))

for j in range(1, altura + 1):
    for k in range (j, 0, -2):
        print(k, end=' ')
    print()
# ############################### 

# ###############################'''
separador(7, "primo o no")

num = int(input("Introduce un número entero: "))

if num <2:
    print(f"{num} no es primo")
else:
    es_primo = True 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
# ############################### 

# ###############################
separador(8, "palabra")
palabra = (input("escribe una palabra: "))
for i in reversed (palabra):
    print (i)
# ############################### 

# ###############################
separador(9, "frase i letra")
frase = (input("escribe una frase: "))
letra = (input("dime una letra de la frase: "))
contador = 0 
for caracter in frase: 
    if caracter == letra :
        contador += 1
print ("la letra", (letra), "aparece", (contador), "veces en la frase" )
# ############################### 

# ###############################
separador(10, "piramide")
blocks = int(input("Ingresa el número de bloques: "))

height = 0 
blocks_used = 0 

while blocks_used <= blocks:
    height += 1
    blocks_in_layer = height 
    blocks_used += blocks_in_layer

print("La altura de la pirámide:", height-1)
