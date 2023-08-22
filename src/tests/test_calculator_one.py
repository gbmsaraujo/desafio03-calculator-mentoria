import math
from src.drivers.calculator_manager import calculator_manager

class TestCalculatorOne:
    entry = 21
    part_one = 7
    part_two = 7
    part_three = 7

    def test_divide_by_3(self):
        result = self.entry / 3
        assert result == 7

    def test_first_part_operation(self):
        result = (self.part_one / 4) + 7
        square_operation = math.sqrt(result) * 0.257
        assert float("{:.2f}".format(square_operation)) == 0.76

    def test_second_part_operation(self):
        result = ((self.part_two**2.121) / 5) + 1
        self.part_two = result
        assert float("{:.2f}".format(result)) == 13.40

    def calculate_media(self):
        value_list = [self.part_one, self.part_two, self.part_three]
        result = calculator_manager.average(value_list)
        assert float("{:.2f}".format(result)) == 7.05
