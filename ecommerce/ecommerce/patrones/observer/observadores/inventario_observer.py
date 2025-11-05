from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class InventarioObserver(Observer):
    """Observador que simula la actualización del inventario."""

    def actualizar(self, evento: str, data: dict):
        print(f"[INVENTARIO] Actualizando inventario por evento '{evento}' con datos: {data}")
