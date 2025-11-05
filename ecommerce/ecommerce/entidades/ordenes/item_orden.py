from __future__ import annotations

class ItemOrden:
    """Representa un ítem dentro de una orden de compra."""

    def __init__(self, producto_id: str, nombre_producto: str, cantidad: int, precio_unitario: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if precio_unitario < 0:
            raise ValueError("El precio unitario no puede ser negativo.")

        self._producto_id = producto_id
        self._nombre_producto = nombre_producto
        self._cantidad = cantidad
        self._precio_unitario = precio_unitario

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_nombre_producto(self) -> str:
        return self._nombre_producto

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio_unitario(self) -> float:
        return self._precio_unitario

    def calcular_subtotal(self) -> float:
        return self._cantidad * self._precio_unitario

    def __str__(self) -> str:
        return f"ItemOrden(Producto ID: {self._producto_id}, Nombre: {self._nombre_producto}, Cantidad: {self._cantidad}, Precio Unitario: {self._precio_unitario})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "producto_id": self._producto_id,
            "nombre_producto": self._nombre_producto,
            "cantidad": self._cantidad,
            "precio_unitario": self._precio_unitario,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ItemOrden:
        return cls(data["producto_id"], data["nombre_producto"], data["cantidad"], data["precio_unitario"])
