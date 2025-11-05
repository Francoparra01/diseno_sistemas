# Sistema de E-Commerce — Proyecto de Diseño de Sistemas
Versión: 1.0.0  
Autor: Franco Parra  
Año: 2025  

---

## Objetivo General

El sistema simula el funcionamiento de una plataforma de comercio electrónico, permitiendo la gestión de usuarios, membresías, catálogo de productos, carritos de compra, procesamiento de órdenes y notificaciones automáticas.  
El enfoque principal es la correcta aplicación de **principios de diseño orientado a objetos** y **patrones de diseño**.

---

## Arquitectura General

El proyecto está dividido en capas lógicas:

| Capa | Responsabilidad |
|------|----------------|
| **Entidades (Modelos / DTOs)** | Representan datos sin lógica compleja. |
| **Servicios (Business Logic)** | Ejecutan reglas de negocio y validaciones. |
| **Patrones** | Encapsulan comportamientos variantes (Strategy, State, Factory, Observer). |
| **Persistencia** | Almacenamiento simple en archivos `.dat` dentro de `data/`. |

---

## Estructura del Proyecto

ecommerce/
│
├── main.py # Demostración integrada del sistema
├── README.md
├── data/ # Datos persistidos
│
└── ecommerce/
├── constantes.py # Valores globales del sistema
│
├── entidades/
│ ├── usuarios/ # Usuario + Membresías
│ ├── catalogo/ # Producto, Categoría, Vendedor
│ ├── compras/ # Carrito, Items, Pago
│ └── ordenes/ # Orden de Compra + Items
│
├── servicios/
│ ├── usuarios/ # Manejo de usuarios y perfiles
│ ├── catalogo/ # Registro y consulta de productos
│ ├── compras/ # Carrito y compras
│ ├── ordenes/ # Ciclo de vida de las órdenes
│ ├── membresias/ # Políticas de membresía
│ └── precio_service.py # Cálculo total con descuento + envío
│
├── patrones/
│ ├── factory/ # MembresiaFactory
│ ├── strategy/ # Descuentos y métodos de envío
│ ├── state/ # Estados de una orden
│ └── observer/ # Notificaciones automáticas
│
└── excepciones/ # Manejo de errores del dominio


---

## Patrones de Diseño Aplicados

| Patrón | Ubicación | Propósito |
|-------|-----------|-----------|
| Factory Method | `patrones/factory/membresia_factory.py` | Crear membresías sin acoplar al tipo concreto |
| Strategy | `patrones/strategy/*` | Cambiar cálculo de descuentos y envíos según membresía |
| State | `patrones/state/*` | Controlar el ciclo de vida de la orden |
| Observer | `patrones/observer/*` | Notificar acciones importantes (email, inventario, analytics) |
| Singleton/Registry | `servicios/catalogo/catalogo_service_registry.py` | Acceso centralizado a servicios |

---

## Historias de Usuario

### Epic 1: Gestión de Usuarios y Membresías

**US-001 — Registrar Usuario**  
Como nuevo cliente  
Quiero crear una cuenta  
Para poder comprar productos.

**Criterios**
- Email único.
- Se asigna una membresía base mediante Factory.
- Si existe email duplicado → `UsuarioExistenteException`.

---

**US-002 — Actualizar Membresía del Usuario**  
Como usuario  
Quiero mejorar mi plan  
Para obtener mejores beneficios.

Roles de membresía:

| Tipo | Descuento | Envío |
|------|-----------|-------|
| Basic | 0% | estándar |
| Prime | 10% | envío prioritario |
| Premium | 20% | envío gratuito |

---

### Epic 2: Gestión de Catálogo

**US-003 — Registrar Productos**  
Como vendedor  
Quiero publicar productos  
Para que los usuarios puedan comprarlos.

---

### Epic 3: Carrito y Compra

**US-004 — Agregar productos al carrito**  
- Cada item incrementa cantidad.
- No puede haber cantidades negativas.

**US-005 — Confirmar compra**  
- Se verifica stock.
- Se aplica Strategy de descuento y envío.
- Se genera **Orden**.

---

### Epic 4: Ciclo de Vida de la Orden (Patrón State)

Estados válidos:

Pendiente → Procesando → Enviado → Entregado
↘ Cancelado




Transiciones inválidas → `OperacionNoPermitidaException`.

---

### Epic 5: Notificaciones (Observer)

Al confirmar compra:
- Se envía email al usuario.
- Se registra evento en Analytics.
- Se descuenta stock en Inventario.

---

## Cómo Ejecutar

```bash
python3 main.py


Persistencia

Los datos se guardan en la carpeta data/ automáticamente al finalizar el flujo de compra.

Limitaciones / Futuras Mejoras

Persistencia local simple (no BD).

Sin interfaz gráfica.

No implementa concurrencia real.

Mejoras posibles:

Migración a SQLite o PostgreSQL.

API REST con FastAPI.

Frontend (React / Vue).

Autor

Franco Parra — Universidad de Mendoza
Diseño de Sistemas — 2025
