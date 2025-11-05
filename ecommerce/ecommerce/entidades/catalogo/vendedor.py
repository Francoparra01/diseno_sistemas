from __future__ import annotations
import uuid

class Vendedor:
    """Representa un vendedor en el e-commerce."""

    def __init__(self, nombre: str, email: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._email = email

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def __str__(self) -> str:
        return f"Vendedor(ID: {self._id}, Nombre: {self._nombre}, Email: {self._email})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "email": self._email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Vendedor:
        vendedor = cls(data["nombre"], data["email"])
        vendedor._id = data["id"]
        return vendedor
