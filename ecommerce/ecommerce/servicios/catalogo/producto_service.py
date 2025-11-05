from __future__ import annotations
from typing import List

from ecommerce.entidades.catalogo.producto import Producto
from ecommerce.servicios.catalogo.catalogo_service_registry import CatalogoServiceRegistry
from ecommerce.excepciones.stock_insuficiente_exception import StockInsuficienteException

class ProductoService:
    """Servicio para la gestión de productos."""

    def __init__(self):
        self._registry = CatalogoServiceRegistry()

    def crear_producto(self, nombre: str, descripcion: str, precio: float, stock: int, categoria_id: str, vendedor_id: str) -> Producto:
        producto = Producto(nombre, descripcion, precio, stock, categoria_id, vendedor_id)
        self._registry.registrar_producto(producto)
        return producto

    def obtener_producto(self, producto_id: str) -> Producto | None:
        return self._registry.obtener_producto(producto_id)

    def listar_productos(self) -> List[Producto]:
        return self._registry.listar_productos()

    def actualizar_stock(self, producto_id: str, cantidad: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
        producto.set_stock(producto.get_stock() + cantidad)

    def verificar_y_reducir_stock(self, producto_id: str, cantidad: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
        if producto.get_stock() < cantidad:
            raise StockInsuficienteException(producto_id, cantidad, producto.get_stock())
        producto.set_stock(producto.get_stock() - cantidad)

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> ProductoService:
        return cls()
