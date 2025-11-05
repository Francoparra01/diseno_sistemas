from .ecommerce_exception import EcommerceException

class PagoRechazadoException(EcommerceException):
    """El procesador de pagos rechazó la transacción."""

    def __init__(self, motivo: str | None = None):
        detalle = f"Pago rechazado{': ' + motivo if motivo else ''}"
        super().__init__(
            user_message="El pago fue rechazado. Intente con otro método o más tarde.",
            technical_message=detalle,
        )
        self._motivo = motivo

    def get_motivo(self) -> str | None:
        return self._motivo
