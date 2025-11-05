from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoOrden(ABC):
    """Interfaz base para los estados de una orden."""

    @abstractmethod
    def get_nombre_estado(self) -> str:
        pass

    @abstractmethod
    def procesar(self, orden: Orden):
        pass

    @abstractmethod
    def enviar(self, orden: Orden):
        pass

    @abstractmethod
    def entregar(self, orden: Orden):
        pass

    @abstractmethod
    def cancelar(self, orden: Orden):
        pass
