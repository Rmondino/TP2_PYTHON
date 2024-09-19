# Función para obtener la suma de los dígitos
def suma_digitos(numero):
    # Obtener el dígito de las unidades
    unidades = numero % 10
    
    # Obtener el dígito de las decenas
    decenas = (numero // 10) % 10
    
    # Obtener el dígito de las centenas
    centenas = numero // 100
    
    # Sumar los dígitos
    suma = unidades + decenas + centenas
    return suma

# Función principal para solicitar el número y mostrar la suma de los dígitos
def main():
    # Solicitar un número de 3 dígitos
    while True:
        try:
            numero = int(input("Ingresa un número de 3 dígitos (entre 100 y 999): "))
            if 100 <= numero <= 999:
                break
            else:
                print("Por favor, ingresa un número válido entre 100 y 999.")
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")
    
    # Llamar a la función para obtener la suma de los dígitos
    resultado = suma_digitos(numero)
    
    # Mostrar el resultado
    print(f"La suma de los dígitos del número {numero} es: {resultado}")

# Llamada a la función principal
if __name__ == "__main__":
    main()
