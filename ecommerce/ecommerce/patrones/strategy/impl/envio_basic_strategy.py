from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_BASIC

class EnvioBasicStrategy(EnvioStrategy):
    """Estrategia de envío para membresía básica (costo fijo)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        # La distancia podría influir, pero para Basic es un costo fijo simple
        return ENVIO_BASIC
