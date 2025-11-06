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
