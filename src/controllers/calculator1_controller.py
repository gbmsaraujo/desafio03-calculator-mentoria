from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository
from src.controllers.interface.Icalculator import ICalculator
from src.types.http_types.http_request import HttpRequest
from src.types.http_types.http_response import HttpResponse


class CalculatorOne(ICalculator):
    def __init__(self) -> None:
        self.values_in_list = []

    def operation(self, req:HttpRequest) -> HttpResponse:
        try:
            number = float(req.body['number'])
            divided_by_3 = self.__divide_by_3(number)
            first_part = self.__first_part_operation(divided_by_3)
            second_part = self.__second_part_operation(divided_by_3)
            self.__format_to_list_values(divided_by_3, first_part, second_part)
            calculator_repository.set_calculator_choice("Calculadora 1")
            calculator_repository.set_entries(number)

            result = calculator_manager.average(self.values_in_list)
            calculator_repository.set_status("Sucesso")
            calculator_repository.set_result(result)
            return HttpResponse(200, calculator_repository.get_response())
        except ValueError as err:
            calculator_repository.set_status("Falha")
            calculator_repository.set_result("Impossível Realizar a Média")
            return  HttpResponse(404, calculator_repository.get_response())

    def __divide_by_3(self,number):
        result = number / 3
        return result

    def __first_part_operation(self, number):
        result = (number / 4) + 7
        square_operation = calculator_manager.square(result) * 0.257
        return square_operation

    def __second_part_operation(self, number):
        result = ((number**2.121) / 5) + 1
        return result

    def __format_to_list_values(self, *args):
        numbers = list(args)
        self.values_in_list.extend(numbers)
