
// SCRIPT: Crear colecciones de la tienda de ropa


// Conectar a la base de datos
use tienda_ropa;

// Crear colecciones
db.createCollection("usuarios");
db.createCollection("marcas");
db.createCollection("prendas");
db.createCollection("ventas");

print("Colecciones creadas exitosamente");