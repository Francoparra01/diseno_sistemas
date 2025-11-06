"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/__init__.py
# ================================================================================

"""Entidades relacionadas con el catálogo de productos."""


# ================================================================================
# ARCHIVO 2/4: categoria.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/categoria.py
# ================================================================================

from __future__ import annotations
import uuid

class Categoria:
    """Representa una categoría de productos en el e-commerce."""

    def __init__(self, nombre: str, descripcion: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._descripcion = descripcion

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion

    def __str__(self) -> str:
        return f"Categoría(ID: {self._id}, Nombre: {self._nombre})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "descripcion": self._descripcion,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Categoria:
        categoria = cls(data["nombre"], data["descripcion"])
        categoria._id = data["id"]
        return categoria


# ================================================================================
# ARCHIVO 3/4: producto.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/producto.py
# ================================================================================

from __future__ import annotations
import uuid

class Producto:
    """Representa un producto disponible en el catálogo."""

    def __init__(self, nombre: str, descripcion: str, precio: float, stock: int, categoria_id: str, vendedor_id: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock
        self._categoria_id = categoria_id
        self._vendedor_id = vendedor_id

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_descripcion(self, descripcion: str):
        self._descripcion = descripcion

    def get_precio(self) -> float:
        return self._precio

    def set_precio(self, precio: float):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    def get_stock(self) -> int:
        return self._stock

    def set_stock(self, stock: int):
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = stock

    def get_categoria_id(self) -> str:
        return self._categoria_id

    def set_categoria_id(self, categoria_id: str):
        self._categoria_id = categoria_id

    def get_vendedor_id(self) -> str:
        return self._vendedor_id

    def set_vendedor_id(self, vendedor_id: str):
        self._vendedor_id = vendedor_id

    def __str__(self) -> str:
        return f"Producto(ID: {self._id}, Nombre: {self._nombre}, Precio: {self._precio}, Stock: {self._stock})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "descripcion": self._descripcion,
            "precio": self._precio,
            "stock": self._stock,
            "categoria_id": self._categoria_id,
            "vendedor_id": self._vendedor_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Producto:
        producto = cls(
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["stock"],
            data["categoria_id"],
            data["vendedor_id"],
        )
        producto._id = data["id"]
        return producto


# ================================================================================
# ARCHIVO 4/4: vendedor.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/vendedor.py
# ================================================================================

from __future__ import annotations
import uuid

class Vendedor:
    """Representa un vendedor en el e-commerce."""

    def __init__(self, nombre: str, email: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._email = email

    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def __str__(self) -> str:
        return f"Vendedor(ID: {self._id}, Nombre: {self._nombre}, Email: {self._email})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "email": self._email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Vendedor:
        vendedor = cls(data["nombre"], data["email"])
        vendedor._id = data["id"]
        return vendedor


