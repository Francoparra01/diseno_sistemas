from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PRIME

class EnvioPrimeStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Prime (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PRIME
