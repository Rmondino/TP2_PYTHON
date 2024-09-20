#Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e.
def remplazodevocales(cadena):
    vocales="aeiouAEIOU"

    for vocal in vocales: #para cada vocal en la cadena de vocales hacemos el reemplazo por la vocal e con la funcion replace
        cadena=cadena.replace(vocal,'e') #funcion predeterminada que reemplaza un caracter por otro
    return cadena

cad=input("Ingrese una cadena de caracteres porfavor ") 
nuevacad=remplazodevocales(cad) #retornamos la nueva cadena
print(nuevacad)