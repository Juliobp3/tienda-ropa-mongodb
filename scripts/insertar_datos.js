// SCRIPT: Insertar datos de ejemplo

use tienda_ropa;

// Insertar usuarios
db.usuarios.insertMany([
    {
        nombre: "Ana García",
        email: "ana.garcia@email.com",
        telefono: "8888-1234",
        direccion: "San José, Costa Rica",
        fechaRegistro: "2025-03-20"
    },
    {
        nombre: "Carlos López",
        email: "carlos@email.com",
        telefono: "8888-5678",
        direccion: "Alajuela, Costa Rica"
    },
    {
        nombre: "María Rodríguez",
        email: "maria@email.com",
        telefono: "8888-9012",
        direccion: "Cartago, Costa Rica"
    }
]);

// Insertar marcas
db.marcas.insertMany([
    { nombre: "Nike", pais: "USA", anioFundacion: 1964 },
    { nombre: "Adidas", pais: "Alemania", anioFundacion: 1949 },
    { nombre: "Zara", pais: "España", anioFundacion: 1975 },
    { nombre: "Levi's", pais: "USA", anioFundacion: 1853 },
    { nombre: "Puma", pais: "Alemania", anioFundacion: 1948 }
]);

// Insertar prendas
db.prendas.insertMany([
    { nombre: "Camiseta Deportiva", marca: "Nike", precio: 25000, stock: 50, talla: "M", color: "Rojo" },
    { nombre: "Pantalón Deportivo", marca: "Nike", precio: 45000, stock: 30, talla: "L", color: "Negro" },
    { nombre: "Zapatillas Running", marca: "Adidas", precio: 70000, stock: 20, talla: "42", color: "Blanco" },
    { nombre: "Chaqueta Casual", marca: "Zara", precio: 55000, stock: 15, talla: "S", color: "Gris" },
    { nombre: "Jeans Clásicos", marca: "Levi's", precio: 35000, stock: 40, talla: "32", color: "Azul" },
    { nombre: "Camisa Formal", marca: "Zara", precio: 30000, stock: 25, talla: "M", color: "Blanco" },
    { nombre: "Gorra Deportiva", marca: "Puma", precio: 15000, stock: 100, talla: "Única", color: "Negro" }
]);

// Insertar ventas
db.ventas.insertMany([
    { fecha: "2025-03-15", prenda: "Camiseta Deportiva", cantidad: 2, precioUnitario: 25000, usuario: "Ana García" },
    { fecha: "2025-03-16", prenda: "Zapatillas Running", cantidad: 1, precioUnitario: 65000, usuario: "Ana García" },
    { fecha: "2025-03-16", prenda: "Jeans Clásicos", cantidad: 3, precioUnitario: 35000, usuario: "Carlos López" },
    { fecha: "2025-03-17", prenda: "Gorra Deportiva", cantidad: 5, precioUnitario: 15000, usuario: "María Rodríguez" },
    { fecha: "2025-03-17", prenda: "Camiseta Deportiva", cantidad: 1, precioUnitario: 25000, usuario: "Carlos López" },
    { fecha: "2025-03-18", prenda: "Zapatillas Running", cantidad: 2, precioUnitario: 65000, usuario: "Ana García" },
    { fecha: "2025-03-18", prenda: "Jeans Clásicos", cantidad: 1, precioUnitario: 35000, usuario: "María Rodríguez" }
]);

print("Datos insertados exitosamente");