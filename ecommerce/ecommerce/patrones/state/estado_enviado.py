from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_entregado import EstadoEntregado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENVIADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEnviado(EstadoOrden):
    """Estado de una orden: Enviada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENVIADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya enviada.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está enviada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido entregada.")
        orden.set_estado(EstadoEntregado())

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya enviada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()
