#%% 1) Crea un diccionario llamado "alumno" que contenga las siguientes claves: "nombre", "edad" y "carrera". Asigna valores adecuados a cada clave. Imprime en pantalla la información del alumno utilizando las claves del diccionario.

alumno = {
    "nombre": "Vero",
    "edad": 28,
    "carrera": "Tecnicatura en Análisis de sistemas"
}

print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])
print("Carrera:", alumno["carrera"])

# %% 2) Modifica el valor de la clave "edad" en el diccionario "alumno" y actualízalo con una nueva edad. Imprime en pantalla la información actualizada del alumno.

alumno = {
    "nombre": "Vero",
    "edad": 28,
    "carrera": "Tecnicatura en Análisis de sistemas"
}

alumno["edad"] = 22

print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])
print("Carrera:", alumno["carrera"])

# %% 3) Agrega una nueva entrada al diccionario "alumno" con la clave "universidad" y un valor correspondiente a la universidad en la que estudia. Imprime en pantalla la información completa del alumno, incluyendo la nueva entrada.

alumno = {
    "nombre": "Vero",
    "edad": 22,
    "carrera": "Tecnicatura en Análisis de sistemas"
}

alumno["universidad"] = "ISFT Nro 151"

print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])
print("Carrera:", alumno["carrera"])
print("Universidad:", alumno["universidad"])

# %% 4) Crea un diccionario llamado "calificaciones" que contenga las claves "matemáticas", "física" y "química", y asigna valores numéricos a cada una. Utiliza un bucle para recorrer el diccionario e imprimir en pantalla cada clave y su respectivo valor.

calificaciones = {
    "matematicas": 7,
    "fisica": 6,
    "quimica": 8,
}

for materia, nota in calificaciones.items():
    print(materia + ":", nota)

# %% 5) En base al ejercicio 4, elimina la entrada correspondiente a la clave "química" del diccionario "calificaciones". Vuelve a recorrer el diccionario y muestra en pantalla las claves y valores restantes.

calificaciones = {
    "matematicas": 7,
    "fisica": 6,
    "quimica": 8,
}

del calificaciones["quimica"]

for materia, nota in calificaciones.items():
    print(materia + ":", nota)

# %% 6) En base al ejercicio 4, utiliza el método keys() para obtener una lista de todas las claves del diccionario "calificaciones". Utiliza el método values() para obtener una lista de todos los valores del diccionario.

calificaciones = {
    "matematicas": 7,
    "fisica": 6,
}

# Obtener lista de claves
lista_claves = list(calificaciones.keys())
print("Lista de claves:", lista_claves)

# Obtener lista de valores
lista_valores = list(calificaciones.values())
print("Lista de valores:", lista_valores)

# %% 7) Crea un diccionario llamado "agenda" que contenga información de contactos. Cada contacto debe ser representado por un diccionario con claves como "nombre", "teléfono" y "email". Agrega al menos tres contactos al diccionario "agenda" y muestra la información de cada contacto en pantalla.

agenda = {
    "contacto1": {
        "nombre": "Vero",
        "telefono": 463749,
        "email": "papp.veronica@gmail.com"
    }, #no olvidar la coma

    "contacto2": {
        "nombre": "Alexis",
        "telefono": 466044,
        "email": "aminjolou@gmail.com"
    }, 

    "contacto3": {
        "nombre": "Gerardo",
        "telefono": 465970,
        "email": "gerardopapp@gmail.com"
    }
}

for contacto, info in agenda.items():
    print(f"Información de {contacto}:")
    print("Nombre:", info["nombre"])
    print("Teléfono:", info["telefono"])
    print("Email:", info["email"])
    print() #para que imprima un espacio entre cada contacto

