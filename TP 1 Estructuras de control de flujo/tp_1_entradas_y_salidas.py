#%% 1) Ingresar un valor por teclado y avisar por consola si es positivo o negativo
numero = int(input("Ingrese un número: "))

if (numero > 0):
    print(f"El número {numero} es positivo.")
else:
    print (f"El número {numero} es negativo.")   

#%% 2) Ingresar el radio de un círculo. Indicar en consola su perímetro y superficie.
import math #para usar el pi sin tener que escribir 3.14

radio = float(input("Ingrese el radio de un círculo: "))

perimetro = 2 * math.pi * radio
superficie = math.pi * (radio ** 2) # ** es para calcular potencia

print(f"El perímetro del círculo es: {perimetro:.2f}") # :.2 es para limitar los decimales a 2
print(f"La superficie del círculo es: {superficie:.2f}") # la f indica que la cadena es una f-string y permite la interpolación de variables

#%% 3) Ingresar un valor por teclado y avisar por consola si es par o impar
numero = int(input("Ingrese un número: "))

if (numero % 2 == 0):
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

#%% 4) Realizá un programa que permita resolver el siguiente problema: cuatro personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje). Solicitar la carga por teclado del nombre de cada socio, su capital aportado y a partir de esto calcular e informar lo requerido previamente.

socio1 = input("Ingrese el nombre del socio: ")
apSocio1 = int(input(f"Ingrese el valor aportado por {socio1}: "))

socio2 = input("Ingrese el nombre del socio: ")
apSocio2 = int(input(f"Ingrese el valor aportado por {socio2}: "))

socio3 = input("Ingrese el nombre del socio: ")
apSocio3 = int(input(f"Ingrese el valor aportado por {socio3}: "))

socio4 = input("Ingrese el nombre del socio: ")
apSocio4 = int(input(f"Ingrese el valor aportado por {socio4}: "))

total_aportado = apSocio1 + apSocio2 + apSocio3 + apSocio4

print(f"El total aportado por los socios es de {total_aportado}.")
print(f"{socio1} aporto un {((apSocio1/total_aportado)*100):.2f}%")
print(f"{socio2} aporto un {((apSocio2/total_aportado)*100):.2f}%")
print(f"{socio3} aporto un {((apSocio3/total_aportado)*100):.2f}%")
print(f"{socio4} aporto un {((apSocio4/total_aportado)*100):.2f}%")
