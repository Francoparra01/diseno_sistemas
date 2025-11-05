from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_procesando import EstadoProcesando
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PENDIENTE

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoPendiente(EstadoOrden):
    """Estado inicial de una orden: Pendiente."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PENDIENTE

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} está siendo procesada.")
        orden.set_estado(EstadoProcesando())

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden pendiente.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden pendiente.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()
