from __future__ import annotations
from abc import ABC, abstractmethod

from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy


class Membresia(ABC):
    """Clase abstracta base para las membresías de usuario."""

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    @abstractmethod
    def get_descuento(self) -> float:
        pass

    @abstractmethod
    def get_costo_envio(self) -> float:
        pass

    @abstractmethod
    def get_descuento_strategy(self) -> DescuentoStrategy:
        pass

    @abstractmethod
    def get_envio_strategy(self) -> EnvioStrategy:
        pass

    def to_dict(self) -> dict:
        return {
            "tipo": self.get_tipo(),
            "descuento": self.get_descuento(),
            "costo_envio": self.get_costo_envio(),
        }
