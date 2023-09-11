from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository
from src.controllers.interface.Icalculator import ICalculator
from src.types.http_types.http_request import HttpRequest
from src.types.http_types.http_response import HttpResponse
import json


class CalculatorTwo(ICalculator):
    def __init__(self) -> None:
        self.result = 0

    def operation(self, req: HttpRequest) -> HttpResponse:
        values = json.loads(req.body["values"])

        return self.__calcule_standard_deviation(values)

    def __calcule_standard_deviation(self, values: list) -> HttpResponse:
        result = [((number) * 11) ** 0.95 for number in values]
        try:
            calculator_repository.set_calculator_choice("Calculadora 2")
            calculator_repository.set_entries(values)
            calculator_repository.set_status("Sucesso")
            deviation = calculator_manager.standard_deviation(result)
            self.result = 1 / deviation
            calculator_repository.set_result(self.result)
            return HttpResponse(200, calculator_repository.get_response())
        except:
            calculator_repository.set_status("Falha")
            calculator_repository.set_result("Erro ao calcular o desvio padrão")
            return HttpResponse(400, calculator_repository.get_response())
