"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/__init__.py
# ================================================================================

"""Entidades relacionadas con los usuarios y sus membresías."""


# ================================================================================
# ARCHIVO 2/7: membresia.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy


class Membresia(ABC):
    """Clase abstracta base para las membresías de usuario."""

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    @abstractmethod
    def get_descuento(self) -> float:
        pass

    @abstractmethod
    def get_costo_envio(self) -> float:
        pass

    @abstractmethod
    def get_descuento_strategy(self) -> DescuentoStrategy:
        pass

    @abstractmethod
    def get_envio_strategy(self) -> EnvioStrategy:
        pass

    def to_dict(self) -> dict:
        return {
            "tipo": self.get_tipo(),
            "descuento": self.get_descuento(),
            "costo_envio": self.get_costo_envio(),
        }


# ================================================================================
# ARCHIVO 3/7: membresia_basic.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_basic.py
# ================================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_BASIC, ENVIO_BASIC
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_basic_strategy import DescuentoBasicStrategy
from ecommerce.patrones.strategy.impl.envio_basic_strategy import EnvioBasicStrategy


class MembresiaBasic(Membresia):
    """Membresía básica sin descuento y con costo de envío estándar."""

    def get_tipo(self) -> str:
        return "BASIC"

    def get_descuento(self) -> float:
        return DESCUENTO_BASIC

    def get_costo_envio(self) -> float:
        return ENVIO_BASIC

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoBasicStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioBasicStrategy()

    def __str__(self) -> str:
        return f"MembresiaBasic(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaBasic:
        return cls()


# ================================================================================
# ARCHIVO 4/7: membresia_premium.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_premium.py
# ================================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PREMIUM, ENVIO_PREMIUM
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_premium_strategy import DescuentoPremiumStrategy
from ecommerce.patrones.strategy.impl.envio_premium_strategy import EnvioPremiumStrategy


class MembresiaPremium(Membresia):
    """Membresía Premium con descuento y costo de envío reducido."""

    def get_tipo(self) -> str:
        return "PREMIUM"

    def get_descuento(self) -> float:
        return DESCUENTO_PREMIUM

    def get_costo_envio(self) -> float:
        return ENVIO_PREMIUM

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPremiumStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPremiumStrategy()

    def __str__(self) -> str:
        return f"MembresiaPremium(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPremium:
        return cls()


# ================================================================================
# ARCHIVO 5/7: membresia_prime.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_prime.py
# ================================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PRIME, ENVIO_PRIME
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_prime_strategy import DescuentoPrimeStrategy
from ecommerce.patrones.strategy.impl.envio_prime_strategy import EnvioPrimeStrategy


class MembresiaPrime(Membresia):
    """Membresía Prime con descuento y envío gratuito."""

    def get_tipo(self) -> str:
        return "PRIME"

    def get_descuento(self) -> float:
        return DESCUENTO_PRIME

    def get_costo_envio(self) -> float:
        return ENVIO_PRIME

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPrimeStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPrimeStrategy()

    def __str__(self) -> str:
        return f"MembresiaPrime(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPrime:
        return cls()


# ================================================================================
# ARCHIVO 6/7: perfil.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/perfil.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/7: usuario.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/usuario.py
# ================================================================================

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


