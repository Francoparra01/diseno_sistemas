from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_BASIC

class DescuentoBasicStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía básica (0%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_BASIC)
