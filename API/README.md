# API de Tienda de Ropa
API desarrollada en Python con Flask y MongoDB

## Documentación de la API

### Base URL


### Ejemplo de uso en Postman

**Obtener todas las marcas:**



### Base URL

http://localhost:5000/api


### Endpoints de Usuarios

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/usuarios` | Obtener todos los usuarios |
| GET | `/usuarios/{id}` | Obtener usuario por ID |
| POST | `/usuarios` | Crear un nuevo usuario |
| PUT | `/usuarios/{id}` | Actualizar un usuario |
| DELETE | `/usuarios/{id}` | Eliminar un usuario |

### Endpoints de Marcas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/marcas` | Obtener todas las marcas |
| GET | `/marcas/{id}` | Obtener marca por ID |
| POST | `/marcas` | Crear una nueva marca |
| PUT | `/marcas/{id}` | Actualizar una marca |
| DELETE | `/marcas/{id}` | Eliminar una marca |

### Endpoints de Prendas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/prendas` | Obtener todas las prendas |
| GET | `/prendas/{id}` | Obtener prenda por ID |
| POST | `/prendas` | Crear una nueva prenda |
| PUT | `/prendas/{id}` | Actualizar una prenda |
| DELETE | `/prendas/{id}` | Eliminar una prenda |

### Endpoints de Ventas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/ventas` | Obtener todas las ventas |
| GET | `/ventas/{id}` | Obtener venta por ID |
| POST | `/ventas` | Crear una nueva venta |
| PUT | `/ventas/{id}` | Actualizar una venta |
| DELETE | `/ventas/{id}` | Eliminar una venta |

### Endpoints de Reportes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/reportes/marcas-con-ventas` | Listar marcas con al menos una venta |
| GET | `/reportes/stock-restante` | Mostrar stock restante por prenda |
| GET | `/reportes/top-marcas` | Listar las 5 marcas más vendidas |

GET http://localhost:5000/api/marcas


**Crear una nueva marca:**

POST http://localhost:5000/api/marcas
Content-Type: application/json

{
"nombre": "New Balance",
"pais": "USA",
"anioFundacion": 1906
}


**Obtener top 5 marcas:**

GET http://localhost:5000/api/reportes/top-marcas

