from flask import request as FlaskRequest
from src.types.http_types.http_request import HttpRequest
from src.controllers.interface.Icalculator import ICalculator
from src.types.http_types.http_response import HttpResponse

def resquest_adapter(request:FlaskRequest, calculator: ICalculator) -> HttpResponse:
    
    req = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=dict(request.args),
        path_params=request.view_args,
        url=request.full_path,
        ipv4=request.remote_addr,
    )

    response = calculator.operation(req)

    return response