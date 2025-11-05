from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class AnalyticsObserver(Observer):
    """Observador que simula el envío de datos a un sistema de analíticas."""

    def actualizar(self, evento: str, data: dict):
        print(f"[ANALYTICS] Evento '{evento}' recibido con datos: {data}")
