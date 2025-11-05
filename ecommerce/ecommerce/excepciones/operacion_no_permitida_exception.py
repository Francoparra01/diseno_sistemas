from .ecommerce_exception import EcommerceException

class OperacionNoPermitidaException(EcommerceException):
    """Operación inválida según las reglas del dominio (por ejemplo, transición de estado no permitida)."""

    def __init__(self, operacion: str):
        super().__init__(
            user_message="Operación no permitida.",
            technical_message=f"Operación no permitida: {operacion}",
        )
        self._operacion = operacion

    def get_operacion(self) -> str:
        return self._operacion
