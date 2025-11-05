from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_enviado import EstadoEnviado
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PROCESANDO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoProcesando(EstadoOrden):
    """Estado de una orden: Procesando."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PROCESANDO

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está en procesamiento.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido enviada.")
        orden.set_estado(EstadoEnviado())

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden que aún no ha sido enviada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada durante el procesamiento.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()
