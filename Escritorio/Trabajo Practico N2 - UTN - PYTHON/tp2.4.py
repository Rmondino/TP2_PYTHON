def calcular_billete(numero):
    billete_200 = int(numero/200)
    numero=numero-(billete_200*200)
    
    billete_100 = int(numero/100)
    numero=numero-(billete_100*100)
    
    billete_50 = int(numero/50)
    numero=numero-(billete_50*50)
    
    billete_20 = int(numero/20)
    numero=numero-(billete_20*20)
    
    billete_10 = int(numero/10)
    numero=numero-(billete_10*10)
    
    billete_5 = int(numero/5)
    numero=numero-(billete_5*5)
    
    billete_2 = int(numero/2)
    numero=numero-(billete_2*2)
    
    billete_1 = int(numero/1)
    numero=numero-(billete_1*1)
    
    moneda_50 = int(numero/0.50)
    numero=numero-(moneda_50*0.50)
    
    moneda_25 = int(numero/0.25)
    numero=numero-(moneda_25*0.25)
    
    moneda_10 = int(numero/0.10)
    numero=numero-(moneda_10*0.10)
    
    moneda_05 = int(numero/0.05)
    numero=numero-(moneda_05*0.05)
    
    lista = [
        f"BILLETE DE 200 = {billete_200}",
        f"Billete DE 100 = {billete_100}",
        f"BILLETE DE 50 = {billete_50}",
        f"BILLETE DE 10 = {billete_10}",
        f"BILLETE DE 5 = {billete_5}",
        f"BILLETE DE 2 = {billete_2}",
        f"BILLETE DE 1 = {billete_1}",
        f"Monedas de 50 = {moneda_50}",
        f"Monedas de 25 = {moneda_25}",
        f"Monedas de 10 = {moneda_10}",
        f"monedas de 0.05 = {moneda_05}"
    ]
    
    # Crear una lista con los valores correspondientes
    valores = [billete_200, billete_100, billete_50, billete_10, billete_5, billete_2, billete_1, moneda_50, moneda_25, moneda_10, moneda_05]

    listanueva = []

    # Iterar por los valores y la lista de descripción
    for i in range(11):
        if valores[i] != 0:  # Verifica si el valor es distinto de 0
            listanueva.append(lista[i])  # Agregar la cadena asociada a listanueva

    return listanueva

# Función principal para solicitar el número y mostrar la suma de los dígitos
def main():
    # Solicitar un número de 3 dígitos
    
    numero = float(input("Ingresa un monto a calcular:"))
    
        
          
    
    # Llamar a la función para obtener la suma de los dígitos
    resultado = calcular_billete(numero)
    
    # Mostrar el resultado
    print(f"los billetes que debe usar para {numero} son: {resultado}")

# Llamada a la función principal
if __name__ == "__main__":
    main()
