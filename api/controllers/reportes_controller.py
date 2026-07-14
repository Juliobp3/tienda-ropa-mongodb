from flask import jsonify
from api.config.db import db

class ReportesController:
    @staticmethod
    def marcas_con_ventas():
        """Reporte 1: Marcas que tienen al menos una venta"""
        try:
            pipeline = [
                {"$lookup": {"from": "prendas", "localField": "prenda", "foreignField": "nombre", "as": "detallePrenda"}},
                {"$unwind": "$detallePrenda"},
                {"$group": {"_id": "$detallePrenda.marca"}}
            ]
            resultado = list(db.ventas.aggregate(pipeline))
            return jsonify({'success': True, 'data': resultado}), 200
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
    
    @staticmethod
    def stock_restante():
        """Reporte 2: Prendas vendidas y stock restante"""
        try:
            pipeline = [
                {"$group": {"_id": "$prenda", "totalVendido": {"$sum": "$cantidad"}}},
                {"$lookup": {"from": "prendas", "localField": "_id", "foreignField": "nombre", "as": "prendaInfo"}},
                {"$unwind": "$prendaInfo"},
                {"$project": {
                    "nombre": "$_id",
                    "vendido": "$totalVendido",
                    "stockOriginal": "$prendaInfo.stock",
                    "stockRestante": {"$subtract": ["$prendaInfo.stock", "$totalVendido"]}
                }}
            ]
            resultado = list(db.ventas.aggregate(pipeline))
            return jsonify({'success': True, 'data': resultado}), 200
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500
    
    @staticmethod
    def top_marcas():
        """Reporte 3: Top 5 marcas más vendidas"""
        try:
            pipeline = [
                {"$lookup": {"from": "prendas", "localField": "prenda", "foreignField": "nombre", "as": "prendaInfo"}},
                {"$unwind": "$prendaInfo"},
                {"$group": {"_id": "$prendaInfo.marca", "totalVentas": {"$sum": "$cantidad"}}},
                {"$sort": {"totalVentas": -1}},
                {"$limit": 5}
            ]
            resultado = list(db.ventas.aggregate(pipeline))
            return jsonify({'success': True, 'data': resultado}), 200
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500