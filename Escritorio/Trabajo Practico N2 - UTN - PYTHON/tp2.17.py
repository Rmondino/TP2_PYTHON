class FuncionesPrograma:
    
    @staticmethod
    def getFechaString(fecha):
        # Diccionarios para convertir números a palabras
        dias = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince",
            16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve", 20: "Veinte",
            21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco",
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta",
            31: "Treinta y uno"
        }
        
        meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
            6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre",
            11: "Noviembre", 12: "Diciembre"
        }
        
        # Función auxiliar para convertir el año a palabras
        def convertir_ano(ano):
            unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
            decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
            centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
            
            # Divide el año en cientos y unidades
            mil = ano // 1000
            resto = ano % 1000
            cientos = resto // 100
            resto %= 100
            decena = resto // 10
            unidad = resto % 10
            
            palabras = "mil "
            if cientos > 0:
                palabras += centenas[cientos] + " "
            if decena > 0:
                palabras += decenas[decena] + " "
            if unidad > 0:
                palabras += unidades[unidad]
                
            return palabras.strip()
        
        # Extraer día, mes y año
        dia, mes, ano = map(int, fecha.split('/'))
        
        # Convertir fecha a string
        dia_string = dias[dia]
        mes_string = meses[mes]
        ano_string = convertir_ano(ano)
        
        return f"{dia_string} de {mes_string} de {ano_string}"
        

# Ejemplo de uso:
fecha = "15/10/1900"
resultado = FuncionesPrograma.getFechaString(fecha)
print(resultado)
