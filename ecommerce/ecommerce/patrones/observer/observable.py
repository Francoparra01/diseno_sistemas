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
