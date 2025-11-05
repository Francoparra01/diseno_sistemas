from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PRIME

class DescuentoPrimeStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Prime (5%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PRIME)
