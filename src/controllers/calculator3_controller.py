import json
from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository
from src.controllers.interface.Icalculator import ICalculator
from src.types.http_types.http_request import HttpRequest
from src.types.http_types.http_response import HttpResponse


class CalculatorThree(ICalculator):
    def __init__(self) -> None:
        pass

    def operation(self, req: HttpRequest) -> HttpResponse:
        values = json.loads(req.body["values"])

        deviation = self.__calcule_standard_deviation(values)
        variance = self.__calculate_variance(values)

        if not variance >= deviation:
            return HttpResponse(404, "Falha ao processar a informação, tente novamente")
        calculator_repository.set_calculator_choice("Calculadora 3")
        calculator_repository.set_entries(values)
        calculator_repository.set_result(
            "Tudo certo, variância maior que desvio padrão!"
        )
        calculator_repository.set_status("Sucesso")
        return HttpResponse(200, calculator_repository.get_response())

    def __calcule_standard_deviation(self, values):
        return calculator_manager.standard_deviation(values)

    def __calculate_variance(self, values):
        return calculator_manager.variance(values)
