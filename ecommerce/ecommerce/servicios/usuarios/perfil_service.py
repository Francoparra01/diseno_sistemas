from __future__ import annotations
from typing import Dict

from ecommerce.entidades.usuarios.perfil import Perfil

class PerfilService:
    """Servicio para la gestión de perfiles de usuario."""

    def __init__(self):
        self._perfiles: Dict[str, Perfil] = {}

    def crear_perfil(self, usuario_id: str, direccion: str, telefono: str) -> Perfil:
        perfil = Perfil(usuario_id, direccion, telefono)
        self._perfiles[usuario_id] = perfil
        return perfil

    def obtener_perfil(self, usuario_id: str) -> Perfil | None:
        return self._perfiles.get(usuario_id)

    def actualizar_perfil(self, usuario_id: str, direccion: str | None = None, telefono: str | None = None) -> Perfil:
        perfil = self.obtener_perfil(usuario_id)
        if not perfil:
            raise ValueError(f"Perfil para usuario {usuario_id} no encontrado.")
        if direccion:
            perfil.set_direccion(direccion)
        if telefono:
            perfil.set_telefono(telefono)
        return perfil

    def to_dict(self) -> dict:
        return {
            "perfiles": {uid: perfil.to_dict() for uid, perfil in self._perfiles.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> PerfilService:
        perfil_service = cls()
        perfil_service._perfiles = {uid: Perfil.from_dict(perfil_data) for uid, perfil_data in data["perfiles"].items()}
        return perfil_service
