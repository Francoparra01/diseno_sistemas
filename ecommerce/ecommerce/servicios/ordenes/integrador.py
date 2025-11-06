"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/ordenes
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/ordenes/__init__.py
# ================================================================================

"""Servicios relacionados con la gestión de órdenes de compra."""


# ================================================================================
# ARCHIVO 2/2: orden_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/ordenes/orden_service.py
# ================================================================================

from __future__ import annotations
from typing import List, Dict

from ecommerce.entidades.ordenes.orden import Orden
from ecommerce.entidades.ordenes.item_orden import ItemOrden
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.patrones.state.estado_entregado import EstadoEntregado
from ecommerce.patrones.state.estado_enviado import EstadoEnviado
from ecommerce.patrones.state.estado_pendiente import EstadoPendiente
from ecommerce.patrones.state.estado_procesando import EstadoProcesando

class OrdenService:
    """Servicio para la gestión del ciclo de vida de las órdenes."""

    def __init__(self):
        self._ordenes: Dict[str, Orden] = {}

    def crear_orden(self, usuario_id: str, items: List[ItemOrden], total: float, direccion_envio: str) -> Orden:
        orden = Orden(usuario_id, items, total, direccion_envio)
        self._ordenes[orden.get_id()] = orden
        return orden

    def obtener_orden(self, orden_id: str) -> Orden | None:
        return self._ordenes.get(orden_id)

    def listar_ordenes(self) -> List[Orden]:
        return list(self._ordenes.values())

    def _reconstruir_estado(self, estado_nombre: str) -> EstadoOrden:
        if estado_nombre == "PENDIENTE":
            return EstadoPendiente()
        elif estado_nombre == "PROCESANDO":
            return EstadoProcesando()
        elif estado_nombre == "ENVIADO":
            return EstadoEnviado()
        elif estado_nombre == "ENTREGADO":
            return EstadoEntregado()
        elif estado_nombre == "CANCELADO":
            return EstadoCancelado()
        else:
            raise ValueError(f"Estado de orden desconocido: {estado_nombre}")

    def to_dict(self) -> dict:
        return {
            "ordenes": {oid: orden.to_dict() for oid, orden in self._ordenes.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> OrdenService:
        orden_service = cls()
        for oid, orden_data in data["ordenes"].items():
            orden = Orden.from_dict(orden_data)
            orden._estado = orden_service._reconstruir_estado(orden_data["estado"])
            orden_service._ordenes[oid] = orden
        return orden_service


