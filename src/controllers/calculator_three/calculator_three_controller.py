from src.drivers.calculator_manager import calculator_manager
from src.models.repositories.calculator_repository import calculator_repository


class CalculatorThree:
    def __init__(self, list_numbers: list) -> None:
        self.entries = list_numbers
        self.deviation = 0
        self.variance = 0

    def operations(self):
        self.__calcule_standard_deviation()
        self.__calculate_variance()
        print(self.deviation, self.variance)
        if not self.variance >= self.deviation:
            return "Falha ao processar a informação, tente novamente"
        calculator_repository.set_calculator_choice("Calculadora 3")
        calculator_repository.set_entries(self.entries)
        calculator_repository.set_result(
            "Tudo certo, variância maior que desvio padrão!"
        )
        calculator_repository.set_status("Sucesso")
        return calculator_repository.get_response()

    def __calcule_standard_deviation(self):
        self.deviation = calculator_manager.standard_deviation(self.entries)

    def __calculate_variance(self):
        self.variance = calculator_manager.variance(self.entries)
