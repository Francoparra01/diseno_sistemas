"""
Archivo integrador generado automáticamente
Directorio: /home/parra1/diseno_sistemas/ecommerce
Fecha: 2025-11-05 21:26:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: buscar_paquete.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/buscar_paquete.py
# ================================================================================

"""
Script utilitario para proyectos Python.

Funciones principales:
1) Buscar un paquete Python (con __init__.py) en el árbol de directorios.
2) Integrar el contenido de todos los .py de cada carpeta en 'integrador.py'
   y generar un 'integradorFinal.py' en la raíz con TODO el código consolidado.

Uso rápido:
- Buscar paquete 'ecommerce' (por defecto):
    python buscar_paquete.py

- Buscar paquete con nombre específico:
    python buscar_paquete.py paquete ecommerce

- Integrar todos los .py a partir de un directorio (el actual por defecto):
    python buscar_paquete.py integrar
    python buscar_paquete.py integrar ruta/al/directorio

- Ayuda:
    python buscar_paquete.py -h
"""
import os
import sys
from datetime import datetime

DEFAULT_PACKAGE = "ecommerce"

# --------------------------------------------------------------------------------------
# Utilidades de búsqueda e integración
# --------------------------------------------------------------------------------------
def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la búsqueda
        nombre_paquete: Nombre del paquete a buscar (p.ej. 'ecommerce')

    Returns:
        Lista de rutas donde se encontró el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        nombre_dir = os.path.basename(raiz)
        if nombre_dir == nombre_paquete:
            if "__init__.py" in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero NO es paquete Python (falta __init__.py): {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursión).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith(".py"):
                # Excluir archivos integradores y __init__ si no los querés duplicar
                if item not in ["integrador.py", "integradorFinal.py"]:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales/ruidosos
                if item not in {"__pycache__", "venv", ".venv", ".git"} and not item.startswith("."):
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.
    """
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python del directorio.
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, "integrador.py")

    try:
        with open(ruta_integrador, "w", encoding="utf-8") as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write("Archivo integrador generado automáticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list | None = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel (DFS).
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio) or directorio}")

    # 1) Descender a subdirectorios (DFS)
    for subdir in obtener_subdirectorios(directorio):
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # 2) Integrar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el código fuente de todas las ramas.
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, "integradorFinal.py")

    # Agrupar por directorio
    archivos_por_directorio: dict[str, list[str]] = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        archivos_por_directorio.setdefault(directorio, []).append(archivo)

    try:
        with open(ruta_integrador_final, "w", encoding="utf-8") as integrador_final:
            # Encabezado
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACIÓN COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raíz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Tamaño
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamaño del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integración para todo el árbol de directorios.
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACIÓN DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raíz: {directorio_raiz}\n")

    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACIÓN POR NIVELES COMPLETADA")
    print("=" * 80)

    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)

# --------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------
def mostrar_ayuda():
    print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
    print("")
    print("Comandos disponibles:")
    print("  (sin argumentos)        Busca el paquete por defecto 'ecommerce' desde el directorio del script")
    print("  paquete <NOMBRE>        Busca un paquete Python llamado <NOMBRE>")
    print("  integrar [DIR]          Integra archivos .py recursivamente a partir de DIR (por defecto: este directorio)")
    print("  help | -h | --help      Muestra esta ayuda")
    print("")
    print("Ejemplos:")
    print("  python buscar_paquete.py")
    print("  python buscar_paquete.py paquete ecommerce")
    print("  python buscar_paquete.py integrar")
    print("  python buscar_paquete.py integrar ecommerce")


def main():
    """Función principal del script."""
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Sin argumentos → buscar paquete por defecto
    if len(sys.argv) == 1:
        nombre = DEFAULT_PACKAGE
        print(f"[INFO] Buscando desde: {directorio_raiz}")
        print(f"[INFO] Buscando paquete: {nombre}\n")
        paquetes = buscar_paquete(directorio_raiz, nombre)
        print("")
        if paquetes:
            print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
            for paquete in paquetes:
                print(f"  - {paquete}")
                print(f"    Contenido:")
                try:
                    contenido = os.listdir(paquete)
                    for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                        ruta_item = os.path.join(paquete, item)
                        if os.path.isdir(ruta_item):
                            print(f"      [DIR]  {item}")
                        else:
                            print(f"      [FILE] {item}")
                    if len(contenido) > 10:
                        print(f"      ... y {len(contenido) - 10} ítems más")
                except PermissionError:
                    print("      [!] Sin permisos para leer el directorio")
            return 0
        else:
            print(f"[!] No se encontró el paquete '{nombre}'")
            return 1

    # Con argumentos
    comando = sys.argv[1].lower()

    if comando in {"help", "--help", "-h"}:
        mostrar_ayuda()
        return 0

    if comando == "paquete":
        if len(sys.argv) < 3:
            print("[!] Falta el nombre del paquete. Ej: python buscar_paquete.py paquete ecommerce")
            return 1
        nombre = sys.argv[2]
        print(f"[INFO] Buscando desde: {directorio_raiz}")
        print(f"[INFO] Buscando paquete: {nombre}\n")
        paquetes = buscar_paquete(directorio_raiz, nombre)
        print("")
        if paquetes:
            print(f"[OK] Se encontraron {len(paquetes)} paquete(s).")
            for p in paquetes:
                print(f"  - {p}")
            return 0
        print(f"[!] No se encontró el paquete '{nombre}'")
        return 1

    if comando == "integrar":
        if len(sys.argv) > 2:
            directorio_objetivo = sys.argv[2]
            if not os.path.isabs(directorio_objetivo):
                directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
        else:
            directorio_objetivo = directorio_raiz

        if not os.path.isdir(directorio_objetivo):
            print(f"[!] El directorio no existe: {directorio_objetivo}")
            return 1

        integrar_arbol_directorios(directorio_objetivo)
        return 0

    print(f"[!] Comando desconocido: {comando}")
    print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
    return 1


if __name__ == "__main__":
    sys.exit(main())


# ================================================================================
# ARCHIVO 2/2: main.py
# Ruta: /home/parra1/diseno_sistemas/ecommerce/main.py
# ================================================================================

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


