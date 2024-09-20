from decimal import Decimal

valorDecimal = Decimal('1e308')  # Valor muy grande
print(f"Valor con Decimal: {valorDecimal}")

# Decimal maneja valores con más precisión y evita el desbordamiento de float
valorDecimal *= Decimal('10')
print(f"Valor después de la multiplicación: {valorDecimal}")
