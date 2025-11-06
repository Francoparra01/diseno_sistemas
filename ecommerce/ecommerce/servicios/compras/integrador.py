"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/__init__.py
# ================================================================================

"""Servicios relacionados con el proceso de compra y carrito."""


# ================================================================================
# ARCHIVO 2/3: carrito_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/carrito_service.py
# ================================================================================

from __future__ import annotations
from typing import Dict

from ecommerce.entidades.compras.carrito import Carrito
from ecommerce.entidades.compras.item_carrito import ItemCarrito
from ecommerce.servicios.catalogo.producto_service import ProductoService

class CarritoService:
    """Servicio para la gestión de carritos de compra."""

    def __init__(self, producto_service: ProductoService):
        self._carritos: Dict[str, Carrito] = {}
        self._producto_service = producto_service

    def crear_carrito(self, usuario_id: str) -> Carrito:
        if usuario_id in self._carritos:
            return self._carritos[usuario_id]
        carrito = Carrito(usuario_id)
        self._carritos[usuario_id] = carrito
        return carrito

    def obtener_carrito(self, usuario_id: str) -> Carrito | None:
        return self._carritos.get(usuario_id)

    def agregar_item_a_carrito(self, usuario_id: str, producto_id: str, cantidad: int):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")

        producto = self._producto_service.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")

        item = ItemCarrito(producto_id, cantidad, producto.get_precio())
        carrito.agregar_item(item)

    def remover_item_de_carrito(self, usuario_id: str, producto_id: str):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.remover_item(producto_id)

    def actualizar_cantidad_item_carrito(self, usuario_id: str, producto_id: str, cantidad: int):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.actualizar_cantidad(producto_id, cantidad)

    def vaciar_carrito(self, usuario_id: str):
        carrito = self.obtener_carrito(usuario_id)
        if not carrito:
            raise ValueError(f"Carrito para usuario {usuario_id} no encontrado.")
        carrito.vaciar()

    def to_dict(self) -> dict:
        return {
            "carritos": {uid: carrito.to_dict() for uid, carrito in self._carritos.items()},
        }

    @classmethod
    def from_dict(cls, data: dict, producto_service: ProductoService) -> CarritoService:
        carrito_service = cls(producto_service)
        carrito_service._carritos = {uid: Carrito.from_dict(carrito_data) for uid, carrito_data in data["carritos"].items()}
        return carrito_service


# ================================================================================
# ARCHIVO 3/3: compra_service.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/compra_service.py
# ================================================================================

from __future__ import annotations
from typing import Dict, List

from ecommerce.entidades.compras.carrito import Carrito
from ecommerce.entidades.compras.procesador_pago import ProcesadorPago
from ecommerce.entidades.ordenes.orden import Orden
from ecommerce.entidades.ordenes.item_orden import ItemOrden
from ecommerce.entidades.usuarios.usuario import Usuario

from ecommerce.excepciones.carrito_vacio_exception import CarritoVacioException
from ecommerce.excepciones.pago_rechazado_exception import PagoRechazadoException
from ecommerce.excepciones.stock_insuficiente_exception import StockInsuficienteException

from ecommerce.servicios.catalogo.producto_service import ProductoService
from ecommerce.servicios.precio_service import PrecioService
from ecommerce.servicios.ordenes.orden_service import OrdenService

from ecommerce.patrones.observer.observable import Observable

class CompraService(Observable):
    """Servicio para gestionar el proceso de compra, desde el carrito hasta la orden."""

    def __init__(self, producto_service: ProductoService, orden_service: OrdenService, procesador_pago: ProcesadorPago):
        super().__init__()
        self._producto_service = producto_service
        self._orden_service = orden_service
        self._procesador_pago = procesador_pago

    def _convertir_carrito_a_items_orden(self, carrito: Carrito) -> List[ItemOrden]:
        items_orden = []
        for item_carrito in carrito.get_items().values():
            producto = self._producto_service.obtener_producto(item_carrito.get_producto_id())
            if not producto:
                raise ValueError(f"Producto con ID {item_carrito.get_producto_id()} no encontrado.")
            items_orden.append(ItemOrden(
                producto_id=producto.get_id(),
                nombre_producto=producto.get_nombre(),
                cantidad=item_carrito.get_cantidad(),
                precio_unitario=producto.get_precio()
            ))
        return items_orden

    def confirmar_compra(self, usuario: Usuario, carrito: Carrito, direccion_envio: str, metodo_pago: str, distancia_envio: float) -> Orden:
        if not carrito.get_items():
            raise CarritoVacioException()

        # 1. Verificar y reducir stock
        for item_carrito in carrito.get_items().values():
            self._producto_service.verificar_y_reducir_stock(item_carrito.get_producto_id(), item_carrito.get_cantidad())

        # 2. Calcular total con estrategias de precio y envío
        precio_service = PrecioService(
            usuario.get_membresia().get_descuento_strategy(),
            usuario.get_membresia().get_envio_strategy()
        )
        subtotal = carrito.calcular_total()
        total_final = precio_service.calcular_precio_final(subtotal, distancia_envio)

        # 3. Procesar pago
        try:
            transaccion_id = self._procesador_pago.procesar_pago(total_final, metodo_pago)
        except PagoRechazadoException as e:
            # Si el pago falla, revertir stock
            for item_carrito in carrito.get_items().values():
                self._producto_service.actualizar_stock(item_carrito.get_producto_id(), item_carrito.get_cantidad())
            raise e

        # 4. Crear orden
        items_orden = self._convertir_carrito_a_items_orden(carrito)
        orden = self._orden_service.crear_orden(usuario.get_id(), items_orden, total_final, direccion_envio)
        orden.set_transaccion_id(transaccion_id)

        # 5. Vaciar carrito
        carrito.vaciar()

        # 6. Notificar observadores
        self.notificar_observadores("orden_creada", {
            "orden_id": orden.get_id(),
            "usuario_id": usuario.get_id(),
            "total": total_final,
            "items": [item.to_dict() for item in items_orden],
            "transaccion_id": transaccion_id,
        })

        return orden

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict, producto_service: ProductoService, orden_service: OrdenService, procesador_pago: ProcesadorPago) -> CompraService:
        return cls(producto_service, orden_service, procesador_pago)


