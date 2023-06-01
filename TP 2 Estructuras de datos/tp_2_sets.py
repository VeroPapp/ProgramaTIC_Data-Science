#%% 1) Crea un conjunto llamado "frutas" que contenga las siguientes frutas: manzana, plátano, naranja y pera. Imprime en pantalla el conjunto completo.

frutas = {"manzana", "plátano", "naranja", "pera"}

print(frutas)

# %% 2) Crea dos conjuntos: "frutas1" con las frutas manzana, plátano y pera, y "frutas2" con las frutas naranja y sandía. Realiza las siguientes operaciones e imprime los resultados: Unión de los conjuntos frutas1 y frutas2. Intersección de los conjuntos frutas1 y frutas2. Diferencia entre los conjuntos frutas1 y frutas2.

frutas1 = {"manzana", "plátano", "pera"}

frutas2 = {"naranja", "sandía"}

# Usando el operador de unión |
union = frutas1 | frutas2
print(union)

# Usando el método union()
union = frutas1.union(frutas2)
print(union)


# Usando el operador de intersección &
interseccion = frutas1 & frutas2
print(interseccion) #vacio porque no comparten elementos

# Usando el método intersection()
interseccion = frutas1.intersection(frutas2)
print(interseccion) #vacio porque no comparten elementos


# Usando el operador de diferencia -
diferencia = frutas1 - frutas2
print(diferencia) #muestra los elementos que están en el set 1 pero no en el 2

# Usando el método difference()
diferencia = frutas1.difference(frutas2)
print(diferencia)

#%% 3) Crea un conjunto vacío llamado "numeros". Agrega los números del 1 al 5 al conjunto utilizando el método add(). Elimina el número 3 del conjunto utilizando el método remove() o discard(). Imprime en pantalla el conjunto resultante.

numeros = set() #para crear un conjunto vacio

for i in range(1, 6):
    numeros.add(i)

numeros.discard(2)

print(numeros)

# %% 4) Crea un conjunto llamado "vocales" que contenga las vocales del alfabeto. Pide al usuario que ingrese una letra y verifica si esa letra está presente en el conjunto "vocales". Muestra un mensaje en pantalla indicando si la letra es una vocal o no.

vocales = {"a", "e", "i", "o", "u"}

letra = input("Ingrese una letra: ")

if letra in vocales:
    print(f"La letra {letra} es una vocal ")
else:
    print(f"La letra {letra} no es una vocal")

# %% 5) Crea una lista llamada "numeros_repetidos" que contenga números repetidos. Convierte la lista en un conjunto utilizando la función set() para eliminar los elementos duplicados. Convierte el conjunto resultante nuevamente en una lista y muéstrala en pantalla.

numeros_repetidos = [2, 5, 3, 2, 6, 6, 8, 5]

conjunto_numeros_repetidos = set(numeros_repetidos)

numeros_sin_repetir = list(conjunto_numeros_repetidos)

print(numeros_sin_repetir)

# %% 6) Crea dos conjuntos: "set1" con los números del 1 al 5, y "set2" con los números del 4 al 8. Utiliza los métodos de conjuntos para realizar las siguientes operaciones e imprime los resultados: Obtener la diferencia simétrica entre set1 y set2. Comprobar si set1 es un subconjunto de set2. Comprobar si set2 es un subconjunto propio de set1.

set1 = {1, 2, 3, 4, 5}

set2 = {4, 5, 6, 7, 8}

diferencia_simetrica = set1 ^ set2

print(diferencia_simetrica)

es_subconjunto = set1.issubset(set2)
#TRUE si es set1 es subconjunto de set2 // FALSE si no lo es

print(es_subconjunto)

es_subconjunto_propio = set2.issubset(set1) and set1 != set2

print(es_subconjunto_propio)

# %% 7) Crea dos conjuntos llamados "set_a" y "set_b" con elementos en común. Utiliza un método de conjuntos para eliminar los elementos comunes de set_a en relación con set_b. Imprime en pantalla el conjunto resultante de set_a.

set_a = {1, 2, 3, 4, 5, 6}

set_b = {5, 6, 7, 8, 9}

set_a.difference_update(set_b)

print(set_a)

# %%
