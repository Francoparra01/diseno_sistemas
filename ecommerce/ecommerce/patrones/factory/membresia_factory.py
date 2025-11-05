from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.entidades.usuarios.membresia_basic import MembresiaBasic
from ecommerce.entidades.usuarios.membresia_prime import MembresiaPrime
from ecommerce.entidades.usuarios.membresia_premium import MembresiaPremium

class MembresiaFactory:
    """Factory Method para crear instancias de Membresia."""

    @staticmethod
    def crear_membresia(tipo: str) -> Membresia:
        if tipo == "BASIC":
            return MembresiaBasic()
        elif tipo == "PRIME":
            return MembresiaPrime()
        elif tipo == "PREMIUM":
            return MembresiaPremium()
        else:
            raise ValueError(f"Tipo de membresía desconocido: {tipo}")
