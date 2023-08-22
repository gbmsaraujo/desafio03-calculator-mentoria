import numpy as np
import math


class __CalculatorManager:
    def __init__(self) -> None:
        self.__np = np
        self.__mt = math

    def square(self, number: float):
        return self.__mt.sqrt(number)

    def average(self, list_numbers: list):
        return self.__np.average(list_numbers)

    def standard_deviation(self, list_numbers: list):
        return self.__np.std(list_numbers)

    def variance(self, list_numbers: list):
        return self.__np.var(list_numbers)


calculator_manager = __CalculatorManager()
