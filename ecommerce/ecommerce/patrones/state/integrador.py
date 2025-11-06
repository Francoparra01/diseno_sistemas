"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/__init__.py
# ================================================================================

"""Patrón State para el manejo del ciclo de vida de las órdenes."""


# ================================================================================
# ARCHIVO 2/7: estado_cancelado.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_cancelado.py
# ================================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_CANCELADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoCancelado(EstadoOrden):
    """Estado de una orden: Cancelada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_CANCELADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden cancelada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden cancelada.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden cancelada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está cancelada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ================================================================================
# ARCHIVO 3/7: estado_entregado.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_entregado.py
# ================================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENTREGADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEntregado(EstadoOrden):
    """Estado de una orden: Entregada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENTREGADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya entregada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden ya entregada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está entregada.")

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya entregada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ================================================================================
# ARCHIVO 4/7: estado_enviado.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_enviado.py
# ================================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_entregado import EstadoEntregado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENVIADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEnviado(EstadoOrden):
    """Estado de una orden: Enviada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENVIADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya enviada.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está enviada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido entregada.")
        orden.set_estado(EstadoEntregado())

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya enviada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ================================================================================
# ARCHIVO 5/7: estado_orden.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_orden.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoOrden(ABC):
    """Interfaz base para los estados de una orden."""

    @abstractmethod
    def get_nombre_estado(self) -> str:
        pass

    @abstractmethod
    def procesar(self, orden: Orden):
        pass

    @abstractmethod
    def enviar(self, orden: Orden):
        pass

    @abstractmethod
    def entregar(self, orden: Orden):
        pass

    @abstractmethod
    def cancelar(self, orden: Orden):
        pass


# ================================================================================
# ARCHIVO 6/7: estado_pendiente.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_pendiente.py
# ================================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_procesando import EstadoProcesando
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PENDIENTE

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoPendiente(EstadoOrden):
    """Estado inicial de una orden: Pendiente."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PENDIENTE

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} está siendo procesada.")
        orden.set_estado(EstadoProcesando())

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden pendiente.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden pendiente.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ================================================================================
# ARCHIVO 7/7: estado_procesando.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_procesando.py
# ================================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_enviado import EstadoEnviado
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PROCESANDO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoProcesando(EstadoOrden):
    """Estado de una orden: Procesando."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PROCESANDO

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está en procesamiento.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido enviada.")
        orden.set_estado(EstadoEnviado())

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden que aún no ha sido enviada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada durante el procesamiento.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


