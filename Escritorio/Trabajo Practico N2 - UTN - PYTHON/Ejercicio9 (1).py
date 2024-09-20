#Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII. 
#Muéstralos en línea recta, separados por un espacio entre cada carácter.
def caracter_a_ASCII(cadena):
    for caracter in cadena:
        print (ord(caracter)) #La funcion predeterminada ord retorna el valor en codigo ASCII de su caracter correspondiente

cad="La lluvia en Mendoza es escasa"
caracter_a_ASCII(cad)