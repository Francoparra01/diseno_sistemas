"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/__init__.py
# ================================================================================

"""Paquete de excepciones personalizadas del e-commerce."""
from .ecommerce_exception import EcommerceException
from .usuario_existente_exception import UsuarioExistenteException
from .stock_insuficiente_exception import StockInsuficienteException
from .carrito_vacio_exception import CarritoVacioException
from .pago_rechazado_exception import PagoRechazadoException
from .persistencia_exception import PersistenciaException
from .operacion_no_permitida_exception import OperacionNoPermitidaException


# ================================================================================
# ARCHIVO 2/8: carrito_vacio_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/carrito_vacio_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class CarritoVacioException(EcommerceException):
    """Se intenta confirmar una compra con carrito vacío."""

    def __init__(self):
        super().__init__(
            user_message="El carrito está vacío.",
            technical_message="Operación inválida: carrito vacío",
        )


# ================================================================================
# ARCHIVO 3/8: ecommerce_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/ecommerce_exception.py
# ================================================================================

from __future__ import annotations

class EcommerceException(Exception):
    """Excepción base del dominio E-commerce.

    Atributos:
        user_message: Mensaje claro para el usuario.
        technical_message: Detalle técnico para logs.
    """

    def __init__(self, user_message: str, technical_message: str | None = None, cause: Exception | None = None):
        super().__init__(technical_message or user_message)
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        if cause is not None:
            self.__cause__ = cause

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"{self._user_message} | {self._technical_message}"


# ================================================================================
# ARCHIVO 4/8: operacion_no_permitida_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/operacion_no_permitida_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class OperacionNoPermitidaException(EcommerceException):
    """Operación inválida según las reglas del dominio (por ejemplo, transición de estado no permitida)."""

    def __init__(self, operacion: str):
        super().__init__(
            user_message="Operación no permitida.",
            technical_message=f"Operación no permitida: {operacion}",
        )
        self._operacion = operacion

    def get_operacion(self) -> str:
        return self._operacion


# ================================================================================
# ARCHIVO 5/8: pago_rechazado_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/pago_rechazado_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class PagoRechazadoException(EcommerceException):
    """El procesador de pagos rechazó la transacción."""

    def __init__(self, motivo: str | None = None):
        detalle = f"Pago rechazado{': ' + motivo if motivo else ''}"
        super().__init__(
            user_message="El pago fue rechazado. Intente con otro método o más tarde.",
            technical_message=detalle,
        )
        self._motivo = motivo

    def get_motivo(self) -> str | None:
        return self._motivo


# ================================================================================
# ARCHIVO 6/8: persistencia_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/persistencia_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class PersistenciaException(EcommerceException):
    """Error leyendo o escribiendo datos en disco."""

    def __init__(self, path: str, operacion: str, cause: Exception | None = None):
        super().__init__(
            user_message="Ocurrió un error de almacenamiento.",
            technical_message=f"Persistencia fallida: {operacion} en '{path}'",
            cause=cause,
        )
        self._path = path
        self._operacion = operacion

    def get_path(self) -> str:
        return self._path

    def get_operacion(self) -> str:
        return self._operacion


# ================================================================================
# ARCHIVO 7/8: stock_insuficiente_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/stock_insuficiente_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class StockInsuficienteException(EcommerceException):
    """No hay stock suficiente para el producto solicitado."""

    def __init__(self, producto_id: str, solicitado: int, disponible: int):
        super().__init__(
            user_message="No hay stock suficiente para completar la operación.",
            technical_message=f"Stock insuficiente: producto_id={producto_id}, solicitado={solicitado}, disponible={disponible}",
        )
        self._producto_id = producto_id
        self._solicitado = solicitado
        self._disponible = disponible

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_solicitado(self) -> int:
        return self._solicitado

    def get_disponible(self) -> int:
        return self._disponible


# ================================================================================
# ARCHIVO 8/8: usuario_existente_exception.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/usuario_existente_exception.py
# ================================================================================

from .ecommerce_exception import EcommerceException

class UsuarioExistenteException(EcommerceException):
    """Se intenta registrar un usuario ya existente (p.ej., por email)."""

    def __init__(self, email: str):
        super().__init__(
            user_message=f"El usuario con email '{email}' ya existe.",
            technical_message=f"Usuario duplicado: email={email}",
        )
        self._email = email

    def get_email(self) -> str:
        return self._email


