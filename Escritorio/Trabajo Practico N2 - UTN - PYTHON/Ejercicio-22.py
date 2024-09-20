def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n + suma_digitos(n -1)

numero = int(input("Ingrese un número: "))
sumaTotal = suma_digitos(numero)
print(f"La suma de los dígitos es: {sumaTotal}")

