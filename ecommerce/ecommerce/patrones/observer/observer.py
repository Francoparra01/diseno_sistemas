from __future__ import annotations
from abc import ABC, abstractmethod

class Observer(ABC):
    """Interfaz para los observadores que reaccionan a eventos."""

    @abstractmethod
    def actualizar(self, evento: str, data: dict):
        pass
