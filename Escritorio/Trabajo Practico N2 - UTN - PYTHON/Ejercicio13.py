#Pedir el ingreso de dos cadenas por teclado, indicar si la segunda cadena se encuentra dentro de la primera.

cadena1 = input("ingrese la primer cadena: ")
cadena2 = input( "ingrese la segunda cadena ")

if cadena2 in cadena1:
    print(f"la cadena {cadena2} se encuentra en la cadena {cadena1}")
else:
    print(f"la cadena {cadena2} no se encuentra en la cadena {cadena1}")
