from flask import request, jsonify
from api.models.venta_model import VentaModel

class VentaController:
    @staticmethod
    def get_all():
        ventas = VentaModel.get_all()
        for v in ventas:
            v['_id'] = str(v['_id'])
        return jsonify(ventas), 200
    
    @staticmethod
    def get_by_id(id):
        venta = VentaModel.get_by_id(id)
        if venta:
            venta['_id'] = str(venta['_id'])
            return jsonify(venta), 200
        return jsonify({'error': 'Venta no encontrada'}), 404
    
    @staticmethod
    def create():
        data = request.get_json()
        required = ['fecha', 'prenda', 'cantidad', 'precioUnitario', 'usuario']
        if not data or any(f not in data for f in required):
            return jsonify({'error': 'Todos los campos son requeridos'}), 400
        result = VentaModel.create(data)
        return jsonify({'mensaje': 'Venta creada', 'id': str(result)}), 201
    
    @staticmethod
    def update(id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Datos inválidos'}), 400
        if not VentaModel.get_by_id(id):
            return jsonify({'error': 'Venta no encontrada'}), 404
        result = VentaModel.update(id, data)
        return jsonify({'mensaje': 'Venta actualizada', 'modificados': result}), 200
    
    @staticmethod
    def delete(id):
        if not VentaModel.get_by_id(id):
            return jsonify({'error': 'Venta no encontrada'}), 404
        result = VentaModel.delete(id)
        return jsonify({'mensaje': 'Venta eliminada', 'eliminados': result}), 200