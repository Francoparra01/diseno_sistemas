"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/__init__.py
# ================================================================================

"""Servicios relacionados con la gestión de usuarios y perfiles."""


# ================================================================================
# ARCHIVO 2/3: perfil_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/perfil_service.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: usuario_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/usuario_service.py
# ================================================================================

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


