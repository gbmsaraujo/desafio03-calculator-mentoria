from src.views.view_choose_calculator import choose_calculator
from src.main.constructor.calculator_one_constructor import calculate_one_constructor

def start_program():
    option = choose_calculator()

    if option == "1":
        calculate_one_constructor()