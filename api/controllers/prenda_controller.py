from flask import request, jsonify
from api.models.prenda_model import PrendaModel

class PrendaController:
    @staticmethod
    def get_all():
        prendas = PrendaModel.get_all()
        for p in prendas:
            p['_id'] = str(p['_id'])
        return jsonify(prendas), 200
    
    @staticmethod
    def get_by_id(id):
        prenda = PrendaModel.get_by_id(id)
        if prenda:
            prenda['_id'] = str(prenda['_id'])
            return jsonify(prenda), 200
        return jsonify({'error': 'Prenda no encontrada'}), 404
    
    @staticmethod
    def create():
        data = request.get_json()
        required = ['nombre', 'marca', 'precio']
        if not data or any(f not in data for f in required):
            return jsonify({'error': 'Nombre, marca y precio son requeridos'}), 400
        result = PrendaModel.create(data)
        return jsonify({'mensaje': 'Prenda creada', 'id': str(result)}), 201
    
    @staticmethod
    def update(id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Datos inválidos'}), 400
        if not PrendaModel.get_by_id(id):
            return jsonify({'error': 'Prenda no encontrada'}), 404
        result = PrendaModel.update(id, data)
        return jsonify({'mensaje': 'Prenda actualizada', 'modificados': result}), 200
    
    @staticmethod
    def delete(id):
        if not PrendaModel.get_by_id(id):
            return jsonify({'error': 'Prenda no encontrada'}), 404
        result = PrendaModel.delete(id)
        return jsonify({'mensaje': 'Prenda eliminada', 'eliminados': result}), 200