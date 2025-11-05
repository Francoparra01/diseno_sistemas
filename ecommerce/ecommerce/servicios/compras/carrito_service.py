from __future__ import annotations
from typing import Dict

from ecommerce.entidades.compras.carrito import Carrito
from ecommerce.entidades.compras.item_carrito import ItemCarrito
from ecommerce.servicios.catalogo.producto_service import ProductoService

class CarritoService:
    """Servicio para la gestión de carritos de compra."""

    def __init__(self, producto_service: ProductoService):
        self._carritos: Dict[str, Carrito] = {}
        self._producto_service = producto_service

    def crear_carrito(self, usuario_id: str) -> Carrito:
        if usuario_id in self._carritos:
            return self._carritos[usuario_id]
        carrito = Carrito(usuario_id)
        self._carritos[usuario_id] = carrito
        return carrito

    def obtener_carrito(self, usuario_id: str) -> Carrito | None:
        return self._carritos.get(usuario_id)

    def agregar_item_a_carrito(self, usuario_id: str, producto_id: str, cantidad: int):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")

        producto = self._producto_service.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        item = ItemCarrito(producto_id, cantidad, producto.get_precio())
        carrito.agregar_item(item)

    def remover_item_de_carrito(self, usuario_id: str, producto_id: str):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.remover_item(producto_id)

    def actualizar_cantidad_item_carrito(self, usuario_id: str, producto_id: str, cantidad: int):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.actualizar_cantidad(producto_id, cantidad)

    def vaciar_carrito(self, usuario_id: str):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.vaciar()

    def to_dict(self) -> dict:
        return {
            "carritos": {uid: carrito.to_dict() for uid, carrito in self._carritos.items()},
        }

    @classmethod
    def from_dict(cls, data: dict, producto_service: ProductoService) -> CarritoService:
        carrito_service = cls(producto_service)
        carrito_service._carritos = {uid: Carrito.from_dict(carrito_data) for uid, carrito_data in data["carritos"].items()}
        return carrito_service
