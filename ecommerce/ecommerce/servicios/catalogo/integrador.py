"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/__init__.py
# ================================================================================

"""Servicios relacionados con la gestión del catálogo de productos."""


# ================================================================================
# ARCHIVO 2/4: catalogo_service_registry.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/catalogo_service_registry.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: producto_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/producto_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: vendedor_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/vendedor_service.py
# ================================================================================

from __future__ import annotations
from typing import List

from ecommerce.entidades.catalogo.vendedor import Vendedor
from ecommerce.servicios.catalogo.catalogo_service_registry import CatalogoServiceRegistry

class VendedorService:
    """Servicio para la gestión de vendedores."""

    def __init__(self):
        self._registry = CatalogoServiceRegistry()

    def crear_vendedor(self, nombre: str, email: str) -> Vendedor:
        vendedor = Vendedor(nombre, email)
        self._registry.registrar_vendedor(vendedor)
        return vendedor

    def obtener_vendedor(self, vendedor_id: str) -> Vendedor | None:
        return self._registry.obtener_vendedor(vendedor_id)

    def listar_vendedores(self) -> List[Vendedor]:
        return self._registry.listar_vendedores()

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> VendedorService:
        return cls()


