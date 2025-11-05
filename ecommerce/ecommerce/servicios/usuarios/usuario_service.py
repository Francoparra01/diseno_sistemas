from __future__ import annotations
from typing import Dict, List

from ecommerce.entidades.usuarios.usuario import Usuario
from ecommerce.excepciones.usuario_existente_exception import UsuarioExistenteException

class UsuarioService:
    """Servicio para la gestión de usuarios."""

    def __init__(self):
        self._usuarios: Dict[str, Usuario] = {}
        self._usuarios_por_email: Dict[str, Usuario] = {}

    def registrar_usuario(self, nombre: str, email: str, password: str) -> Usuario:
        if email in self._usuarios_por_email:
            raise UsuarioExistenteException(email)
        usuario = Usuario(nombre, email, password)
        self._usuarios[usuario.get_id()] = usuario
        self._usuarios_por_email[email] = usuario
        return usuario

    def obtener_usuario_por_id(self, usuario_id: str) -> Usuario | None:
        return self._usuarios.get(usuario_id)

    def obtener_usuario_por_email(self, email: str) -> Usuario | None:
        return self._usuarios_por_email.get(email)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios.values())

    def to_dict(self) -> dict:
        return {
            "usuarios": {uid: user.to_dict() for uid, user in self._usuarios.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> UsuarioService:
        usuario_service = cls()
        for uid, user_data in data["usuarios"].items():
            user = Usuario.from_dict(user_data)
            usuario_service._usuarios[uid] = user
            usuario_service._usuarios_por_email[user.get_email()] = user
        return usuario_service
