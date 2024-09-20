class OperacionMatematica:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 == 0:
            return "Error: División por cero"
        return self.valor1 / self.valor2

    def aplicarOperacion(self, operacion):
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"


class Calculo:
    @staticmethod
    def main():
        # Crear una instancia de la clase OperacionMatematica
        operacion = OperacionMatematica(10, 5)
        
        # Realizar las operaciones y mostrar los resultados
        print("Suma (10 + 5):", operacion.aplicarOperacion("+"))
        print("Resta (10 - 5):", operacion.aplicarOperacion("-"))
        print("Multiplicación (10 * 5):", operacion.aplicarOperacion("*"))
        print("División (10 / 5):", operacion.aplicarOperacion("/"))


# Ejecución del programa
if __name__ == "__main__":
    Calculo.main()
