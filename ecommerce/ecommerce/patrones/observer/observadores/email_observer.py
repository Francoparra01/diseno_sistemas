from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class EmailObserver(Observer):
    """Observador que simula el envío de correos electrónicos."""

    def actualizar(self, evento: str, data: dict):
        print(f"[EMAIL] Enviando correo por evento '{evento}' con datos: {data}")
