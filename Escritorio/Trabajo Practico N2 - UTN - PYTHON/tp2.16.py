def contiene_numeros(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False

# Ejemplo de uso:
cadena = "Hola123"
resultado = contiene_numeros(cadena)
print("¿La cadena contiene números?", resultado)
