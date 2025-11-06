"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/__init__.py
# ================================================================================

"""Entidades relacionadas con las órdenes de compra."""


# ================================================================================
# ARCHIVO 2/3: item_orden.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/item_orden.py
# ================================================================================

from __future__ import annotations

class ItemOrden:
    """Representa un ítem dentro de una orden de compra."""

    def __init__(self, producto_id: str, nombre_producto: str, cantidad: int, precio_unitario: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")

        self._producto_id = producto_id
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_nombre_producto(self) -> str:
        return self._nombre_producto

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio_unitario(self) -> float:
        return self._precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __str__(self) -> str:
        return f"ItemOrden(Producto ID: {self._producto_id}, Nombre: {self._nombre_producto}, Cantidad: {self._cantidad}, Precio Unitario: {self._precio_unitario})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "producto_id": self._producto_id,
            "nombre_producto": self._nombre_producto,
            "cantidad": self._cantidad,
            "precio_unitario": self._precio_unitario,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ItemOrden:
        return cls(data["producto_id"], data["nombre_producto"], data["cantidad"], data["precio_unitario"])


# ================================================================================
# ARCHIVO 3/3: orden.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/orden.py
# ================================================================================

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


