// =====================================================
// PROYECTO: Tienda de Ropa - Base de Datos MongoDB
// AUTOR: Julio Brumley Pérez
// FECHA: Marzo 2025
// =====================================================

/**
 * Este archivo documenta las operaciones realizadas en MongoDB Compass
 * para el proyecto de tienda de ropa.
 * 
 * BASE DE DATOS: tienda_ropa
 * 
 * COLECCIONES:
 * - usuarios (3 documentos)
 * - marcas (5 documentos)
 * - prendas (7 documentos)
 * - ventas (7 documentos)
 */

// =====================================================
// 1. OPERACIONES DE INSERCIÓN
// =====================================================

// INSERTAR UN SOLO DOCUMENTO en usuarios
db.usuarios.insertOne({
  "nombre": "Ana García",
  "email": "ana.garcia@email.com",
  "telefono": "8888-1234",
  "direccion": "San José, Costa Rica",
  "fechaRegistro": "2025-03-20"
})

// INSERTAR VARIOS DOCUMENTOS en usuarios
db.usuarios.insertMany([
  {
    "nombre": "Carlos López",
    "email": "carlos@email.com",
    "telefono": "8888-5678",
    "direccion": "Alajuela, Costa Rica",
    "fechaRegistro": "2025-03-20"
  },
  {
    "nombre": "María Rodríguez",
    "email": "maria@email.com",
    "telefono": "8888-9012",
    "direccion": "Cartago, Costa Rica",
    "fechaRegistro": "2025-03-20"
  }
])

// INSERTAR MARCAS
db.marcas.insertMany([
  { "nombre": "Nike", "pais": "USA", "anioFundacion": 1964 },
  { "nombre": "Adidas", "pais": "Alemania", "anioFundacion": 1949 },
  { "nombre": "Zara", "pais": "España", "anioFundacion": 1975 },
  { "nombre": "Levi's", "pais": "USA", "anioFundacion": 1853 },
  { "nombre": "Puma", "pais": "Alemania", "anioFundacion": 1948 }
])

// INSERTAR PRENDAS
db.prendas.insertMany([
  { "nombre": "Camiseta Deportiva", "marca": "Nike", "precio": 25000, "stock": 50, "talla": "M", "color": "Rojo" },
  { "nombre": "Pantalón Deportivo", "marca": "Nike", "precio": 45000, "stock": 30, "talla": "L", "color": "Negro" },
  { "nombre": "Zapatillas Running", "marca": "Adidas", "precio": 65000, "stock": 20, "talla": "42", "color": "Blanco" },
  { "nombre": "Chaqueta Casual", "marca": "Zara", "precio": 55000, "stock": 15, "talla": "S", "color": "Gris" },
  { "nombre": "Jeans Clásicos", "marca": "Levi's", "precio": 35000, "stock": 40, "talla": "32", "color": "Azul" },
  { "nombre": "Camisa Formal", "marca": "Zara", "precio": 30000, "stock": 25, "talla": "M", "color": "Blanco" },
  { "nombre": "Gorra Deportiva", "marca": "Puma", "precio": 15000, "stock": 100, "talla": "Única", "color": "Negro" }
])

// INSERTAR VENTAS
db.ventas.insertMany([
  { "fecha": "2025-03-15", "prenda": "Camiseta Deportiva", "cantidad": 2, "precioUnitario": 25000, "usuario": "Ana García" },
  { "fecha": "2025-03-16", "prenda": "Zapatillas Running", "cantidad": 1, "precioUnitario": 65000, "usuario": "Ana García" },
  { "fecha": "2025-03-16", "prenda": "Jeans Clásicos", "cantidad": 3, "precioUnitario": 35000, "usuario": "Carlos López" },
  { "fecha": "2025-03-17", "prenda": "Gorra Deportiva", "cantidad": 5, "precioUnitario": 15000, "usuario": "María Rodríguez" },
  { "fecha": "2025-03-17", "prenda": "Camiseta Deportiva", "cantidad": 1, "precioUnitario": 25000, "usuario": "Carlos López" },
  { "fecha": "2025-03-18", "prenda": "Zapatillas Running", "cantidad": 2, "precioUnitario": 65000, "usuario": "Ana García" },
  { "fecha": "2025-03-18", "prenda": "Jeans Clásicos", "cantidad": 1, "precioUnitario": 35000, "usuario": "María Rodríguez" }
])

// =====================================================
// 2. OPERACIONES DE ACTUALIZACIÓN
// =====================================================

// Actualizar precio de Zapatillas Running
db.prendas.updateOne(
  { "nombre": "Zapatillas Running" },
  { "$set": { "precio": 70000 } }
)

// =====================================================
// 3. OPERACIONES DE ELIMINACIÓN
// =====================================================

// Eliminar una venta específica
db.ventas.deleteOne(
  { "prenda": "Jeans Clásicos", "cantidad": 1 }
)

// =====================================================
// 4. CONSULTAS OBLIGATORIAS
// =====================================================

// CONSULTA 1: Obtener la cantidad vendida de prendas por fecha específica
// ¿Qué hace? Cuenta el total de prendas vendidas en una fecha específica (2025-03-17)
db.ventas.aggregate([
  { "$match": { "fecha": "2025-03-17" } },
  { "$group": { "_id": "$fecha", "totalVendido": { "$sum": "$cantidad" } } }
])

// CONSULTA 2: Obtener lista de todas las marcas que tienen al menos una venta
// ¿Qué hace? Une ventas con prendas y agrupa por marca para listar solo las que se han vendido
db.ventas.aggregate([
  { "$lookup": { "from": "prendas", "localField": "prenda", "foreignField": "nombre", "as": "detallePrenda" } },
  { "$unwind": "$detallePrenda" },
  { "$group": { "_id": "$detallePrenda.marca" } }
])

// CONSULTA 3: Obtener prendas vendidas y su cantidad restante en stock
// ¿Qué hace? Calcula cuántas unidades de cada prenda se han vendido y cuántas quedan en inventario
db.ventas.aggregate([
  { "$group": { "_id": "$prenda", "totalVendido": { "$sum": "$cantidad" } } },
  { "$lookup": { "from": "prendas", "localField": "_id", "foreignField": "nombre", "as": "prendaInfo" } },
  { "$unwind": "$prendaInfo" },
  { "$project": { "nombre": "$_id", "vendido": "$totalVendido", "stockOriginal": "$prendaInfo.stock", "stockRestante": { "$subtract": ["$prendaInfo.stock", "$totalVendido"] } } }
])

// CONSULTA 4: Obtener listado de las 5 marcas más vendidas y su cantidad de ventas
// ¿Qué hace? Identifica las 5 marcas con mayor número de unidades vendidas
db.ventas.aggregate([
  { "$lookup": { "from": "prendas", "localField": "prenda", "foreignField": "nombre", "as": "prendaInfo" } },
  { "$unwind": "$prendaInfo" },
  { "$group": { "_id": "$prendaInfo.marca", "totalVentas": { "$sum": "$cantidad" } } },
  { "$sort": { "totalVentas": -1 } },
  { "$limit": 5 }
])
