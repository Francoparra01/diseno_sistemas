"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/__init__.py
# ================================================================================

"""Patrón Observer para notificaciones y eventos."""


# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observable.py
# ================================================================================

from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

from ecommerce.patrones.observer.observer import Observer

class Observable(ABC):
    """Sujeto observable que notifica a sus observadores."""

    def __init__(self):
        self._observers: List[Observer] = []

    def agregar_observador(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remover_observador(self, observer: Observer):
        self._observers.remove(observer)

    def notificar_observadores(self, evento: str, data: dict):
        for observer in self._observers:
            observer.actualizar(evento, data)


# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observer.py
# ================================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class Observer(ABC):
    """Interfaz para los observadores que reaccionan a eventos."""

    @abstractmethod
    def actualizar(self, evento: str, data: dict):
        pass


