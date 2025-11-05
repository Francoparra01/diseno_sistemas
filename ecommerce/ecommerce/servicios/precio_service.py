from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy

if TYPE_CHECKING:
    from ecommerce.entidades.usuarios.membresia import Membresia

class PrecioService:
    """Servicio para calcular precios finales aplicando descuentos y costos de envío."""

    def __init__(self, descuento_strategy: DescuentoStrategy, envio_strategy: EnvioStrategy):
        self._descuento_strategy = descuento_strategy
        self._envio_strategy = envio_strategy

    def calcular_precio_final(self, subtotal: float, distancia_envio: float) -> float:
        total_con_descuento = self._descuento_strategy.aplicar_descuento(subtotal)
        costo_envio = self._envio_strategy.calcular_costo_envio(distancia_envio)
        return total_con_descuento + costo_envio

    def to_dict(self) -> dict:
        # Las estrategias no son serializables directamente aquí, se reconstruyen
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> PrecioService:
        # Este método no se usará directamente para cargar, las estrategias se inyectan
        raise NotImplementedError("PrecioService se construye con estrategias, no se carga directamente.")
