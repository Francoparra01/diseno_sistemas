from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENTREGADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEntregado(EstadoOrden):
    """Estado de una orden: Entregada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENTREGADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya entregada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden ya entregada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está entregada.")

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya entregada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()
