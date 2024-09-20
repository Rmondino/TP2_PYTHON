def suma_recursiva(n):
    if n == 1:
        return 1
    return n + suma_recursiva(n - 1)
validarNumero = True

numero = int(input("Ingrese un número entero mayor a cero: "))
while validarNumero :
    if numero > 0 :
        validarNumero=False
        resultado = suma_recursiva(numero)
    else :
        numero = int(input("Ingrese un número entero mayor a cero: "))
        
print(f"La suma es: {resultado}")
