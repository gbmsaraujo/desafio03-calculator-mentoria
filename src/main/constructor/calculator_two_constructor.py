from src.views.view_insert_n_numbers import insert_n_numbers
from src.controllers.calculator_two.calculator_two_controller import (
    CalculatorTwo,
)


def calculator_two_constructor():
    numbers = insert_n_numbers()
    calculator_two = CalculatorTwo(numbers)
    return calculator_two.operations()
