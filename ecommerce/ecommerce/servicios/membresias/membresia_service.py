from __future__ import annotations
from typing import Dict

from ecommerce.entidades.usuarios.usuario import Usuario
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.patrones.factory.membresia_factory import MembresiaFactory

class MembresiaService:
    """Servicio para la gestión de membresías de usuarios."""

    def __init__(self):
        pass

    def asignar_membresia(self, usuario: Usuario, tipo_membresia: str) -> Membresia:
        membresia = MembresiaFactory.crear_membresia(tipo_membresia)
        usuario.set_membresia(membresia)
        return membresia

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaService:
        return cls()
