from src.drivers.calculator_manager import calculator_manager
class TestCalculatorTwoController:
    list_numbers = [2, 4]
    
    def test_standard_deviation(self):
        result = [(number * 11) ** 0.95 for number in self.list_numbers]
        assert float("{:.2f}".format(calculator_manager.standard_deviation(result))) == 8.78


