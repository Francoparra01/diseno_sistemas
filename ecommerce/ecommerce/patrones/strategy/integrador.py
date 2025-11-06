"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/__init__.py
# ================================================================================

"""Patrón Strategy para aplicar diferentes lógicas de negocio."""


# ================================================================================
# ARCHIVO 2/3: descuento_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/descuento_strategy.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class DescuentoStrategy(ABC):
    """Interfaz para estrategias de cálculo de descuento."""

    @abstractmethod
    def aplicar_descuento(self, total: float) -> float:
        pass


# ================================================================================
# ARCHIVO 3/3: envio_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/envio_strategy.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class EnvioStrategy(ABC):
    """Interfaz para estrategias de cálculo de costo de envío."""

    @abstractmethod
    def calcular_costo_envio(self, distancia: float) -> float:
        pass


