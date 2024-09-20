def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
#n%10 toma el ultimo digito para sumarlo y n//10 borra el ultimo digito para la siguiente vuelta

numero = int(input("Ingrese un número: "))
sumaTotal = suma_digitos(numero)
print(f"La suma de los dígitos es: {sumaTotal}")
