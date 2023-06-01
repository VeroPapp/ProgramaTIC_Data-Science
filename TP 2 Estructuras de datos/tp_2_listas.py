#%% 1) Crea una lista llamada "frutas" que contenga las siguientes frutas: manzana, banana, naranja y pera. Imprime en pantalla la lista completa.

frutas = ["manzana", "banana", "naranja", "pera"]

print(frutas)
# %% 2) En base al ejercicio 1, accede al segundo elemento de la lista "frutas" e imprímelo en pantalla.


frutas = ["manzana", "banana", "naranja", "pera"]

print (frutas[1])

# %% 3) En base al ejercicio 1, modifica el primer elemento de la lista "frutas" y cámbialo por "Cereza". Imprime en pantalla la lista actualizada.

frutas = ["manzana", "banana", "naranja", "pera"]

frutas[0] = "cereza"

print(frutas)

# %% 4) En base al ejercicio 1, agrega la fruta "sandía" al final de la lista "frutas" utilizando el método append(). Imprime en pantalla la lista actualizada.

frutas = ["cereza", "banana", "naranja", "pera"]

frutas.append("sandía")

print(frutas)

# %% 5) En base al ejercicio 1, elimina la fruta "naranja" de la lista "frutas" utilizando el método remove(). Imprime en pantalla la lista resultante.

frutas = ["cereza", "banana", "naranja", "pera", "sandía"]

frutas.remove("naranja")

print(frutas)
# %% 6) Crea una lista de números llamada "numeros" con valores del 1 al 5. Utiliza un bucle for para recorrer la lista e imprimir en pantalla cada número.

numeros = [1 , 2 , 3 , 4 , 5]

for numero in numeros:
    print(numero)

# %% 7) Crea una lista llamada "pares" con los números pares del 2 al 10. Utiliza el método reverse() para invertir el orden de los elementos en la lista. Utiliza el método sort() para ordenar la lista de forma ascendente. Imprime en pantalla la lista resultante.

pares = [2, 4, 6, 8 , 10]

pares.reverse()

print(pares)

pares.sort()

print(pares)

# %% 8) Crea una lista llamada "cuadrados" que contenga los cuadrados de los números del 1 al 5. Utiliza la comprensión de listas para generar la lista de forma concisa. Imprime en pantalla la lista resultante.

cuadrados = [num ** 2 for num in range(1, 6)]

print(cuadrados)

# %% 9) Crea una lista llamada "nombres" con varios nombres de personas. Pide al usuario que ingrese un nombre y verifica si está presente en la lista. Muestra un mensaje en pantalla indicando si el nombre está o no en la lista.

nombres = ["Vero", "Alexis", "Martin", "Gerardo", "Lucia", "Luciana", "Sebastian", "Magali", "Alan"]

nombre = input("Ingrese un nombre: ")

if nombre.capitalize() in nombres: #.capitalize() para que ponga la primer letra en mayuscula en caso de que el usuario no lo haga
    print (f"El nombre {nombre} está en la lista.")
else:
    print(f"El nombre {nombre} no está en la lista")

# %% 10) Crea una lista llamada "numeros" con valores del 1 al 10. Divide la lista en sublistas de tamaño 3 utilizando la técnica de slicing. Imprime en pantalla las sublistas resultantes.

# alternativa para crear la lista de números del 1 al 10
numeros = list(range(1, 11))  

# Divide la lista en sublistas de tamaño 3 con la tecnica de slicing
sublista1 = numeros[:3]
sublista2 = numeros[3:6] 
sublista3 = numeros[6:9] 
sublista4 = numeros[9:]

print(sublista1)
print(sublista2)
print(sublista3)
print(sublista4)
# %%
