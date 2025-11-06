"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/factory
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/factory/__init__.py
# ================================================================================

"""Patrón Factory Method para la creación de objetos."""


# ================================================================================
# ARCHIVO 2/2: membresia_factory.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/factory/membresia_factory.py
# ================================================================================

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


