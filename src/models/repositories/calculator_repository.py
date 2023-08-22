class __CalculatorRepository:
    def __init__(self) -> None:
        self.calculator: str = None
        self.entries: list | float = None
        self.status: str = None
        self.result: float | str = None

    def set_calculator_choice(self, option: str) -> None:
        self.calculator = option

    def set_entries(self, entries: list | float) -> None:
        self.entries = entries

    def set_status(self, status: str) -> None:
        self.status = status

    def set_result(self, result: float | str) -> None:
        self.result = result

    def get_response(self):
        return {
            "calculator": self.calculator,
            "entries": self.entries,
            "status": self.status,
            "result": self.result,
        }

calculator_repository = __CalculatorRepository()