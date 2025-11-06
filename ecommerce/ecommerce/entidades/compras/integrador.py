"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/__init__.py
# ================================================================================

"""Entidades relacionadas con el proceso de compra."""


# ================================================================================
# ARCHIVO 2/4: carrito.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/carrito.py
# ================================================================================

from __future__ import annotations
import uuid
from typing import Dict
from ecommerce.entidades.compras.item_carrito import ItemCarrito

class Carrito:
    """Representa el carrito de compras de un usuario."""

    def __init__(self, usuario_id: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._items: Dict[str, ItemCarrito] = {}

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_items(self) -> Dict[str, ItemCarrito]:
        return self._items

    def agregar_item(self, item: ItemCarrito):
        self._items[item.get_producto_id()] = item

    def remover_item(self, producto_id: str):
        if producto_id in self._items:
            del self._items[producto_id]

    def actualizar_cantidad(self, producto_id: str, cantidad: int):
        if producto_id in self._items:
            self._items[producto_id].set_cantidad(cantidad)

    def vaciar(self):
        self._items.clear()

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self._items.values())

    def __str__(self) -> str:
        items_str = "\n    ".join(str(item) for item in self._items.values())
        return (
            f"Carrito(ID: {self._id}, Usuario ID: {self._usuario_id}, "
            f"Items: {len(self._items)})"
            + (f"\n    {items_str}" if items_str else "")
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "items": {pid: item.to_dict() for pid, item_data in self._items.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> Carrito:
        carrito = cls(data["usuario_id"])
        carrito._id = data["id"]
        carrito._items = {pid: ItemCarrito.from_dict(item_data) for pid, item_data in data["items"].items()}
        return carrito


# ================================================================================
# ARCHIVO 3/4: item_carrito.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/item_carrito.py
# ================================================================================

from __future__ import annotations

class ItemCarrito:
    """Representa un ítem dentro del carrito de compras."""

    def __init__(self, producto_id: str, cantidad: int, precio_unitario: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")

        self._producto_id = producto_id
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_cantidad(self) -> int:
        return self._cantidad

    def set_cantidad(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self._cantidad = cantidad

    def get_precio_unitario(self) -> float:
        return self._precio_unitario

    def set_precio_unitario(self, precio_unitario: float):
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self._precio_unitario = precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __str__(self) -> str:
        return f"ItemCarrito(Producto ID: {self._producto_id}, Cantidad: {self._cantidad}, Precio Unitario: {self._precio_unitario})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "producto_id": self._producto_id,
            "cantidad": self._cantidad,
            "precio_unitario": self._precio_unitario,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ItemCarrito:
        return cls(data["producto_id"], data["cantidad"], data["precio_unitario"])


# ================================================================================
# ARCHIVO 4/4: procesador_pago.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/procesador_pago.py
# ================================================================================

from __future__ import annotations
import uuid
from datetime import datetime

from ecommerce.excepciones.pago_rechazado_exception import PagoRechazadoException

class ProcesadorPago:
    """Simula un procesador de pagos externo."""

    def __init__(self):
        self._transacciones = {}

    def procesar_pago(self, monto: float, metodo_pago: str) -> str:
        """Simula el procesamiento de un pago.

        Args:
            monto: El monto a pagar.
            metodo_pago: El método de pago (ej. 'tarjeta', 'paypal').

        Returns:
            Un ID de transacción si el pago es exitoso.

        Raises:
            PagoRechazadoException: Si el pago es rechazado.
        """
        if monto <= 0:
            raise ValueError("El monto a pagar debe ser positivo.")

        # Simulación de lógica de rechazo
        if "rechazar" in metodo_pago.lower():
            raise PagoRechazadoException(f"Método de pago '{metodo_pago}' configurado para rechazo.")

        transaccion_id = str(uuid.uuid4())
        self._transacciones[transaccion_id] = {
            "monto": monto,
            "metodo_pago": metodo_pago,
            "fecha": datetime.now().isoformat(),
            "estado": "aprobado",
        }
        return transaccion_id

    def get_estado_transaccion(self, transaccion_id: str) -> dict | None:
        """Obtiene el estado de una transacción."""
        return self._transacciones.get(transaccion_id)

    def to_dict(self) -> dict:
        return {
            "transacciones": self._transacciones,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ProcesadorPago:
        procesador = cls()
        procesador._transacciones = data["transacciones"]
        return procesador


