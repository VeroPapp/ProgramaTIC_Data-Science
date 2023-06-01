#%% 5) Ingresar 10 valores, indicar para cada uno su paridad, y al final indicar cuántos pares y cuantos impares hubo.
num_pares = 0
num_impares = 0

for i in range (10):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        num_pares += 1
        print(f"El número {num} es par.")
    else:
        num_impares += 1
        print(f"El número {num} es impar.")

print(f"\nEn total, se escribieron {num_pares} números pares.")
print(f"En total, se escribieron {num_impares} números impares.")

#%% 6) Generalizar el punto anterior para ingresar N valores, indicar de cada uno su paridad, y al final indicar cuántos pares y cuantos impares hubo.
num_pares = 0
num_impares = 0

n = int(input("Ingrese la cantidad de números a ingresar: "))

for i in range (n):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        num_pares += 1
        print(f"El número {num} es par.")
    else:
        num_impares += 1
        print(f"El número {num} es impar.")

print(f"\nEn total, se escribieron {num_pares} números pares.")
print(f"En total, se escribieron {num_impares} números impares.")
#%% 7) Ingresar 10 valores por teclado. Indicar cuál fue el mayor y cuál fue el menor

#empieza con una lista vacia
numeros = [] 

for i in range(10):
    #pide un valor para la variable num
    num = int(input(f"Ingrese un número: "))
    #a la lista numeros le agrega al final el numero que ingreso el usuario
    numeros.append(num)

mayor = max(numeros) #busca el numero mayor dentro de la lista numeros
menor = min(numeros) #busca el numero menor dentro de la lista numeros

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")

#%% 8) Indicar por teclado cuántos números deben ingresarse, ingresarlos y luego calcular la suma o multiplicación de los mismos.

numeros = []

n = int(input("Ingrese la cantidad de números a ingresar: "))

for i in range(n):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

opcion = int(input("Ingrese 1 para sumar los números o 2 para multiplicarlos: "))

if (opcion == 1):
    suma = sum(numeros)
    print(f"La suma de los números ingresados es: {suma}")
else:
    if (opcion == 2):
        multiplicacion = 1
        for num in numeros:
            multiplicacion *= num
        print(f"La multiplicación de los números ingresados es: {multiplicacion}")
    else:
        print("La opción ingresada es inválida.")



# %% 9) Ingresar por teclado usuario y contraseña. Debe indicar si el usuario ingresado es correcto o no.

#diccionario que contiene los nombres de usuario y sus contraseñas
usuarios = { 
    "vero_papp": "programatic2023",
    "usuario2": "programatic2023",
    "usuario3": "programatic2023",
    "usuario4": "programatic2023",
}

#se solicita al usuario que ingrese su nombre de usuario
nombre_usuario = input("Ingrese el usuario: ")

#verifica que el usuario sea correcto
if nombre_usuario in usuarios:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == usuarios[nombre_usuario]:
        print("Inicio de sesión exitoso.")
    else: 
        print("Contrseña incorrecta.")
else:
    print("Nombre de usuario incorrecto.")


# %% 10) Realizar un programa que solicite números y finalice al ingresar un valor 0. Al terminar indicar la sumatoria total.

num = int(input("Ingrese un número (0 para finalizar): "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número (0 para finalizar): "))

print(f"La suma de todos los números introducidos es {suma}")

# %% 11) Realizar un programa que permita ingresar el monto mensual de ventas realizadas por un comercio durante el año (un ingreso por mes). A su vez ingresar gasto por mes. Calcular: a) Facturación anual b) Ganancia mensual c) Ganancia promedio

ventas_anuales = 0
gastos_anuales = 0

for mes in range(1, 13):
    ventas_mes = float(input(f"Ingrese el monto de ventas para el mes {mes}: "))
    gastos_mes = float(input(f"Ingrese el monto de gastos para el mes {mes}: "))

    ventas_anuales += ventas_mes
    gastos_anuales += gastos_mes

facturacion_anual = ventas_anuales

ganancia_mensual = ventas_anuales / 12 - gastos_anuales / 12

ganancia_promedio = facturacion_anual / 12

print(f"\nFacturación anual: ${facturacion_anual}")
print(f"Ganancia mensual: ${ganancia_mensual:.2f}")
print(f"Ganancia promedio: ${ganancia_promedio:.2f}")

#%% 12) Realizar una calculadora que permita ingresar dos valores y la operación a realizar y brinde el resultado en pantalla. El programa no finaliza.

print("==== CALCULADORA ====")

#bucle que no finaliza hasta que no haya un break
while True:
    print("Ingrese el tipo de operación que desea realizar: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input())
    
#verifica que la opcion sea valida antes de seguir
    if opcion <= 4:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))

        if opcion == 1:
            suma = num1 + num2
            print(f"\n{num1} + {num2} = {suma}")
            print()
        elif opcion == 2:
            resta = num1 - num2
            print(f"\n{num1} - {num2} = {resta}")
            print()
        elif opcion == 3:
            multiplicacion = num1 * num2
            print(f"\n{num1} * {num2} = {multiplicacion}")
            print()
        elif opcion == 4:
            division = num1 / num2
            print(f"\n{num1} / {num2} = {division}")
            print()
    else:
        print("\nLa opción elegida es inválida. Intente nuevamente ")
        print()


# %%
