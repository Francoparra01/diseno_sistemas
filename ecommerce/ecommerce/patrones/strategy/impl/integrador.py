"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/__init__.py
# ================================================================================

"""Implementaciones concretas de las estrategias de descuento y envío."""


# ================================================================================
# ARCHIVO 2/7: descuento_basic_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_basic_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_BASIC

class DescuentoBasicStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía básica (0%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_BASIC)


# ================================================================================
# ARCHIVO 3/7: descuento_premium_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_premium_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PREMIUM

class DescuentoPremiumStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Premium (12%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PREMIUM)


# ================================================================================
# ARCHIVO 4/7: descuento_prime_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_prime_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PRIME

class DescuentoPrimeStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Prime (5%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PRIME)


# ================================================================================
# ARCHIVO 5/7: envio_basic_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_basic_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_BASIC

class EnvioBasicStrategy(EnvioStrategy):
    """Estrategia de envío para membresía básica (costo fijo)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        # La distancia podría influir, pero para Basic es un costo fijo simple
        return ENVIO_BASIC


# ================================================================================
# ARCHIVO 6/7: envio_premium_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_premium_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PREMIUM

class EnvioPremiumStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Premium (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PREMIUM


# ================================================================================
# ARCHIVO 7/7: envio_prime_strategy.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_prime_strategy.py
# ================================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PRIME

class EnvioPrimeStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Prime (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PRIME


