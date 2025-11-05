from __future__ import annotations
import uuid

class Categoria:
    """Representa una categoría de productos en el e-commerce."""

    def __init__(self, nombre: str, descripcion: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion

    def __str__(self) -> str:
        return f"Categoría(ID: {self._id}, Nombre: {self._nombre})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "descripcion": self._descripcion,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Categoria:
        categoria = cls(data["nombre"], data["descripcion"])
        categoria._id = data["id"]
        return categoria
