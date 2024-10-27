from operators.addition import Addition
from controllers.controllers import Controllers
from operators.multiplication import Multiplication

class Calculator:

    def sum(self, first_hex_value, second_hex_value):
        return Addition.sum_hex(first_hex_value, second_hex_value)

    def multiply(self, first_hex_value, second_hex_value):
        return Multiplication.multiply_hex(first_hex_value, second_hex_value)

    def __init__(self):
        first_hex_value = input("\nPrimeiro valor: ").upper()
        second_hex_value = input("Segundo valor: ").upper()

        Controllers.check_hex_values(first_hex_value, second_hex_value)

        print(f"\nResultado da Multiplicação: {first_hex_value} x {second_hex_value} = {self.multiply(first_hex_value, second_hex_value)}")
        print(f"Resultado da Soma: {first_hex_value} + {second_hex_value} = {self.sum(first_hex_value, second_hex_value)}\n")


if __name__ == "__main__":
    try:
        calculator = Calculator()
    
    except Exception as exception:
        print(exception)

