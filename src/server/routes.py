from src.controllers.calculator1_controller import CalculatorOne
from src.adapter.request_adapter import resquest_adapter
from src.controllers.calculator2_controller import CalculatorTwo
from src.controllers.calculator3_controller import CalculatorThree
from .server import app
from flask import request


@app.route("/calculator1", methods=["POST"])
def calculator_one():
    calculator_1 = resquest_adapter(request, CalculatorOne())

    return calculator_1.body, calculator_1.status_code


@app.route("/calculator2", methods=["POST"])
def calculator_two():
    calculator_2 = resquest_adapter(request, CalculatorTwo())

    return calculator_2.body, calculator_2.status_code


@app.route("/calculator3", methods=["POST"])
def calculator_three():
    calculator_3 = resquest_adapter(request, CalculatorThree())

    return calculator_3.body, calculator_3.status_code
