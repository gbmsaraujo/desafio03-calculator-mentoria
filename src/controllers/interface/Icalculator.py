from abc import ABC, abstractmethod
from src.types.http_types.http_request import HttpRequest
from src.types.http_types.http_response import HttpResponse


class ICalculator(ABC):
    @abstractmethod
    def operation(self, req: HttpRequest) -> HttpResponse:
        pass
