from __future__ import annotations
import uuid
from datetime import datetime
from typing import List

from ecommerce.entidades.ordenes.item_orden import ItemOrden
from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_pendiente import EstadoPendiente

class Orden:
    """Representa una orden de compra realizada por un usuario."""

    def __init__(self, usuario_id: str, items: List[ItemOrden], total: float, direccion_envio: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._fecha_creacion = datetime.now().isoformat()
        self._items = items
        self._total = total
        self._direccion_envio = direccion_envio
        self._estado: EstadoOrden = EstadoPendiente()
        self._transaccion_id: str | None = None

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_fecha_creacion(self) -> str:
        return self._fecha_creacion

    def get_items(self) -> List[ItemOrden]:
        return self._items

    def get_total(self) -> float:
        return self._total

    def get_direccion_envio(self) -> str:
        return self._direccion_envio

    def get_estado(self) -> EstadoOrden:
        return self._estado

    def set_estado(self, estado: EstadoOrden):
        self._estado = estado

    def get_transaccion_id(self) -> str | None:
        return self._transaccion_id

    def set_transaccion_id(self, transaccion_id: str):
        self._transaccion_id = transaccion_id

    # Métodos de transición de estado
    def procesar(self):
        self._estado.procesar(self)

    def enviar(self):
        self._estado.enviar(self)

    def entregar(self):
        self._estado.entregar(self)

    def cancelar(self):
        self._estado.cancelar(self)

    def __str__(self) -> str:
        return f"Orden(ID: {self._id}, Usuario ID: {self._usuario_id}, Total: {self._total}, Estado: {self._estado.get_nombre_estado()})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "fecha_creacion": self._fecha_creacion,
            "items": [item.to_dict() for item in self._items],
            "total": self._total,
            "direccion_envio": self._direccion_envio,
            "estado": self._estado.get_nombre_estado(), # Guardamos solo el nombre del estado
            "transaccion_id": self._transaccion_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Orden:
        # La reconstrucción del estado se hará en el servicio de órdenes
        # para evitar dependencias circulares y manejar la lógica de estados.
        orden = cls(
            data["usuario_id"],
            [ItemOrden.from_dict(item_data) for item_data in data["items"]],
            data["total"],
            data["direccion_envio"],
        )
        orden._id = data["id"]
        orden._fecha_creacion = data["fecha_creacion"]
        orden._transaccion_id = data["transaccion_id"]
        # El estado se establecerá externamente después de la creación de la orden
        return orden
