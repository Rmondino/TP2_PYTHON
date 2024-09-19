valor_decimal = float(input("ingresa un numero decimal: "))

valor_int = int (valor_decimal)
print(f"Valor convertido a int: {valor_int}")
try:
    if -32768 <= valor_decimal <= 32767:
        valorShort = int(valor_decimal)
        print(f"Valor convertido a short: {valorShort}")
    else:
        print("El valor está fuera del rango de short (-32768 a 32767)")
except ValueError:
    print("Error en la conversión a short")

# Conversión a float (aunque ya lo ingresamos como float, esto es para demostrar el proceso)
valorFloat = float(valor_decimal)
print(f"Valor convertido a float: {valorFloat}")