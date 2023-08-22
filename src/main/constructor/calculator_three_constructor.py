from src.views.view_insert_n_numbers import insert_n_numbers
from src.controllers.calculator_three.calculator_three_controller import CalculatorThree


def calculator_three_constructor():
    numbers = insert_n_numbers()
    calculator_three = CalculatorThree(numbers)
    return calculator_three.operations()
