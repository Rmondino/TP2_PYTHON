def leer_caracteres(cadena, i=0):
    
    if i == len(cadena):
        return
    
    print(cadena[i])
    leer_caracteres(cadena, i + 1)


entrada = input("Ingrese una cadena de texto: ")
leer_caracteres(entrada)
