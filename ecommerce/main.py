import os
import json
import pickle

from ecommerce.constantes import DATA_DIR

from ecommerce.entidades.compras.procesador_pago import ProcesadorPago

from ecommerce.excepciones.ecommerce_exception import EcommerceException

from ecommerce.patrones.observer.observadores.analytics_observer import AnalyticsObserver
from ecommerce.patrones.observer.observadores.email_observer import EmailObserver
from ecommerce.patrones.observer.observadores.inventario_observer import InventarioObserver
from ecommerce.patrones.observer.observadores.sms_observer import SmsObserver

from ecommerce.entidades.catalogo.categoria import Categoria
from ecommerce.entidades.catalogo.producto import Producto
from ecommerce.entidades.catalogo.vendedor import Vendedor

from ecommerce.servicios.catalogo.catalogo_service_registry import CatalogoServiceRegistry
from ecommerce.servicios.catalogo.producto_service import ProductoService
from ecommerce.servicios.catalogo.vendedor_service import VendedorService
from ecommerce.servicios.compras.carrito_service import CarritoService
from ecommerce.servicios.compras.compra_service import CompraService
from ecommerce.servicios.membresias.membresia_service import MembresiaService
from ecommerce.servicios.ordenes.orden_service import OrdenService
from ecommerce.servicios.usuarios.perfil_service import PerfilService
from ecommerce.servicios.usuarios.usuario_service import UsuarioService

class ECommerceApp:
    def __init__(self):
        self.usuario_service = UsuarioService()
        self.perfil_service = PerfilService()
        self.membresia_service = MembresiaService()
        self.vendedor_service = VendedorService()
        self.producto_service = ProductoService()
        self.carrito_service = CarritoService(self.producto_service)
        self.orden_service = OrdenService()
        self.procesador_pago = ProcesadorPago()
        self.compra_service = CompraService(self.producto_service, self.orden_service, self.procesador_pago)

        # Registrar observadores
        self.compra_service.agregar_observador(AnalyticsObserver())
        self.compra_service.agregar_observador(EmailObserver())
        self.compra_service.agregar_observador(InventarioObserver())
        self.compra_service.agregar_observador(SmsObserver())

    def guardar_estado(self, filename="ecommerce_snapshot.pkl"):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'wb') as f:
            pickle.dump({
                "usuario_service": self.usuario_service.to_dict(),
                "perfil_service": self.perfil_service.to_dict(),
                "membresia_service": self.membresia_service.to_dict(),
                "catalogo_registry": CatalogoServiceRegistry().to_dict(),
                "carrito_service": self.carrito_service.to_dict(),
                "orden_service": self.orden_service.to_dict(),
                "procesador_pago": self.procesador_pago.to_dict(),
            }, f)
        print(f"Estado del sistema guardado en {filepath}")

    def cargar_estado(self, filename="ecommerce_snapshot.pkl"):
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
                self.usuario_service = UsuarioService.from_dict(data["usuario_service"])
                self.perfil_service = PerfilService.from_dict(data["perfil_service"])
                self.membresia_service = MembresiaService.from_dict(data["membresia_service"])
                
                # Cargar el Singleton CatalogoServiceRegistry
                CatalogoServiceRegistry.from_dict(data["catalogo_registry"])

                # Re-inicializar servicios que dependen del registro o de otros servicios
                self.vendedor_service = VendedorService()
                self.producto_service = ProductoService()
                self.carrito_service = CarritoService.from_dict(data["carrito_service"], self.producto_service)
                self.orden_service = OrdenService.from_dict(data["orden_service"])
                self.procesador_pago = ProcesadorPago.from_dict(data["procesador_pago"])
                self.compra_service = CompraService(self.producto_service, self.orden_service, self.procesador_pago)

                # Re-registrar observadores después de cargar
                self.compra_service.agregar_observador(AnalyticsObserver())
                self.compra_service.agregar_observador(EmailObserver())
                self.compra_service.agregar_observador(InventarioObserver())
                self.compra_service.agregar_observador(SmsObserver())

            print(f"Estado del sistema cargado desde {filepath}")
        else:
            print("No se encontró un estado guardado, iniciando con estado vacío.")

    def run_demo(self):
        print("\n--- SISTEMA DE E-COMMERCE ---")

        # 1) Crear usuario + membresía
        print("\n1. Creando usuario y asignando membresía...")
        try:
            usuario1 = self.usuario_service.registrar_usuario("Alice Smith", "alice@example.com", "pass123")
            self.membresia_service.asignar_membresia(usuario1, "PRIME")
            self.perfil_service.crear_perfil(usuario1.get_id(), "Calle Falsa 123", "555-1234")
            print(f"Usuario creado: {usuario1}")
            print(f"Membresía de {usuario1.get_nombre()}: {usuario1.get_membresia().get_tipo()}")

            usuario2 = self.usuario_service.registrar_usuario("Bob Johnson", "bob@example.com", "securepass")
            self.membresia_service.asignar_membresia(usuario2, "PREMIUM")
            self.perfil_service.crear_perfil(usuario2.get_id(), "Avenida Siempre Viva 742", "555-5678")
            print(f"Usuario creado: {usuario2}")
            print(f"Membresía de {usuario2.get_nombre()}: {usuario2.get_membresia().get_tipo()}")

        except EcommerceException as e:
            print(f"Error al crear usuario: {e.get_user_message()}")

        # 2) Crear vendedor + categoría + productos
        print("\n2. Creando vendedor, categoría y productos...")
        vendedor1 = self.vendedor_service.crear_vendedor("TechStore", "ventas@techstore.com")
        categoria1 = CatalogoServiceRegistry().registrar_categoria(Categoria("Electrónica", "Dispositivos electrónicos"))
        categoria2 = CatalogoServiceRegistry().registrar_categoria(Categoria("Libros", "Obras literarias"))

        producto1 = self.producto_service.crear_producto("Laptop X1", "Potente laptop para trabajo", 1200.00, 10, categoria1.get_id(), vendedor1.get_id())
        producto2 = self.producto_service.crear_producto("Mouse Ergonómico", "Mouse cómodo para uso prolongado", 25.00, 50, categoria1.get_id(), vendedor1.get_id())
        producto3 = self.producto_service.crear_producto("El Señor de los Anillos", "Novela épica de fantasía", 30.00, 20, categoria2.get_id(), vendedor1.get_id())

        print(f"Vendedor creado: {vendedor1.get_nombre()}")
        print(f"Categorías: {CatalogoServiceRegistry().listar_categorias()}")
        print(f"Productos: {self.producto_service.listar_productos()}")

        # 3) Armar carrito y agregar ítems
        print("\n3. Armar carrito y agregar ítems...")
        carrito_alice = self.carrito_service.crear_carrito(usuario1.get_id())
        self.carrito_service.agregar_item_a_carrito(usuario1.get_id(), producto1.get_id(), 1)
        self.carrito_service.agregar_item_a_carrito(usuario1.get_id(), producto2.get_id(), 2)
        print(f"Carrito de {usuario1.get_nombre()}: {carrito_alice}")

        carrito_bob = self.carrito_service.crear_carrito(usuario2.get_id())
        self.carrito_service.agregar_item_a_carrito(usuario2.get_id(), producto3.get_id(), 1)
        print(f"Carrito de {usuario2.get_nombre()}: {carrito_bob}")

        # 4) Calcular total usando Strategy (descuento+envío)
        print("\n4. Calculando totales con descuentos y envíos...")
        subtotal_alice = carrito_alice.calcular_total()
        precio_final_alice = self.compra_service.confirmar_compra(usuario1, carrito_alice, "Calle Falsa 123", "tarjeta", 10.0).get_total()
        print(f"Subtotal Alice: {subtotal_alice:.2f}")
        print(f"Total final Alice (con Prime): {precio_final_alice:.2f}")

        subtotal_bob = carrito_bob.calcular_total()
        precio_final_bob = self.compra_service.confirmar_compra(usuario2, carrito_bob, "Avenida Siempre Viva 742", "paypal", 25.0).get_total()
        print(f"Subtotal Bob: {subtotal_bob:.2f}")
        print(f"Total final Bob (con Premium): {precio_final_bob:.2f}")

        # 5) Simular pago y crear Orden (Estado = Pendiente)
        print("\n5. Simulando pago y creando órdenes...")
        orden_alice = self.orden_service.obtener_orden(self.orden_service.listar_ordenes()[0].get_id())
        orden_bob = self.orden_service.obtener_orden(self.orden_service.listar_ordenes()[1].get_id())
        print(f"Orden de Alice creada: {orden_alice}")
        print(f"Orden de Bob creada: {orden_bob}")

        # 6) Avanzar estado: Pendiente → Procesando → Enviado → Entregado
        print("\n6. Avanzando estados de las órdenes...")
        print(f"Estado inicial Alice: {orden_alice.get_estado().get_nombre_estado()}")
        orden_alice.procesar()
        print(f"Estado Alice después de procesar: {orden_alice.get_estado().get_nombre_estado()}")
        orden_alice.enviar()
        print(f"Estado Alice después de enviar: {orden_alice.get_estado().get_nombre_estado()}")
        orden_alice.entregar()
        print(f"Estado Alice después de entregar: {orden_alice.get_estado().get_nombre_estado()}")

        print(f"Estado inicial Bob: {orden_bob.get_estado().get_nombre_estado()}")
        orden_bob.procesar()
        print(f"Estado Bob después de procesar: {orden_bob.get_estado().get_nombre_estado()}")
        orden_bob.enviar()
        print(f"Estado Bob después de enviar: {orden_bob.get_estado().get_nombre_estado()}")
        orden_bob.entregar()
        print(f"Estado Bob después de entregar: {orden_bob.get_estado().get_nombre_estado()}")

        # 7) Enviar notificaciones (Observer) - Ya se hicieron durante la confirmación de compra
        print("\n7. Las notificaciones (Observer) se activaron automáticamente al crear las órdenes.")

        # 8) Guardar snapshot en data/ y volver a cargarlo
        print("\n8. Guardando y cargando estado del sistema...")
        self.guardar_estado()
        
        # Crear una nueva instancia de la aplicación para simular una recarga completa
        app_recargada = ECommerceApp()
        app_recargada.cargar_estado()

        print("\nVerificando estado cargado (ej. órdenes de Alice y Bob):")
        orden_alice_cargada = app_recargada.orden_service.obtener_orden(orden_alice.get_id())
        orden_bob_cargada = app_recargada.orden_service.obtener_orden(orden_bob.get_id())
        print(f"Orden Alice cargada: {orden_alice_cargada} (Estado: {orden_alice_cargada.get_estado().get_nombre_estado()})")
        print(f"Orden Bob cargada: {orden_bob_cargada} (Estado: {orden_bob_cargada.get_estado().get_nombre_estado()})")

        print("\n--- DEMO FINALIZADA ---")

if __name__ == "__main__":
    app = ECommerceApp()
    app.run_demo()
