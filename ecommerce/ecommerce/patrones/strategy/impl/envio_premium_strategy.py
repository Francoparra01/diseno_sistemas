from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PREMIUM

class EnvioPremiumStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Premium (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PREMIUM
