from src.views.view_choose_calculator import choose_calculator
from src.views.view_results import view_results
from src.main.constructor.calculator_one_constructor import calculate_one_constructor
from src.main.constructor.calculator_two_constructor import calculator_two_constructor
from src.main.constructor.calculator_three_constructor import (
    calculator_three_constructor,
)


def start_program():
    is_finished = False
    option = choose_calculator()

    while not is_finished:
        if option == "1":
            response = calculate_one_constructor()
            view_results(response)
        elif option == "2":
            response = calculator_two_constructor()
            view_results(response)
        elif option == "3":
            response = calculator_three_constructor()
            view_results(response)
        elif option == "4":
            is_finished = True
        else:
            print("Selecione uma opção correta!")
