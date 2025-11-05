from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PREMIUM

class DescuentoPremiumStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Premium (12%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PREMIUM)
