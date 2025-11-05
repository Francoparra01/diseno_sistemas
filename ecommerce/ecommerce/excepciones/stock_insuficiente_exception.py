from .ecommerce_exception import EcommerceException

class StockInsuficienteException(EcommerceException):
    """No hay stock suficiente para el producto solicitado."""

    def __init__(self, producto_id: str, solicitado: int, disponible: int):
        super().__init__(
            user_message="No hay stock suficiente para completar la operación.",
            technical_message=f"Stock insuficiente: producto_id={producto_id}, solicitado={solicitado}, disponible={disponible}",
        )
        self._producto_id = producto_id
        self._solicitado = solicitado
        self._disponible = disponible

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_solicitado(self) -> int:
        return self._solicitado

    def get_disponible(self) -> int:
        return self._disponible
