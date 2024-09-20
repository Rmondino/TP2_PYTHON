class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumarFracciones(self, f):
        nuevoNumerador = self.numerador * f.denominador + f.numerador * self.denominador
        nuevoDenominador = self.denominador * f.denominador
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def restarFracciones(self, f):
        nuevoNumerador = self.numerador * f.denominador - f.numerador * self.denominador
        nuevoDenominador = self.denominador * f.denominador
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def multiplicarFracciones(self, f):
        nuevoNumerador = self.numerador * f.numerador
        nuevoDenominador = self.denominador * f.denominador
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def dividirFracciones(self, f):
        nuevoNumerador = self.numerador * f.denominador
        nuevoDenominador = self.denominador * f.numerador
        return Fraccion(nuevoNumerador, nuevoDenominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

class OperacionesFracciones:
    def main():
        num1 = int(input("Ingrese el numerador de la primera fracción: "))
        den1 = int(input("Ingrese el denominador de la primera fracción: "))
        f1 = Fraccion(num1, den1)

        num2 = int(input("Ingrese el numerador de la segunda fracción: "))
        den2 = int(input("Ingrese el denominador de la segunda fracción: "))
        f2 = Fraccion(num2, den2)

        suma = f1.sumarFracciones(f2)
        resta = f1.restarFracciones(f2)
        multiplicacion = f1.multiplicarFracciones(f2)
        division = f1.dividirFracciones(f2)

        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")

if __name__ == "__main__":
    OperacionesFracciones.main()

