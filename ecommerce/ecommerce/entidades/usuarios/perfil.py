from __future__ import annotations
import uuid

class Perfil:
    """Representa el perfil de un usuario con información adicional."""

    def __init__(self, usuario_id: str, direccion: str, telefono: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._direccion = direccion
        self._telefono = telefono

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_direccion(self) -> str:
        return self._direccion

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def get_telefono(self) -> str:
        return self._telefono

    def set_telefono(self, telefono: str):
        self._telefono = telefono

    def __str__(self) -> str:
        return f"Perfil(ID: {self._id}, Usuario ID: {self._usuario_id}, Dirección: {self._direccion})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "direccion": self._direccion,
            "telefono": self._telefono,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Perfil:
        perfil = cls(data["usuario_id"], data["direccion"], data["telefono"])
        perfil._id = data["id"]
        return perfil
