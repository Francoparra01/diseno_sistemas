from __future__ import annotations
import uuid
from datetime import datetime

from ecommerce.excepciones.pago_rechazado_exception import PagoRechazadoException

class ProcesadorPago:
    """Simula un procesador de pagos externo."""

    def __init__(self):
        self._transacciones = {}

    def procesar_pago(self, monto: float, metodo_pago: str) -> str:
        """Simula el procesamiento de un pago.

        Args:
            monto: El monto a pagar.
            metodo_pago: El método de pago (ej. 'tarjeta', 'paypal').

        Returns:
            Un ID de transacción si el pago es exitoso.

        Raises:
            PagoRechazadoException: Si el pago es rechazado.
        """
        if monto <= 0:
            raise ValueError("El monto a pagar debe ser positivo.")

        # Simulación de lógica de rechazo
        if "rechazar" in metodo_pago.lower():
            raise PagoRechazadoException(f"Método de pago '{metodo_pago}' configurado para rechazo.")

        transaccion_id = str(uuid.uuid4())
        self._transacciones[transaccion_id] = {
            "monto": monto,
            "metodo_pago": metodo_pago,
            "fecha": datetime.now().isoformat(),
            "estado": "aprobado",
        }
        return transaccion_id

    def get_estado_transaccion(self, transaccion_id: str) -> dict | None:
        """Obtiene el estado de una transacción."""
        return self._transacciones.get(transaccion_id)

    def to_dict(self) -> dict:
        return {
            "transacciones": self._transacciones,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ProcesadorPago:
        procesador = cls()
        procesador._transacciones = data["transacciones"]
        return procesador
