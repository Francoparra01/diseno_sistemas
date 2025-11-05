from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class SmsObserver(Observer):
    """Observador que simula el envío de mensajes SMS."""

    def actualizar(self, evento: str, data: dict):
        print(f"[SMS] Enviando SMS por evento '{evento}' con datos: {data}")
