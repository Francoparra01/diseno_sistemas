from __future__ import annotations
import uuid

from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.entidades.usuarios.membresia_basic import MembresiaBasic

class Usuario:
    """Representa un usuario del sistema E-commerce."""

    def __init__(self, nombre: str, email: str, password: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._email = email
        self._password = password  # En un sistema real, esto estaría hasheado
        self._membresia: Membresia = MembresiaBasic()

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

    def verificar_password(self, password: str) -> bool:
        # En un sistema real, se compararía el hash
        return self._password == password

    def set_password(self, password: str):
        self._password = password

    def get_membresia(self) -> Membresia:
        return self._membresia

    def set_membresia(self, membresia: Membresia):
        self._membresia = membresia

    def __str__(self) -> str:
        return f"Usuario(ID: {self._id}, Nombre: {self._nombre}, Email: {self._email}, Membresía: {self._membresia.get_tipo()})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "email": self._email,
            "password": self._password,
            "membresia": self._membresia.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> Usuario:
        from ecommerce.patrones.factory.membresia_factory import MembresiaFactory

        usuario = cls(data["nombre"], data["email"], data["password"])
        usuario._id = data["id"]
        usuario._membresia = MembresiaFactory.crear_membresia(data["membresia"]["tipo"])
        return usuario
