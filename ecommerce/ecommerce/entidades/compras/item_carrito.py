from __future__ import annotations

class ItemCarrito:
    """Representa un ítem dentro del carrito de compras."""

    def __init__(self, producto_id: str, cantidad: int, precio_unitario: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")

        self._producto_id = producto_id
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_cantidad(self) -> int:
        return self._cantidad

    def set_cantidad(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self._cantidad = cantidad

    def get_precio_unitario(self) -> float:
        return self._precio_unitario

    def set_precio_unitario(self, precio_unitario: float):
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        self._precio_unitario = precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __str__(self) -> str:
        return f"ItemCarrito(Producto ID: {self._producto_id}, Cantidad: {self._cantidad}, Precio Unitario: {self._precio_unitario})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "producto_id": self._producto_id,
            "cantidad": self._cantidad,
            "precio_unitario": self._precio_unitario,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ItemCarrito:
        return cls(data["producto_id"], data["cantidad"], data["precio_unitario"])
