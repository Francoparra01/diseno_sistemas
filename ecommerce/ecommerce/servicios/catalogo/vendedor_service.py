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
