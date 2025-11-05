from __future__ import annotations
from typing import Dict, Type

from ecommerce.entidades.catalogo.categoria import Categoria
from ecommerce.entidades.catalogo.producto import Producto
from ecommerce.entidades.catalogo.vendedor import Vendedor

class CatalogoServiceRegistry:
    """Registro Singleton para los servicios del catálogo."""

    _instance: CatalogoServiceRegistry | None = None
    _categorias: Dict[str, Categoria] = {}
    _productos: Dict[str, Producto] = {}
    _vendedores: Dict[str, Vendedor] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def registrar_categoria(self, categoria: Categoria):
        self._categorias[categoria.get_id()] = categoria
        return categoria

    def obtener_categoria(self, categoria_id: str) -> Categoria | None:
        return self._categorias.get(categoria_id)

    def listar_categorias(self) -> List[Categoria]:
        return list(self._categorias.values())

    def registrar_producto(self, producto: Producto):
        self._productos[producto.get_id()] = producto
        return producto

    def obtener_producto(self, producto_id: str) -> Producto | None:
        return self._productos.get(producto_id)

    def listar_productos(self) -> List[Producto]:
        return list(self._productos.values())

    def registrar_vendedor(self, vendedor: Vendedor):
        self._vendedores[vendedor.get_id()] = vendedor
        return vendedor

    def obtener_vendedor(self, vendedor_id: str) -> Vendedor | None:
        return self._vendedores.get(vendedor_id)

    def listar_vendedores(self) -> List[Vendedor]:
        return list(self._vendedores.values())

    def to_dict(self) -> dict:
        return {
            "categorias": {cid: cat.to_dict() for cid, cat in self._categorias.items()},
            "productos": {pid: prod.to_dict() for pid, prod in self._productos.items()},
            "vendedores": {vid: vend.to_dict() for vid, vend in self._vendedores.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> CatalogoServiceRegistry:
        registry = cls()
        registry._categorias = {cid: Categoria.from_dict(cat_data) for cid, cat_data in data["categorias"].items()}
        registry._productos = {pid: Producto.from_dict(prod_data) for pid, prod_data in data["productos"].items()}
        registry._vendedores = {vid: Vendedor.from_dict(vend_data) for vid, vend_data in data["vendedores"].items()}
        return registry
