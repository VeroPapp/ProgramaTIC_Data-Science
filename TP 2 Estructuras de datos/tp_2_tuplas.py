#%% 1) Crea una tupla llamada "meses" que contenga los nombres de los meses del año como elementos. Imprime en pantalla la tupla completa.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" )

print(meses)

# %% 2) En base al ejercicio 1, acede al tercer elemento de la tupla "meses" e imprímelo en pantalla.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" )

print(meses[2])

# %% 3) Accede al último elemento de la tupla "meses" utilizando indexación negativa. Imprime en pantalla el último elemento.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" )

print(meses[-1])

# %% 4) Intenta asignar un nuevo valor a uno de los elementos de la tupla "meses" y observa el error que se produce. Comenta el código erróneo y explica en un comentario por qué ocurre el error.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" )

meses[2] = "Diciembre2"

print(meses[2])

#TypeError: 'tuple' object does not support item assignment

#Los elementos de las tuplas no se pueden modificar.

# %% 5) Crea dos tuplas llamadas "tupla1" y "tupla2" con diferentes elementos. Concatena las dos tuplas y almacena el resultado en una nueva tupla llamada "tupla_concatenada". Imprime en pantalla la tupla concatenada.

tupla1 = ("rosa", "azul", "blanco", "negro", "celeste")

tupla2 = ("celular", "notebook", "smartwatch", "monitor", "tablet")

tupla_concatenada = tupla1 + tupla2

print(tupla_concatenada)


# %% 6) Crea una tupla llamada "coordenadas" que contenga las coordenadas x, y, z de un punto en el espacio. Utiliza el desempaquetado de tuplas para asignar cada valor de la tupla a variables individuales llamadas "x", "y" y "z". Imprime en pantalla los valores de las variables.

coordenadas = (3.5, -2.2, 1.8)

x, y, z = coordenadas

print (x)
print (y)
print (z)


# %% 7) Crea una lista de tuplas llamada "alumnos" que contenga el nombre y la edad de varios estudiantes. Utiliza un bucle para iterar sobre la lista de tuplas y mostrar en pantalla el nombre y la edad de cada estudiante.

alumnos = [("Vero", 28), ("Alexis", 29), ("Lucia", 26), ("Javier", 33)]

for alumno in alumnos:
    nombre, edad = alumno
    print("Nombre:", nombre)
    print("Edad:", edad)
    print()
