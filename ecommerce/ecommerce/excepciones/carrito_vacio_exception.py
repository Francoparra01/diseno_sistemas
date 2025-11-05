from .ecommerce_exception import EcommerceException

class CarritoVacioException(EcommerceException):
    """Se intenta confirmar una compra con carrito vacío."""

    def __init__(self):
        super().__init__(
            user_message="El carrito está vacío.",
            technical_message="Operación inválida: carrito vacío",
        )
