"""
INTEGRADOR FINAL - CONSOLIDACIÓN COMPLETA DEL PROYECTO
============================================================================
Directorio raíz: /home/parra1/diseno_sistemas/ecommerce
Fecha de generación: 2025-11-05 21:26:25
Total de archivos integrados: 75
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. buscar_paquete.py
#   2. main.py
#
# DIRECTORIO: ecommerce
#   3. __init__.py
#   4. constantes.py
#
# DIRECTORIO: ecommerce/entidades
#   5. __init__.py
#
# DIRECTORIO: ecommerce/entidades/catalogo
#   6. __init__.py
#   7. categoria.py
#   8. producto.py
#   9. vendedor.py
#
# DIRECTORIO: ecommerce/entidades/compras
#   10. __init__.py
#   11. carrito.py
#   12. item_carrito.py
#   13. procesador_pago.py
#
# DIRECTORIO: ecommerce/entidades/ordenes
#   14. __init__.py
#   15. item_orden.py
#   16. orden.py
#
# DIRECTORIO: ecommerce/entidades/usuarios
#   17. __init__.py
#   18. membresia.py
#   19. membresia_basic.py
#   20. membresia_premium.py
#   21. membresia_prime.py
#   22. perfil.py
#   23. usuario.py
#
# DIRECTORIO: ecommerce/excepciones
#   24. __init__.py
#   25. carrito_vacio_exception.py
#   26. ecommerce_exception.py
#   27. operacion_no_permitida_exception.py
#   28. pago_rechazado_exception.py
#   29. persistencia_exception.py
#   30. stock_insuficiente_exception.py
#   31. usuario_existente_exception.py
#
# DIRECTORIO: ecommerce/patrones
#   32. __init__.py
#
# DIRECTORIO: ecommerce/patrones/factory
#   33. __init__.py
#   34. membresia_factory.py
#
# DIRECTORIO: ecommerce/patrones/observer
#   35. __init__.py
#   36. observable.py
#   37. observer.py
#
# DIRECTORIO: ecommerce/patrones/observer/observadores
#   38. __init__.py
#   39. analytics_observer.py
#   40. email_observer.py
#   41. inventario_observer.py
#   42. sms_observer.py
#
# DIRECTORIO: ecommerce/patrones/state
#   43. __init__.py
#   44. estado_cancelado.py
#   45. estado_entregado.py
#   46. estado_enviado.py
#   47. estado_orden.py
#   48. estado_pendiente.py
#   49. estado_procesando.py
#
# DIRECTORIO: ecommerce/patrones/strategy
#   50. __init__.py
#   51. descuento_strategy.py
#   52. envio_strategy.py
#
# DIRECTORIO: ecommerce/patrones/strategy/impl
#   53. __init__.py
#   54. descuento_basic_strategy.py
#   55. descuento_premium_strategy.py
#   56. descuento_prime_strategy.py
#   57. envio_basic_strategy.py
#   58. envio_premium_strategy.py
#   59. envio_prime_strategy.py
#
# DIRECTORIO: ecommerce/servicios
#   60. __init__.py
#   61. precio_service.py
#
# DIRECTORIO: ecommerce/servicios/catalogo
#   62. __init__.py
#   63. catalogo_service_registry.py
#   64. producto_service.py
#   65. vendedor_service.py
#
# DIRECTORIO: ecommerce/servicios/compras
#   66. __init__.py
#   67. carrito_service.py
#   68. compra_service.py
#
# DIRECTORIO: ecommerce/servicios/membresias
#   69. __init__.py
#   70. membresia_service.py
#
# DIRECTORIO: ecommerce/servicios/ordenes
#   71. __init__.py
#   72. orden_service.py
#
# DIRECTORIO: ecommerce/servicios/usuarios
#   73. __init__.py
#   74. perfil_service.py
#   75. usuario_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/75: buscar_paquete.py
# Directorio: .
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/buscar_paquete.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 2/75: main.py
# Directorio: .
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/main.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: ecommerce
################################################################################

# ==============================================================================
# ARCHIVO 3/75: __init__.py
# Directorio: ecommerce
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/75: constantes.py
# Directorio: ecommerce
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/constantes.py
# ==============================================================================


# Constantes del sistema E-Commerce

# Descuentos por membresía (porcentaje)
DESCUENTO_BASIC = 0.00       # 0%
DESCUENTO_PRIME = 0.05       # 5%
DESCUENTO_PREMIUM = 0.12     # 12%

# Costos base de envío
ENVIO_BASIC = 1500.0
ENVIO_PRIME = 0.0
ENVIO_PREMIUM = 0.0

# Estados de la Orden
ESTADO_PENDIENTE = 'PENDIENTE'
ESTADO_PROCESANDO = 'PROCESANDO'
ESTADO_ENVIADO = 'ENVIADO'
ESTADO_ENTREGADO = 'ENTREGADO'
ESTADO_CANCELADO = 'CANCELADO'

# Persistencia
DATA_DIR = 'data'



################################################################################
# DIRECTORIO: ecommerce/entidades
################################################################################

# ==============================================================================
# ARCHIVO 5/75: __init__.py
# Directorio: ecommerce/entidades
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/__init__.py
# ==============================================================================

"""Módulo que contiene las definiciones de las entidades del dominio E-commerce."""



################################################################################
# DIRECTORIO: ecommerce/entidades/catalogo
################################################################################

# ==============================================================================
# ARCHIVO 6/75: __init__.py
# Directorio: ecommerce/entidades/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/__init__.py
# ==============================================================================

"""Entidades relacionadas con el catálogo de productos."""


# ==============================================================================
# ARCHIVO 7/75: categoria.py
# Directorio: ecommerce/entidades/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/categoria.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 8/75: producto.py
# Directorio: ecommerce/entidades/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/producto.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 9/75: vendedor.py
# Directorio: ecommerce/entidades/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/catalogo/vendedor.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: ecommerce/entidades/compras
################################################################################

# ==============================================================================
# ARCHIVO 10/75: __init__.py
# Directorio: ecommerce/entidades/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/__init__.py
# ==============================================================================

"""Entidades relacionadas con el proceso de compra."""


# ==============================================================================
# ARCHIVO 11/75: carrito.py
# Directorio: ecommerce/entidades/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/carrito.py
# ==============================================================================

from __future__ import annotations
import uuid
from typing import Dict
from ecommerce.entidades.compras.item_carrito import ItemCarrito

class Carrito:
    """Representa el carrito de compras de un usuario."""

    def __init__(self, usuario_id: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._items: Dict[str, ItemCarrito] = {}

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_items(self) -> Dict[str, ItemCarrito]:
        return self._items

    def agregar_item(self, item: ItemCarrito):
        self._items[item.get_producto_id()] = item

    def remover_item(self, producto_id: str):
        if producto_id in self._items:
            del self._items[producto_id]

    def actualizar_cantidad(self, producto_id: str, cantidad: int):
        if producto_id in self._items:
            self._items[producto_id].set_cantidad(cantidad)

    def vaciar(self):
        self._items.clear()

    def calcular_total(self) -> float:
        return sum(item.calcular_subtotal() for item in self._items.values())

    def __str__(self) -> str:
        items_str = "\n    ".join(str(item) for item in self._items.values())
        return (
            f"Carrito(ID: {self._id}, Usuario ID: {self._usuario_id}, "
            f"Items: {len(self._items)})"
            + (f"\n    {items_str}" if items_str else "")
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "items": {pid: item.to_dict() for pid, item_data in self._items.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> Carrito:
        carrito = cls(data["usuario_id"])
        carrito._id = data["id"]
        carrito._items = {pid: ItemCarrito.from_dict(item_data) for pid, item_data in data["items"].items()}
        return carrito


# ==============================================================================
# ARCHIVO 12/75: item_carrito.py
# Directorio: ecommerce/entidades/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/item_carrito.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 13/75: procesador_pago.py
# Directorio: ecommerce/entidades/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/compras/procesador_pago.py
# ==============================================================================

from __future__ import annotations
import uuid
from datetime import datetime

from ecommerce.excepciones.pago_rechazado_exception import PagoRechazadoException

class ProcesadorPago:
    """Simula un procesador de pagos externo."""

    def __init__(self):
        self._transacciones = {}

    def procesar_pago(self, monto: float, metodo_pago: str) -> str:
        """Simula el procesamiento de un pago.

        Args:
            monto: El monto a pagar.
            metodo_pago: El método de pago (ej. 'tarjeta', 'paypal').

        Returns:
            Un ID de transacción si el pago es exitoso.

        Raises:
            PagoRechazadoException: Si el pago es rechazado.
        """
        if monto <= 0:
            raise ValueError("El monto a pagar debe ser positivo.")

        # Simulación de lógica de rechazo
        if "rechazar" in metodo_pago.lower():
            raise PagoRechazadoException(f"Método de pago '{metodo_pago}' configurado para rechazo.")

        transaccion_id = str(uuid.uuid4())
        self._transacciones[transaccion_id] = {
            "monto": monto,
            "metodo_pago": metodo_pago,
            "fecha": datetime.now().isoformat(),
            "estado": "aprobado",
        }
        return transaccion_id

    def get_estado_transaccion(self, transaccion_id: str) -> dict | None:
        """Obtiene el estado de una transacción."""
        return self._transacciones.get(transaccion_id)

    def to_dict(self) -> dict:
        return {
            "transacciones": self._transacciones,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ProcesadorPago:
        procesador = cls()
        procesador._transacciones = data["transacciones"]
        return procesador



################################################################################
# DIRECTORIO: ecommerce/entidades/ordenes
################################################################################

# ==============================================================================
# ARCHIVO 14/75: __init__.py
# Directorio: ecommerce/entidades/ordenes
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/__init__.py
# ==============================================================================

"""Entidades relacionadas con las órdenes de compra."""


# ==============================================================================
# ARCHIVO 15/75: item_orden.py
# Directorio: ecommerce/entidades/ordenes
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/item_orden.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 16/75: orden.py
# Directorio: ecommerce/entidades/ordenes
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/ordenes/orden.py
# ==============================================================================

from __future__ import annotations
import uuid
from datetime import datetime
from typing import List

from ecommerce.entidades.ordenes.item_orden import ItemOrden
from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_pendiente import EstadoPendiente

class Orden:
    """Representa una orden de compra realizada por un usuario."""

    def __init__(self, usuario_id: str, items: List[ItemOrden], total: float, direccion_envio: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._fecha_creacion = datetime.now().isoformat()
        self._items = items
        self._total = total
        self._direccion_envio = direccion_envio
        self._estado: EstadoOrden = EstadoPendiente()
        self._transaccion_id: str | None = None

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_fecha_creacion(self) -> str:
        return self._fecha_creacion

    def get_items(self) -> List[ItemOrden]:
        return self._items

    def get_total(self) -> float:
        return self._total

    def get_direccion_envio(self) -> str:
        return self._direccion_envio

    def get_estado(self) -> EstadoOrden:
        return self._estado

    def set_estado(self, estado: EstadoOrden):
        self._estado = estado

    def get_transaccion_id(self) -> str | None:
        return self._transaccion_id

    def set_transaccion_id(self, transaccion_id: str):
        self._transaccion_id = transaccion_id

    # Métodos de transición de estado
    def procesar(self):
        self._estado.procesar(self)

    def enviar(self):
        self._estado.enviar(self)

    def entregar(self):
        self._estado.entregar(self)

    def cancelar(self):
        self._estado.cancelar(self)

    def __str__(self) -> str:
        return f"Orden(ID: {self._id}, Usuario ID: {self._usuario_id}, Total: {self._total}, Estado: {self._estado.get_nombre_estado()})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "fecha_creacion": self._fecha_creacion,
            "items": [item.to_dict() for item in self._items],
            "total": self._total,
            "direccion_envio": self._direccion_envio,
            "estado": self._estado.get_nombre_estado(), # Guardamos solo el nombre del estado
            "transaccion_id": self._transaccion_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Orden:
        # La reconstrucción del estado se hará en el servicio de órdenes
        # para evitar dependencias circulares y manejar la lógica de estados.
        orden = cls(
            data["usuario_id"],
            [ItemOrden.from_dict(item_data) for item_data in data["items"]],
            data["total"],
            data["direccion_envio"],
        )
        orden._id = data["id"]
        orden._fecha_creacion = data["fecha_creacion"]
        orden._transaccion_id = data["transaccion_id"]
        # El estado se establecerá externamente después de la creación de la orden
        return orden



################################################################################
# DIRECTORIO: ecommerce/entidades/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 17/75: __init__.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/__init__.py
# ==============================================================================

"""Entidades relacionadas con los usuarios y sus membresías."""


# ==============================================================================
# ARCHIVO 18/75: membresia.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy


class Membresia(ABC):
    """Clase abstracta base para las membresías de usuario."""

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    @abstractmethod
    def get_descuento(self) -> float:
        pass

    @abstractmethod
    def get_costo_envio(self) -> float:
        pass

    @abstractmethod
    def get_descuento_strategy(self) -> DescuentoStrategy:
        pass

    @abstractmethod
    def get_envio_strategy(self) -> EnvioStrategy:
        pass

    def to_dict(self) -> dict:
        return {
            "tipo": self.get_tipo(),
            "descuento": self.get_descuento(),
            "costo_envio": self.get_costo_envio(),
        }


# ==============================================================================
# ARCHIVO 19/75: membresia_basic.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_basic.py
# ==============================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_BASIC, ENVIO_BASIC
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_basic_strategy import DescuentoBasicStrategy
from ecommerce.patrones.strategy.impl.envio_basic_strategy import EnvioBasicStrategy


class MembresiaBasic(Membresia):
    """Membresía básica sin descuento y con costo de envío estándar."""

    def get_tipo(self) -> str:
        return "BASIC"

    def get_descuento(self) -> float:
        return DESCUENTO_BASIC

    def get_costo_envio(self) -> float:
        return ENVIO_BASIC

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoBasicStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioBasicStrategy()

    def __str__(self) -> str:
        return f"MembresiaBasic(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaBasic:
        return cls()


# ==============================================================================
# ARCHIVO 20/75: membresia_premium.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_premium.py
# ==============================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PREMIUM, ENVIO_PREMIUM
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_premium_strategy import DescuentoPremiumStrategy
from ecommerce.patrones.strategy.impl.envio_premium_strategy import EnvioPremiumStrategy


class MembresiaPremium(Membresia):
    """Membresía Premium con descuento y costo de envío reducido."""

    def get_tipo(self) -> str:
        return "PREMIUM"

    def get_descuento(self) -> float:
        return DESCUENTO_PREMIUM

    def get_costo_envio(self) -> float:
        return ENVIO_PREMIUM

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPremiumStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPremiumStrategy()

    def __str__(self) -> str:
        return f"MembresiaPremium(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPremium:
        return cls()


# ==============================================================================
# ARCHIVO 21/75: membresia_prime.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/membresia_prime.py
# ==============================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PRIME, ENVIO_PRIME
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_prime_strategy import DescuentoPrimeStrategy
from ecommerce.patrones.strategy.impl.envio_prime_strategy import EnvioPrimeStrategy


class MembresiaPrime(Membresia):
    """Membresía Prime con descuento y envío gratuito."""

    def get_tipo(self) -> str:
        return "PRIME"

    def get_descuento(self) -> float:
        return DESCUENTO_PRIME

    def get_costo_envio(self) -> float:
        return ENVIO_PRIME

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPrimeStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPrimeStrategy()

    def __str__(self) -> str:
        return f"MembresiaPrime(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPrime:
        return cls()


# ==============================================================================
# ARCHIVO 22/75: perfil.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/perfil.py
# ==============================================================================

from __future__ import annotations
import uuid

class Perfil:
    """Representa el perfil de un usuario con información adicional."""

    def __init__(self, usuario_id: str, direccion: str, telefono: str):
        self._id = str(uuid.uuid4())
        self._usuario_id = usuario_id
        self._direccion = direccion
        self._telefono = telefono

    def get_id(self) -> str:
        return self._id

    def get_usuario_id(self) -> str:
        return self._usuario_id

    def get_direccion(self) -> str:
        return self._direccion

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def get_telefono(self) -> str:
        return self._telefono

    def set_telefono(self, telefono: str):
        self._telefono = telefono

    def __str__(self) -> str:
        return f"Perfil(ID: {self._id}, Usuario ID: {self._usuario_id}, Dirección: {self._direccion})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "usuario_id": self._usuario_id,
            "direccion": self._direccion,
            "telefono": self._telefono,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Perfil:
        perfil = cls(data["usuario_id"], data["direccion"], data["telefono"])
        perfil._id = data["id"]
        return perfil


# ==============================================================================
# ARCHIVO 23/75: usuario.py
# Directorio: ecommerce/entidades/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/entidades/usuarios/usuario.py
# ==============================================================================

from __future__ import annotations
import uuid

from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.entidades.usuarios.membresia_basic import MembresiaBasic

class Usuario:
    """Representa un usuario del sistema E-commerce."""

    def __init__(self, nombre: str, email: str, password: str):
        self._id = str(uuid.uuid4())
        self._nombre = nombre
        self._email = email
        self._password = password  # En un sistema real, esto estaría hasheado
        self._membresia: Membresia = MembresiaBasic()

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

    def verificar_password(self, password: str) -> bool:
        # En un sistema real, se compararía el hash
        return self._password == password

    def set_password(self, password: str):
        self._password = password

    def get_membresia(self) -> Membresia:
        return self._membresia

    def set_membresia(self, membresia: Membresia):
        self._membresia = membresia

    def __str__(self) -> str:
        return f"Usuario(ID: {self._id}, Nombre: {self._nombre}, Email: {self._email}, Membresía: {self._membresia.get_tipo()})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "email": self._email,
            "password": self._password,
            "membresia": self._membresia.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> Usuario:
        from ecommerce.patrones.factory.membresia_factory import MembresiaFactory

        usuario = cls(data["nombre"], data["email"], data["password"])
        usuario._id = data["id"]
        usuario._membresia = MembresiaFactory.crear_membresia(data["membresia"]["tipo"])
        return usuario



################################################################################
# DIRECTORIO: ecommerce/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 24/75: __init__.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/__init__.py
# ==============================================================================

"""Paquete de excepciones personalizadas del e-commerce."""
from .ecommerce_exception import EcommerceException
from .usuario_existente_exception import UsuarioExistenteException
from .stock_insuficiente_exception import StockInsuficienteException
from .carrito_vacio_exception import CarritoVacioException
from .pago_rechazado_exception import PagoRechazadoException
from .persistencia_exception import PersistenciaException
from .operacion_no_permitida_exception import OperacionNoPermitidaException


# ==============================================================================
# ARCHIVO 25/75: carrito_vacio_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/carrito_vacio_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class CarritoVacioException(EcommerceException):
    """Se intenta confirmar una compra con carrito vacío."""

    def __init__(self):
        super().__init__(
            user_message="El carrito está vacío.",
            technical_message="Operación inválida: carrito vacío",
        )


# ==============================================================================
# ARCHIVO 26/75: ecommerce_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/ecommerce_exception.py
# ==============================================================================

from __future__ import annotations

class EcommerceException(Exception):
    """Excepción base del dominio E-commerce.

    Atributos:
        user_message: Mensaje claro para el usuario.
        technical_message: Detalle técnico para logs.
    """

    def __init__(self, user_message: str, technical_message: str | None = None, cause: Exception | None = None):
        super().__init__(technical_message or user_message)
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        if cause is not None:
            self.__cause__ = cause

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"{self._user_message} | {self._technical_message}"


# ==============================================================================
# ARCHIVO 27/75: operacion_no_permitida_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/operacion_no_permitida_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class OperacionNoPermitidaException(EcommerceException):
    """Operación inválida según las reglas del dominio (por ejemplo, transición de estado no permitida)."""

    def __init__(self, operacion: str):
        super().__init__(
            user_message="Operación no permitida.",
            technical_message=f"Operación no permitida: {operacion}",
        )
        self._operacion = operacion

    def get_operacion(self) -> str:
        return self._operacion


# ==============================================================================
# ARCHIVO 28/75: pago_rechazado_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/pago_rechazado_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class PagoRechazadoException(EcommerceException):
    """El procesador de pagos rechazó la transacción."""

    def __init__(self, motivo: str | None = None):
        detalle = f"Pago rechazado{': ' + motivo if motivo else ''}"
        super().__init__(
            user_message="El pago fue rechazado. Intente con otro método o más tarde.",
            technical_message=detalle,
        )
        self._motivo = motivo

    def get_motivo(self) -> str | None:
        return self._motivo


# ==============================================================================
# ARCHIVO 29/75: persistencia_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/persistencia_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class PersistenciaException(EcommerceException):
    """Error leyendo o escribiendo datos en disco."""

    def __init__(self, path: str, operacion: str, cause: Exception | None = None):
        super().__init__(
            user_message="Ocurrió un error de almacenamiento.",
            technical_message=f"Persistencia fallida: {operacion} en '{path}'",
            cause=cause,
        )
        self._path = path
        self._operacion = operacion

    def get_path(self) -> str:
        return self._path

    def get_operacion(self) -> str:
        return self._operacion


# ==============================================================================
# ARCHIVO 30/75: stock_insuficiente_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/stock_insuficiente_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class StockInsuficienteException(EcommerceException):
    """No hay stock suficiente para el producto solicitado."""

    def __init__(self, producto_id: str, solicitado: int, disponible: int):
        super().__init__(
            user_message="No hay stock suficiente para completar la operación.",
            technical_message=f"Stock insuficiente: producto_id={producto_id}, solicitado={solicitado}, disponible={disponible}",
        )
        self._producto_id = producto_id
        self._solicitado = solicitado
        self._disponible = disponible

    def get_producto_id(self) -> str:
        return self._producto_id

    def get_solicitado(self) -> int:
        return self._solicitado

    def get_disponible(self) -> int:
        return self._disponible


# ==============================================================================
# ARCHIVO 31/75: usuario_existente_exception.py
# Directorio: ecommerce/excepciones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/excepciones/usuario_existente_exception.py
# ==============================================================================

from .ecommerce_exception import EcommerceException

class UsuarioExistenteException(EcommerceException):
    """Se intenta registrar un usuario ya existente (p.ej., por email)."""

    def __init__(self, email: str):
        super().__init__(
            user_message=f"El usuario con email '{email}' ya existe.",
            technical_message=f"Usuario duplicado: email={email}",
        )
        self._email = email

    def get_email(self) -> str:
        return self._email



################################################################################
# DIRECTORIO: ecommerce/patrones
################################################################################

# ==============================================================================
# ARCHIVO 32/75: __init__.py
# Directorio: ecommerce/patrones
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/__init__.py
# ==============================================================================

"""Módulo que contiene la implementación de patrones de diseño."""



################################################################################
# DIRECTORIO: ecommerce/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 33/75: __init__.py
# Directorio: ecommerce/patrones/factory
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/factory/__init__.py
# ==============================================================================

"""Patrón Factory Method para la creación de objetos."""


# ==============================================================================
# ARCHIVO 34/75: membresia_factory.py
# Directorio: ecommerce/patrones/factory
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/factory/membresia_factory.py
# ==============================================================================

from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.entidades.usuarios.membresia_basic import MembresiaBasic
from ecommerce.entidades.usuarios.membresia_prime import MembresiaPrime
from ecommerce.entidades.usuarios.membresia_premium import MembresiaPremium

class MembresiaFactory:
    """Factory Method para crear instancias de Membresia."""

    @staticmethod
    def crear_membresia(tipo: str) -> Membresia:
        if tipo == "BASIC":
            return MembresiaBasic()
        elif tipo == "PRIME":
            return MembresiaPrime()
        elif tipo == "PREMIUM":
            return MembresiaPremium()
        else:
            raise ValueError(f"Tipo de membresía desconocido: {tipo}")



################################################################################
# DIRECTORIO: ecommerce/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 35/75: __init__.py
# Directorio: ecommerce/patrones/observer
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/__init__.py
# ==============================================================================

"""Patrón Observer para notificaciones y eventos."""


# ==============================================================================
# ARCHIVO 36/75: observable.py
# Directorio: ecommerce/patrones/observer
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observable.py
# ==============================================================================

from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

from ecommerce.patrones.observer.observer import Observer

class Observable(ABC):
    """Sujeto observable que notifica a sus observadores."""

    def __init__(self):
        self._observers: List[Observer] = []

    def agregar_observador(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remover_observador(self, observer: Observer):
        self._observers.remove(observer)

    def notificar_observadores(self, evento: str, data: dict):
        for observer in self._observers:
            observer.actualizar(evento, data)


# ==============================================================================
# ARCHIVO 37/75: observer.py
# Directorio: ecommerce/patrones/observer
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observer.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class Observer(ABC):
    """Interfaz para los observadores que reaccionan a eventos."""

    @abstractmethod
    def actualizar(self, evento: str, data: dict):
        pass



################################################################################
# DIRECTORIO: ecommerce/patrones/observer/observadores
################################################################################

# ==============================================================================
# ARCHIVO 38/75: __init__.py
# Directorio: ecommerce/patrones/observer/observadores
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observadores/__init__.py
# ==============================================================================

"""Implementaciones concretas del patrón Observer."""


# ==============================================================================
# ARCHIVO 39/75: analytics_observer.py
# Directorio: ecommerce/patrones/observer/observadores
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observadores/analytics_observer.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class AnalyticsObserver(Observer):
    """Observador que simula el envío de datos a un sistema de analíticas."""

    def actualizar(self, evento: str, data: dict):
        print(f"[ANALYTICS] Evento '{evento}' recibido con datos: {data}")


# ==============================================================================
# ARCHIVO 40/75: email_observer.py
# Directorio: ecommerce/patrones/observer/observadores
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observadores/email_observer.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class EmailObserver(Observer):
    """Observador que simula el envío de correos electrónicos."""

    def actualizar(self, evento: str, data: dict):
        print(f"[EMAIL] Enviando correo por evento '{evento}' con datos: {data}")


# ==============================================================================
# ARCHIVO 41/75: inventario_observer.py
# Directorio: ecommerce/patrones/observer/observadores
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observadores/inventario_observer.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class InventarioObserver(Observer):
    """Observador que simula la actualización del inventario."""

    def actualizar(self, evento: str, data: dict):
        print(f"[INVENTARIO] Actualizando inventario por evento '{evento}' con datos: {data}")


# ==============================================================================
# ARCHIVO 42/75: sms_observer.py
# Directorio: ecommerce/patrones/observer/observadores
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/observer/observadores/sms_observer.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.observer.observer import Observer

class SmsObserver(Observer):
    """Observador que simula el envío de mensajes SMS."""

    def actualizar(self, evento: str, data: dict):
        print(f"[SMS] Enviando SMS por evento '{evento}' con datos: {data}")



################################################################################
# DIRECTORIO: ecommerce/patrones/state
################################################################################

# ==============================================================================
# ARCHIVO 43/75: __init__.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/__init__.py
# ==============================================================================

"""Patrón State para el manejo del ciclo de vida de las órdenes."""


# ==============================================================================
# ARCHIVO 44/75: estado_cancelado.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_cancelado.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_CANCELADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoCancelado(EstadoOrden):
    """Estado de una orden: Cancelada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_CANCELADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden cancelada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden cancelada.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden cancelada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está cancelada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ==============================================================================
# ARCHIVO 45/75: estado_entregado.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_entregado.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENTREGADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEntregado(EstadoOrden):
    """Estado de una orden: Entregada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENTREGADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya entregada.")

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden ya entregada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está entregada.")

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya entregada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ==============================================================================
# ARCHIVO 46/75: estado_enviado.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_enviado.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_entregado import EstadoEntregado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_ENVIADO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoEnviado(EstadoOrden):
    """Estado de una orden: Enviada."""

    def get_nombre_estado(self) -> str:
        return ESTADO_ENVIADO

    def procesar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede procesar una orden ya enviada.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está enviada.")

    def entregar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido entregada.")
        orden.set_estado(EstadoEntregado())

    def cancelar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede cancelar una orden ya enviada.")

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ==============================================================================
# ARCHIVO 47/75: estado_orden.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_orden.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoOrden(ABC):
    """Interfaz base para los estados de una orden."""

    @abstractmethod
    def get_nombre_estado(self) -> str:
        pass

    @abstractmethod
    def procesar(self, orden: Orden):
        pass

    @abstractmethod
    def enviar(self, orden: Orden):
        pass

    @abstractmethod
    def entregar(self, orden: Orden):
        pass

    @abstractmethod
    def cancelar(self, orden: Orden):
        pass


# ==============================================================================
# ARCHIVO 48/75: estado_pendiente.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_pendiente.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_procesando import EstadoProcesando
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PENDIENTE

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoPendiente(EstadoOrden):
    """Estado inicial de una orden: Pendiente."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PENDIENTE

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} está siendo procesada.")
        orden.set_estado(EstadoProcesando())

    def enviar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede enviar una orden pendiente.")

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden pendiente.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()


# ==============================================================================
# ARCHIVO 49/75: estado_procesando.py
# Directorio: ecommerce/patrones/state
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/state/estado_procesando.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.state.estado_orden import EstadoOrden
from ecommerce.patrones.state.estado_enviado import EstadoEnviado
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.excepciones.operacion_no_permitida_exception import OperacionNoPermitidaException
from ecommerce.constantes import ESTADO_PROCESANDO

if TYPE_CHECKING:
    from ecommerce.entidades.ordenes.orden import Orden

class EstadoProcesando(EstadoOrden):
    """Estado de una orden: Procesando."""

    def get_nombre_estado(self) -> str:
        return ESTADO_PROCESANDO

    def procesar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ya está en procesamiento.")

    def enviar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido enviada.")
        orden.set_estado(EstadoEnviado())

    def entregar(self, orden: Orden):
        raise OperacionNoPermitidaException("No se puede entregar una orden que aún no ha sido enviada.")

    def cancelar(self, orden: Orden):
        print(f"Orden {orden.get_id()} ha sido cancelada durante el procesamiento.")
        orden.set_estado(EstadoCancelado())

    def __str__(self) -> str:
        return self.get_nombre_estado()

    def __repr__(self) -> str:
        return self.__str__()



################################################################################
# DIRECTORIO: ecommerce/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 50/75: __init__.py
# Directorio: ecommerce/patrones/strategy
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/__init__.py
# ==============================================================================

"""Patrón Strategy para aplicar diferentes lógicas de negocio."""


# ==============================================================================
# ARCHIVO 51/75: descuento_strategy.py
# Directorio: ecommerce/patrones/strategy
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/descuento_strategy.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class DescuentoStrategy(ABC):
    """Interfaz para estrategias de cálculo de descuento."""

    @abstractmethod
    def aplicar_descuento(self, total: float) -> float:
        pass


# ==============================================================================
# ARCHIVO 52/75: envio_strategy.py
# Directorio: ecommerce/patrones/strategy
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/envio_strategy.py
# ==============================================================================

from __future__ import annotations
from abc import ABC, abstractmethod

class EnvioStrategy(ABC):
    """Interfaz para estrategias de cálculo de costo de envío."""

    @abstractmethod
    def calcular_costo_envio(self, distancia: float) -> float:
        pass



################################################################################
# DIRECTORIO: ecommerce/patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 53/75: __init__.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/__init__.py
# ==============================================================================

"""Implementaciones concretas de las estrategias de descuento y envío."""


# ==============================================================================
# ARCHIVO 54/75: descuento_basic_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_basic_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_BASIC

class DescuentoBasicStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía básica (0%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_BASIC)


# ==============================================================================
# ARCHIVO 55/75: descuento_premium_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_premium_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PREMIUM

class DescuentoPremiumStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Premium (12%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PREMIUM)


# ==============================================================================
# ARCHIVO 56/75: descuento_prime_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/descuento_prime_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.constantes import DESCUENTO_PRIME

class DescuentoPrimeStrategy(DescuentoStrategy):
    """Estrategia de descuento para membresía Prime (5%)."""

    def aplicar_descuento(self, total: float) -> float:
        return total * (1 - DESCUENTO_PRIME)


# ==============================================================================
# ARCHIVO 57/75: envio_basic_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_basic_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_BASIC

class EnvioBasicStrategy(EnvioStrategy):
    """Estrategia de envío para membresía básica (costo fijo)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        # La distancia podría influir, pero para Basic es un costo fijo simple
        return ENVIO_BASIC


# ==============================================================================
# ARCHIVO 58/75: envio_premium_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_premium_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PREMIUM

class EnvioPremiumStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Premium (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PREMIUM


# ==============================================================================
# ARCHIVO 59/75: envio_prime_strategy.py
# Directorio: ecommerce/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/patrones/strategy/impl/envio_prime_strategy.py
# ==============================================================================

from __future__ import annotations
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.constantes import ENVIO_PRIME

class EnvioPrimeStrategy(EnvioStrategy):
    """Estrategia de envío para membresía Prime (envío gratuito)."""

    def calcular_costo_envio(self, distancia: float) -> float:
        return ENVIO_PRIME



################################################################################
# DIRECTORIO: ecommerce/servicios
################################################################################

# ==============================================================================
# ARCHIVO 60/75: __init__.py
# Directorio: ecommerce/servicios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/__init__.py
# ==============================================================================

"""Módulo que contiene la lógica de negocio del sistema E-commerce."""


# ==============================================================================
# ARCHIVO 61/75: precio_service.py
# Directorio: ecommerce/servicios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/precio_service.py
# ==============================================================================

from __future__ import annotations
from typing import TYPE_CHECKING

from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy

if TYPE_CHECKING:
    from ecommerce.entidades.usuarios.membresia import Membresia

class PrecioService:
    """Servicio para calcular precios finales aplicando descuentos y costos de envío."""

    def __init__(self, descuento_strategy: DescuentoStrategy, envio_strategy: EnvioStrategy):
        self._descuento_strategy = descuento_strategy
        self._envio_strategy = envio_strategy

    def calcular_precio_final(self, subtotal: float, distancia_envio: float) -> float:
        total_con_descuento = self._descuento_strategy.aplicar_descuento(subtotal)
        costo_envio = self._envio_strategy.calcular_costo_envio(distancia_envio)
        return total_con_descuento + costo_envio

    def to_dict(self) -> dict:
        # Las estrategias no son serializables directamente aquí, se reconstruyen
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> PrecioService:
        # Este método no se usará directamente para cargar, las estrategias se inyectan
        raise NotImplementedError("PrecioService se construye con estrategias, no se carga directamente.")



################################################################################
# DIRECTORIO: ecommerce/servicios/catalogo
################################################################################

# ==============================================================================
# ARCHIVO 62/75: __init__.py
# Directorio: ecommerce/servicios/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/__init__.py
# ==============================================================================

"""Servicios relacionados con la gestión del catálogo de productos."""


# ==============================================================================
# ARCHIVO 63/75: catalogo_service_registry.py
# Directorio: ecommerce/servicios/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/catalogo_service_registry.py
# ==============================================================================

from __future__ import annotations
from typing import Dict, Type

from ecommerce.entidades.catalogo.categoria import Categoria
from ecommerce.entidades.catalogo.producto import Producto
from ecommerce.entidades.catalogo.vendedor import Vendedor

class CatalogoServiceRegistry:
    """Registro Singleton para los servicios del catálogo."""

    _instance: CatalogoServiceRegistry | None = None
    _categorias: Dict[str, Categoria] = {}
    _productos: Dict[str, Producto] = {}
    _vendedores: Dict[str, Vendedor] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def registrar_categoria(self, categoria: Categoria):
        self._categorias[categoria.get_id()] = categoria
        return categoria

    def obtener_categoria(self, categoria_id: str) -> Categoria | None:
        return self._categorias.get(categoria_id)

    def listar_categorias(self) -> List[Categoria]:
        return list(self._categorias.values())

    def registrar_producto(self, producto: Producto):
        self._productos[producto.get_id()] = producto
        return producto

    def obtener_producto(self, producto_id: str) -> Producto | None:
        return self._productos.get(producto_id)

    def listar_productos(self) -> List[Producto]:
        return list(self._productos.values())

    def registrar_vendedor(self, vendedor: Vendedor):
        self._vendedores[vendedor.get_id()] = vendedor
        return vendedor

    def obtener_vendedor(self, vendedor_id: str) -> Vendedor | None:
        return self._vendedores.get(vendedor_id)

    def listar_vendedores(self) -> List[Vendedor]:
        return list(self._vendedores.values())

    def to_dict(self) -> dict:
        return {
            "categorias": {cid: cat.to_dict() for cid, cat in self._categorias.items()},
            "productos": {pid: prod.to_dict() for pid, prod in self._productos.items()},
            "vendedores": {vid: vend.to_dict() for vid, vend in self._vendedores.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> CatalogoServiceRegistry:
        registry = cls()
        registry._categorias = {cid: Categoria.from_dict(cat_data) for cid, cat_data in data["categorias"].items()}
        registry._productos = {pid: Producto.from_dict(prod_data) for pid, prod_data in data["productos"].items()}
        registry._vendedores = {vid: Vendedor.from_dict(vend_data) for vid, vend_data in data["vendedores"].items()}
        return registry


# ==============================================================================
# ARCHIVO 64/75: producto_service.py
# Directorio: ecommerce/servicios/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/producto_service.py
# ==============================================================================

from __future__ import annotations
from typing import List

from ecommerce.entidades.catalogo.producto import Producto
from ecommerce.servicios.catalogo.catalogo_service_registry import CatalogoServiceRegistry
from ecommerce.excepciones.stock_insuficiente_exception import StockInsuficienteException

class ProductoService:
    """Servicio para la gestión de productos."""

    def __init__(self):
        self._registry = CatalogoServiceRegistry()

    def crear_producto(self, nombre: str, descripcion: str, precio: float, stock: int, categoria_id: str, vendedor_id: str) -> Producto:
        producto = Producto(nombre, descripcion, precio, stock, categoria_id, vendedor_id)
        self._registry.registrar_producto(producto)
        return producto

    def obtener_producto(self, producto_id: str) -> Producto | None:
        return self._registry.obtener_producto(producto_id)

    def listar_productos(self) -> List[Producto]:
        return self._registry.listar_productos()

    def actualizar_stock(self, producto_id: str, cantidad: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
        producto.set_stock(producto.get_stock() + cantidad)

    def verificar_y_reducir_stock(self, producto_id: str, cantidad: int):
        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError(f"Producto con ID {producto_id} no encontrado.")
        if producto.get_stock() < cantidad:
            raise StockInsuficienteException(producto_id, cantidad, producto.get_stock())
        producto.set_stock(producto.get_stock() - cantidad)

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> ProductoService:
        return cls()


# ==============================================================================
# ARCHIVO 65/75: vendedor_service.py
# Directorio: ecommerce/servicios/catalogo
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/catalogo/vendedor_service.py
# ==============================================================================

from __future__ import annotations
from typing import List

from ecommerce.entidades.catalogo.vendedor import Vendedor
from ecommerce.servicios.catalogo.catalogo_service_registry import CatalogoServiceRegistry

class VendedorService:
    """Servicio para la gestión de vendedores."""

    def __init__(self):
        self._registry = CatalogoServiceRegistry()

    def crear_vendedor(self, nombre: str, email: str) -> Vendedor:
        vendedor = Vendedor(nombre, email)
        self._registry.registrar_vendedor(vendedor)
        return vendedor

    def obtener_vendedor(self, vendedor_id: str) -> Vendedor | None:
        return self._registry.obtener_vendedor(vendedor_id)

    def listar_vendedores(self) -> List[Vendedor]:
        return self._registry.listar_vendedores()

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> VendedorService:
        return cls()



################################################################################
# DIRECTORIO: ecommerce/servicios/compras
################################################################################

# ==============================================================================
# ARCHIVO 66/75: __init__.py
# Directorio: ecommerce/servicios/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/__init__.py
# ==============================================================================

"""Servicios relacionados con el proceso de compra y carrito."""


# ==============================================================================
# ARCHIVO 67/75: carrito_service.py
# Directorio: ecommerce/servicios/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/carrito_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 68/75: compra_service.py
# Directorio: ecommerce/servicios/compras
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/compras/compra_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: ecommerce/servicios/membresias
################################################################################

# ==============================================================================
# ARCHIVO 69/75: __init__.py
# Directorio: ecommerce/servicios/membresias
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/membresias/__init__.py
# ==============================================================================

"""Servicios relacionados con la gestión de membresías de usuario."""


# ==============================================================================
# ARCHIVO 70/75: membresia_service.py
# Directorio: ecommerce/servicios/membresias
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/membresias/membresia_service.py
# ==============================================================================

from __future__ import annotations
from typing import Dict

from ecommerce.entidades.usuarios.usuario import Usuario
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.patrones.factory.membresia_factory import MembresiaFactory

class MembresiaService:
    """Servicio para la gestión de membresías de usuarios."""

    def __init__(self):
        pass

    def asignar_membresia(self, usuario: Usuario, tipo_membresia: str) -> Membresia:
        membresia = MembresiaFactory.crear_membresia(tipo_membresia)
        usuario.set_membresia(membresia)
        return membresia

    def to_dict(self) -> dict:
        return {}

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaService:
        return cls()



################################################################################
# DIRECTORIO: ecommerce/servicios/ordenes
################################################################################

# ==============================================================================
# ARCHIVO 71/75: __init__.py
# Directorio: ecommerce/servicios/ordenes
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/ordenes/__init__.py
# ==============================================================================

"""Servicios relacionados con la gestión de órdenes de compra."""


# ==============================================================================
# ARCHIVO 72/75: orden_service.py
# Directorio: ecommerce/servicios/ordenes
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/ordenes/orden_service.py
# ==============================================================================

from __future__ import annotations
from typing import List, Dict

from ecommerce.entidades.ordenes.orden import Orden
from ecommerce.entidades.ordenes.item_orden import ItemOrden
from ecommerce.patrones.state.estado_cancelado import EstadoCancelado
from ecommerce.patrones.state.estado_entregado import EstadoEntregado
from ecommerce.patrones.state.estado_enviado import EstadoEnviado
from ecommerce.patrones.state.estado_pendiente import EstadoPendiente
from ecommerce.patrones.state.estado_procesando import EstadoProcesando

class OrdenService:
    """Servicio para la gestión del ciclo de vida de las órdenes."""

    def __init__(self):
        self._ordenes: Dict[str, Orden] = {}

    def crear_orden(self, usuario_id: str, items: List[ItemOrden], total: float, direccion_envio: str) -> Orden:
        orden = Orden(usuario_id, items, total, direccion_envio)
        self._ordenes[orden.get_id()] = orden
        return orden

    def obtener_orden(self, orden_id: str) -> Orden | None:
        return self._ordenes.get(orden_id)

    def listar_ordenes(self) -> List[Orden]:
        return list(self._ordenes.values())

    def _reconstruir_estado(self, estado_nombre: str) -> EstadoOrden:
        if estado_nombre == "PENDIENTE":
            return EstadoPendiente()
        elif estado_nombre == "PROCESANDO":
            return EstadoProcesando()
        elif estado_nombre == "ENVIADO":
            return EstadoEnviado()
        elif estado_nombre == "ENTREGADO":
            return EstadoEntregado()
        elif estado_nombre == "CANCELADO":
            return EstadoCancelado()
        else:
            raise ValueError(f"Estado de orden desconocido: {estado_nombre}")

    def to_dict(self) -> dict:
        return {
            "ordenes": {oid: orden.to_dict() for oid, orden in self._ordenes.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> OrdenService:
        orden_service = cls()
        for oid, orden_data in data["ordenes"].items():
            orden = Orden.from_dict(orden_data)
            orden._estado = orden_service._reconstruir_estado(orden_data["estado"])
            orden_service._ordenes[oid] = orden
        return orden_service



################################################################################
# DIRECTORIO: ecommerce/servicios/usuarios
################################################################################

# ==============================================================================
# ARCHIVO 73/75: __init__.py
# Directorio: ecommerce/servicios/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/__init__.py
# ==============================================================================

"""Servicios relacionados con la gestión de usuarios y perfiles."""


# ==============================================================================
# ARCHIVO 74/75: perfil_service.py
# Directorio: ecommerce/servicios/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/perfil_service.py
# ==============================================================================

from __future__ import annotations
from typing import Dict

from ecommerce.entidades.usuarios.perfil import Perfil

class PerfilService:
    """Servicio para la gestión de perfiles de usuario."""

    def __init__(self):
        self._perfiles: Dict[str, Perfil] = {}

    def crear_perfil(self, usuario_id: str, direccion: str, telefono: str) -> Perfil:
        perfil = Perfil(usuario_id, direccion, telefono)
        self._perfiles[usuario_id] = perfil
        return perfil

    def obtener_perfil(self, usuario_id: str) -> Perfil | None:
        return self._perfiles.get(usuario_id)

    def actualizar_perfil(self, usuario_id: str, direccion: str | None = None, telefono: str | None = None) -> Perfil:
        perfil = self.obtener_perfil(usuario_id)
        if not perfil:
            raise ValueError(f"Perfil para usuario {usuario_id} no encontrado.")
        if direccion:
            perfil.set_direccion(direccion)
        if telefono:
            perfil.set_telefono(telefono)
        return perfil

    def to_dict(self) -> dict:
        return {
            "perfiles": {uid: perfil.to_dict() for uid, perfil in self._perfiles.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> PerfilService:
        perfil_service = cls()
        perfil_service._perfiles = {uid: Perfil.from_dict(perfil_data) for uid, perfil_data in data["perfiles"].items()}
        return perfil_service


# ==============================================================================
# ARCHIVO 75/75: usuario_service.py
# Directorio: ecommerce/servicios/usuarios
# Ruta completa: /home/parra1/diseno_sistemas/ecommerce/ecommerce/servicios/usuarios/usuario_service.py
# ==============================================================================

from __future__ import annotations
from typing import Dict, List

from ecommerce.entidades.usuarios.usuario import Usuario
from ecommerce.excepciones.usuario_existente_exception import UsuarioExistenteException

class UsuarioService:
    """Servicio para la gestión de usuarios."""

    def __init__(self):
        self._usuarios: Dict[str, Usuario] = {}
        self._usuarios_por_email: Dict[str, Usuario] = {}

    def registrar_usuario(self, nombre: str, email: str, password: str) -> Usuario:
        if email in self._usuarios_por_email:
            raise UsuarioExistenteException(email)
        usuario = Usuario(nombre, email, password)
        self._usuarios[usuario.get_id()] = usuario
        self._usuarios_por_email[email] = usuario
        return usuario

    def obtener_usuario_por_id(self, usuario_id: str) -> Usuario | None:
        return self._usuarios.get(usuario_id)

    def obtener_usuario_por_email(self, email: str) -> Usuario | None:
        return self._usuarios_por_email.get(email)

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios.values())

    def to_dict(self) -> dict:
        return {
            "usuarios": {uid: user.to_dict() for uid, user in self._usuarios.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> UsuarioService:
        usuario_service = cls()
        for uid, user_data in data["usuarios"].items():
            user = Usuario.from_dict(user_data)
            usuario_service._usuarios[uid] = user
            usuario_service._usuarios_por_email[user.get_email()] = user
        return usuario_service



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 75
# Generado: 2025-11-05 21:26:25
################################################################################
