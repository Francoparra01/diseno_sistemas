from __future__ import annotations
from abc import ABC, abstractmethod

class DescuentoStrategy(ABC):
    """Interfaz para estrategias de cálculo de descuento."""

    @abstractmethod
    def aplicar_descuento(self, total: float) -> float:
        pass
