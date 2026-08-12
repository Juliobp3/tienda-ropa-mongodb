// SCRIPT: Consultas de la tienda de ropa

use tienda_ropa;

// CONSULTA 1: Cantidad vendida por fecha específica
print("CONSULTA 1: Ventas por fecha (2025-03-17)");
db.ventas.aggregate([
    { $match: { fecha: "2025-03-17" } },
    { $group: { _id: "$fecha", totalVendido: { $sum: "$cantidad" } } }
]);

// CONSULTA 2: Marcas que tienen al menos una venta
print("CONSULTA 2: Marcas con ventas");
db.ventas.aggregate([
    { $lookup: { from: "prendas", localField: "prenda", foreignField: "nombre", as: "detallePrenda" } },
    { $unwind: "$detallePrenda" },
    { $group: { _id: "$detallePrenda.marca" } }
]);

// CONSULTA 3: Prendas vendidas y stock restante
print("CONSULTA 3: Stock restante por prenda");
db.ventas.aggregate([
    { $group: { _id: "$prenda", totalVendido: { $sum: "$cantidad" } } },
    { $lookup: { from: "prendas", localField: "_id", foreignField: "nombre", as: "prendaInfo" } },
    { $unwind: "$prendaInfo" },
    { $project: {
        nombre: "$_id",
        vendido: "$totalVendido",
        stockOriginal: "$prendaInfo.stock",
        stockRestante: { $subtract: ["$prendaInfo.stock", "$totalVendido"] }
    } }
]);

// CONSULTA 4: Top 5 marcas más vendidas
print("CONSULTA 4: Top 5 marcas más vendidas");
db.ventas.aggregate([
    { $lookup: { from: "prendas", localField: "prenda", foreignField: "nombre", as: "prendaInfo" } },
    { $unwind: "$prendaInfo" },
    { $group: { _id: "$prendaInfo.marca", totalVentas: { $sum: "$cantidad" } } },
    { $sort: { totalVentas: -1 } },
    { $limit: 5 }
]);

print("Consultas ejecutadas exitosamente");