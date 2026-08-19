# 🛍️ Tienda de Ropa - Proyecto Final

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo para una **tienda de ropa** que incluye:

- **Base de datos NoSQL** en MongoDB Atlas
- **API REST** en Python con Flask
- **Front-end** con HTML, CSS y JavaScript (AJAX)

La base de datos gestiona:
- 👤 **Usuarios** - Clientes de la tienda
- 🏷️ **Marcas** - Fabricantes de prendas
- 👕 **Prendas** - Productos disponibles
- 💰 **Ventas** - Registro de transacciones

## 📁 Estructura del Repositorio

tienda-ropa-mongodb/
API/ # API en Python con Flask
front-end/ # Interfaz de usuario
scripts/ # Scripts de base de datos
database/ # Operaciones de base de datos
README.md # Documentación principal


## Estructura de la Base de Datos

**Base de datos:** `tienda_ropa`

### Colección: `usuarios`

[
  {
    "nombre": "Ana García",
    "email": "ana.garcia@email.com",
    "telefono": "8888-1234",
    "direccion": "San José, Costa Rica",
    "fechaRegistro": "2025-03-20"
  },
  {
    "nombre": "Carlos López",
    "email": "carlos@email.com",
    "telefono": "8888-5678",
    "direccion": "Alajuela, Costa Rica"
  },
  {
    "nombre": "María Rodríguez",
    "email": "maria@email.com",
    "telefono": "8888-9012",
    "direccion": "Cartago, Costa Rica"
  }
]

marcas

[
  {
    "nombre": "Nike",
    "pais": "USA",
    "anioFundacion": 1964
  },
  {
    "nombre": "Adidas",
    "pais": "Alemania",
    "anioFundacion": 1949
  },
  {
    "nombre": "Zara",
    "pais": "España",
    "anioFundacion": 1975
  },
  {
    "nombre": "Levi's",
    "pais": "USA",
    "anioFundacion": 1853
  },
  {
    "nombre": "Puma",
    "pais": "Alemania",
    "anioFundacion": 1948
  }
]

prendas

[
  {
    "nombre": "Camiseta Deportiva",
    "marca": "Nike",
    "precio": 25000,
    "stock": 50,
    "talla": "M",
    "color": "Rojo"
  },
  {
    "nombre": "Pantalón Deportivo",
    "marca": "Nike",
    "precio": 45000,
    "stock": 30,
    "talla": "L",
    "color": "Negro"
  },
  {
    "nombre": "Zapatillas Running",
    "marca": "Adidas",
    "precio": 70000,
    "stock": 20,
    "talla": "42",
    "color": "Blanco"
  },
  {
    "nombre": "Chaqueta Casual",
    "marca": "Zara",
    "precio": 55000,
    "stock": 15,
    "talla": "S",
    "color": "Gris"
  },
  {
    "nombre": "Jeans Clásicos",
    "marca": "Levi's",
    "precio": 35000,
    "stock": 40,
    "talla": "32",
    "color": "Azul"
  },
  {
    "nombre": "Camisa Formal",
    "marca": "Zara",
    "precio": 30000,
    "stock": 25,
    "talla": "M",
    "color": "Blanco"
  },
  {
    "nombre": "Gorra Deportiva",
    "marca": "Puma",
    "precio": 15000,
    "stock": 100,
    "talla": "Única",
    "color": "Negro"
  }
]

ventas

[
  {
    "fecha": "2025-03-15",
    "prenda": "Camiseta Deportiva",
    "cantidad": 2,
    "precioUnitario": 25000,
    "usuario": "Ana García"
  },
  {
    "fecha": "2025-03-16",
    "prenda": "Zapatillas Running",
    "cantidad": 1,
    "precioUnitario": 65000,
    "usuario": "Ana García"
  },
  {
    "fecha": "2025-03-16",
    "prenda": "Jeans Clásicos",
    "cantidad": 3,
    "precioUnitario": 35000,
    "usuario": "Carlos López"
  },
  {
    "fecha": "2025-03-17",
    "prenda": "Gorra Deportiva",
    "cantidad": 5,
    "precioUnitario": 15000,
    "usuario": "María Rodríguez"
  },
  {
    "fecha": "2025-03-17",
    "prenda": "Camiseta Deportiva",
    "cantidad": 1,
    "precioUnitario": 25000,
    "usuario": "Carlos López"
  },
  {
    "fecha": "2025-03-18",
    "prenda": "Zapatillas Running",
    "cantidad": 2,
    "precioUnitario": 65000,
    "usuario": "Ana García"
  },
  {
    "fecha": "2025-03-18",
    "prenda": "Jeans Clásicos",
    "cantidad": 1,
    "precioUnitario": 35000,
    "usuario": "María Rodríguez"
  }
]

API
Tecnologías
Python 3.x

Flask - Framework web

PyMongo - Conector MongoDB

JWT - Autenticación

Instalación y Ejecución
Clonar el repositorio

Navegar a la carpeta API/

Crear entorno virtual:

python -m venv venv
venv\Scripts\activate     # Windows
# o
source venv/bin/activate  # Linux/Mac

Instalar dependencias:

pip install -r requirements.txt

Crear archivo .env:

MONGO_URI=mongodb+srv://<usuario>:<contraseña>@...
DB_NAME=tienda_ropa
JWT_SECRET=tu_clave_secreta
PORT=5000

Ejecutar la API:

python run.py

Documentación Interactiva
La API incluye documentación Swagger disponible en:

http://localhost:5000/apidocs

Front-end
Tecnologías
HTML5

CSS3

JavaScript (Vanilla JS con AJAX)

Páginas
Página	Descripción
index.html: Página principal con menú y autenticación
login.html: Inicio de sesión para obtener token
prendas.html: CRUD completo de prendas
reportes.html: Visualización de 3 reportes

Funcionalidades
Autenticación

Login con email y contraseña

Almacenamiento del token en localStorage

Cierre de sesión

Gestión de Prendas

Listar todas las prendas

Crear nueva prenda (modal)

Editar prenda existente (modal)

Eliminar prenda (confirmación)

Reportes

Marcas que tienen al menos una venta

Prendas vendidas y stock restante

Top 5 marcas más vendidas

Cómo usar el Front-end
Abrir index.html en el navegador

Ir a "Iniciar Sesión"

Ingresar credenciales de prueba:

Email: juliobp3@email.com

Password: juliobp3

Explorar las funciones del menú

Requisitos para el Front-end
La API debe estar corriendo en http://127.0.0.1:5000

El token se guarda automáticamente en el navegador

Todas las peticiones usan AJAX con fetch()
