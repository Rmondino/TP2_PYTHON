#Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario 
#pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el 
#resultado por pantalla. 
def convertir_a_mayusculas(cadena):
    cadena=cadena.upper() #funcion predeterminada que convierte a mayusculas un caracter o una cadena
    return cadena
def convertir_a_minusculas(cadena):
    cadena=cadena.lower() #funcion predeterminada que convierte a minusculas un caracter o una cadena
    return cadena

cad=input("Ingrese una cadena de caracteres porfavor ")
respuesta=input("Ingrese el numero de la opcion que prefiere \n 1:Convertir cadena a mayusculas \n 2:Convertir cadena a minusculas ")

while respuesta!="1" and respuesta!="2": #limitamos el ingreso de la respuesta a esas dos opciones
    respuesta=int(input("Ingrese el numero de la opcion que prefiere \n 1:Convertir cadena a mayusculas \n 2:Convertir cadena a minusculas "))

if respuesta=="1": 
    nuevacad=convertir_a_mayusculas(cad)
else:
    nuevacad=convertir_a_minusculas(cad)

print(nuevacad)