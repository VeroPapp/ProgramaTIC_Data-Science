#%% 1) Escribe una función llamada "saludo" que no reciba parámetros y y muestre el mensaje "¡Hola!". Llama a la función varias veces para probarla.

def saludo():
    print("¡Hola!")

saludo()

saludo()


# %% 2) Escribe una función llamada "saludo" que reciba un nombre como parámetro y muestre el mensaje "¡Hola, [nombre]!". Llama a la función con diferentes nombres para probarla.

def saludo(nombre):
    print("¡Hola, " + nombre + "!")

saludo("Vero")

saludo("Alexis")

# %% 3) Crea una función llamada "suma" que reciba dos números como parámetros y devuelva la suma de ambos. Llama a la función con diferentes pares de números e imprime el resultado.

def suma(num1, num2):
    suma = num1 + num2
    return suma

resultado_suma = suma(2, 5)

print(resultado_suma)

resultado_suma = suma(8, 2)

print(resultado_suma)

resultado_suma = suma(5.5, 30)

print(resultado_suma)

# %% 4) Define una función llamada "saludo_personalizado" que reciba un nombre y un saludo opcionalmente. Si no se proporciona un saludo, debe utilizar "¡Hola" como saludo predeterminado. Llama a la función para saludar a diferentes personas con y sin saludo personalizado.

def saludo_personalizado (nombre, saludo = "¡Hola"):
    print(f"{saludo}, {nombre}!")

saludo_personalizado("Vero")

saludo_personalizado("Vero", "Buen día")

# %% 5) Escribe una función llamada "promedio" que acepte una cantidad variable de números y calcule su promedio. Llama a la función con diferentes conjuntos de números y muestra el promedio resultante.

def promedio (*numeros):
    suma =0
    cant_num = 0

    for num in numeros:
        suma += num
        cant_num += 1
    
    promedio = suma / cant_num

    print(f"El promedio de los numeros ingresados es: {promedio}")

promedio(2, 5, 6, 3, 2)
promedio(5,2,5)

# %% 6) Crea una función llamada "factorial" que calcule el factorial de un número dado. Utiliza la recursividad para implementar la función. Prueba la función con diferentes números y muestra los resultados.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

resultado = factorial(4)
print(f"El factorial del número ingresado es: {resultado}")

resultado = factorial(8)
print(f"El factorial del número ingresado es: {resultado}")

# %% 7) Escribe una función llamada "ordenar_lista" que reciba una lista de números y devuelva una nueva lista con los mismos números ordenados de forma ascendente. Utiliza una función integrada de Python para realizar la clasificación. Prueba la función con diferentes listas de números.

def ordenar_lista (numeros):
    return sorted(numeros)

lista1 = [5, 6, 2, 15, 22, 3, 8]

lista1_ordenada = ordenar_lista(lista1)

print(lista1_ordenada)

lista2 = [22, 2, 4, 15, 99, 54, 20]

lista2_ordenada = ordenar_lista(lista2)

print(lista2_ordenada)

# %% 8) Define una función llamada "dividir" que acepte dos números y realice la división del primero por el segundo. Maneja la excepción que se produce cuando el divisor es igual a cero y muestra un mensaje de error adecuado. Llama a la función con diferentes pares de números, incluido el caso en el que el divisor sea cero.

def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

print(dividir(10, 2))
print(dividir(15, 0))
print(dividir(50, 5))

# %% 9) Crea una función llamada "informacion_persona" que acepte los siguientes parámetros: nombre, edad y ciudad. La función debe imprimir en pantalla la información proporcionada en un formato legible, como "Nombre: [nombre], Edad: [edad], Ciudad: [ciudad]". Llama a la función utilizando argumentos de palabras clave para especificar los valores de los parámetros.

def informacion_persona(nombre, edad, ciudad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print()

informacion_persona(nombre = "Vero", edad = 28, ciudad = "Mar del plata")

informacion_persona(nombre = "Alexis", edad = 28, ciudad = "Villa Gesell")

# %% 10) - repetido punto 8

#%% 11) Define una función llamada "concatenar_strings" que acepte una cantidad variable de cadenas de texto y las concatene en una sola cadena. Utiliza el operador de concatenación de cadenas o el método join() para realizar la concatenación. Prueba la función con diferentes cadenas y muestra el resultado.

def concatenar_strings(*cadenas):
    # Usando el método join()
    resultado = "".join(cadenas)
    return resultado

print(concatenar_strings("Hola", " ", "Mundo")) 
print(concatenar_strings("Esto", ", ", "es", " ", "una", " ", "cadena"))  

#%% 12) Escribe una función llamada "eliminar_duplicados" que reciba una lista como parámetro y devuelva una nueva lista que contenga los elementos únicos de la lista original, sin duplicados. Utiliza las propiedades de los conjuntos (set) para eliminar los elementos duplicados. Prueba la función con diferentes listas y muestra el resultado.

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

lista = [1, 1, 2, 6, 2, 8, 6]

eliminar_duplicados(lista)


#%% 13) Crea una función recursiva llamada "fibonacci" que calcule el enésimo número de la secuencia de Fibonacci. La secuencia de Fibonacci comienza con 0 y 1, y cada número siguiente se calcula sumando los dos números anteriores. Prueba la función para obtener diferentes números de la secuencia de Fibonacci.

def fibonacci (n):
    if n <= 0:
        return "El valor de 'n' debe ser mayor que 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#%% 14) Crea una función llamada "generar_numero_aleatorio" que utilice el módulo random de Python para generar un número entero aleatorio entre un rango dado. El rango debe ser especificado como parámetros de la función. Llama a la función para generar diferentes números aleatorios y muestra los resultados.

import random

def generar_numero_aleatorio(inicio, fin):
    numero_aleatorio = random.randint(inicio, fin)
    return numero_aleatorio

print(generar_numero_aleatorio(1, 50))  
print(generar_numero_aleatorio(-10, 10)) 


#%% 15) Escribe una función llamada "contar_lineas" que acepte el nombre de un archivo como parámetro y cuente el número total de líneas en ese archivo. Utiliza el manejo de archivos en Python para abrir y leer el archivo. Llama a la función con diferentes archivos y muestra el número de líneas resultante.

def contar_lineas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            num_lineas = len(lineas)
            return num_lineas
    except FileNotFoundError:
        print("El archivo no existe.")

    except:
        print("Ocurrió un error al leer el archivo.")

print(contar_lineas("ejemplo_de_archivo.txt"))
print(contar_lineas("ejemplo_de_archivo_2.txt"))

#%% 16) Escribe una función llamada "calcular_estadisticas" que reciba una tupla de números como parámetro y devuelva la suma, el promedio y el máximo valor de la tupla. Llama a la función con diferentes tuplas de números y muestra los resultados obtenidos.

def calcular_estadisticas(tupla):
    suma = sum(tupla)
    promedio = suma / len(tupla)
    maximo = max(tupla)
    return suma, promedio, maximo

tupla1 = (1, 2, 3, 4, 5)

resultado1 = calcular_estadisticas(tupla1)

print(f"La suma es: {resultado1[0]}")
print(f"El promedio es: {resultado1[1]}")
print(f"El máximo valor es: {resultado1[2]}")
print()

tupla2 = (10, 15, 20, 25, 30)

resultado2 = calcular_estadisticas(tupla2)

print(f"La suma es: {resultado2[0]}")
print(f"El promedio es: {resultado2[1]}")
print(f"El máximo valor es: {resultado2[2]}")
print()
