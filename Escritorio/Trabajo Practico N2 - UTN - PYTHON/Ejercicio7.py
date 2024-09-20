#Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas 
#vocales tiene en total.
cad=input("Ingrese una cadena de caracteres porfavor ")
vocales="aeiouAEIOU"
longitud_cad=len(cad) #La funcion len retorna el numero de elementos de una secuencia.
num_vocales=0
for caracter in cad: #recorremos la cadena caracter por caracter
    if caracter in vocales: #nos fijamos si el caracter esta tambien en la cadena de vocales
        num_vocales+=1 #si coinciden sumamos el contador de vocales

print("El tamaño de la cadena es de ",longitud_cad," caracteres y tiene ",num_vocales," vocales")
