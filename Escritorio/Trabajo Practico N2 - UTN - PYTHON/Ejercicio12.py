#Dada la cadena “hipopotamo”, extraer la cuarta y quinta letra.
palabra = "hipopotamo"

for i,letra in enumerate(palabra):
    if i == 3 or i == 4:
        print(f"Letra {i+1}:{letra}")
