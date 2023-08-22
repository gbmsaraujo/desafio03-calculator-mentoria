import numpy as np


class __CalculatorManager:
    def __init__(self) -> None:
        self.__np = np

    def average(self, list_numbers: list):
        return self.__np.average(list_numbers)

    def standard_deviation(self, list_numbers: list):
        return self.__np.std(list_numbers)

    def variance(self, list_numbers: list):
        return self.__np.var(list_numbers)

calculator_manager = __CalculatorManager()