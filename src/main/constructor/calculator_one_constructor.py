from src.controllers.calculator_one.calculator_one_controller import CalculatorOne
from src.views.view_calculator_one import insert_a_number


def calculate_one_constructor():
    number = float(insert_a_number())
    calculate_one = CalculatorOne(number)
    return calculate_one.operation()
