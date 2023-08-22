from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository


class CalculatorTwo:
    def __init__(self, list_numbers: list) -> None:
        self.entries = list_numbers
        self.result = 0

    def operations(self):
        return self.__calcule_standard_deviation()

    def __calcule_standard_deviation(self):
        result = [((number) * 11) ** 0.95 for number in self.entries]
        try:
            calculator_repository.set_calculator_choice("Calculadora 2")
            calculator_repository.set_entries(self.entries)
            calculator_repository.set_status("Sucesso")
            deviation = calculator_manager.standard_deviation(result)
            self.result = 1 / deviation
            calculator_repository.set_result(self.result)
            return calculator_repository.get_response()
        except:
            calculator_repository.set_status("Falha")
            calculator_repository.set_result("Erro ao calcular o desvio padrão")
            return calculator_repository.get_response()
