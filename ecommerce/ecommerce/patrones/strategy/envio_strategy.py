from __future__ import annotations
from abc import ABC, abstractmethod

class EnvioStrategy(ABC):
    """Interfaz para estrategias de cálculo de costo de envío."""

    @abstractmethod
    def calcular_costo_envio(self, distancia: float) -> float:
        pass
