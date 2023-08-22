# class Result:
#     def __init__(self) -> None:
#         self.calculator = str
#         self.entries = list
#         self.status = str
#         self.result = str


def view_results(result: dict):
    print(
        f"""
          * {result['calculator']}
          * {result['entries']}
          * {result['status']}
          * {result['result']}

"""
    )
