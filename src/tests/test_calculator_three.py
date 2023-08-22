from src.drivers.calculator_manager import calculator_manager


class TestCalculatorThree:
    list_number = [20,80]
    variance = 77.13
    deviation = 8.78

    def test_variance_calc(self):
        assert float("{:.2f}".format(calculator_manager.variance(self.list_number))) == 900

    def test_deviation_calc(self):
        assert float("{:.2f}".format(calculator_manager.standard_deviation(self.list_number))) == 30.00

    def test_compare(self):
        assert self.variance > self.deviation
