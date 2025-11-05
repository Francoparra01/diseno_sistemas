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
