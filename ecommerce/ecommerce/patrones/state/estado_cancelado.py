from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_CANCELADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoCancelado(EstadoOrden):
    """Estado de una orden: Cancelada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_CANCELADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden cancelada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden cancelada.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden cancelada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está cancelada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()
