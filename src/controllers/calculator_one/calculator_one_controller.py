import math
from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository


class CalculatorOne:
    def __init__(self, entry: float) -> None:
        self.values_in_list = []
        self.entry = entry
        self.part_one = 0
        self.part_two = 0
        self.part_three = 0

    def operation(self):
        self.__divide_by_3()
        self.__first_part_operation()
        self.__second_part_operation()
        self.__format_to_list_values()
        calculator_repository.set_calculator_choice("Calculadora 1")
        calculator_repository.set_entries(self.entry)

        try:
            result = calculator_manager.average(self.values_in_list)
            calculator_repository.set_status("Sucesso")
            calculator_repository.set_result(result)
            return calculator_repository.get_response()
        except ValueError as err:
            calculator_repository.set_status("Falha")
            calculator_repository.set_result("Impossível Realizar a Média")
            return calculator_repository.get_response()

    def __divide_by_3(self):
        result = self.entry / 3
        self.part_one = self.part_two = self.part_three = result

    def __first_part_operation(self):
        result = (self.part_one / 4) + 7
        square_operation = math.sqrt(result) * 0.257
        self.part_one = square_operation

    def __second_part_operation(self):
        result = ((self.part_two**2.121) / 5) + 1
        self.part_two = result

    def __format_to_list_values(self):
        self.values_in_list.append(self.part_one)
        self.values_in_list.append(self.part_two)
        self.values_in_list.append(self.part_three)
