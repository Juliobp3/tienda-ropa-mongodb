from flask import request, jsonify
from api.models.marca_model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        marcas = MarcaModel.get_all()
        for m in marcas:
            m['_id'] = str(m['_id'])
        return jsonify(marcas), 200
    
    @staticmethod
    def get_by_id(id):
        marca = MarcaModel.get_by_id(id)
        if marca:
            marca['_id'] = str(marca['_id'])
            return jsonify(marca), 200
        return jsonify({'error': 'Marca no encontrada'}), 404
    
    @staticmethod
    def create():
        data = request.get_json()
        if not data or 'nombre' not in data:
            return jsonify({'error': 'El campo nombre es requerido'}), 400
        if MarcaModel.get_by_nombre(data['nombre']):
            return jsonify({'error': 'La marca ya existe'}), 400
        result = MarcaModel.create(data)
        return jsonify({'mensaje': 'Marca creada', 'id': str(result)}), 201
    
    @staticmethod
    def update(id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Datos inválidos'}), 400
        if not MarcaModel.get_by_id(id):
            return jsonify({'error': 'Marca no encontrada'}), 404
        result = MarcaModel.update(id, data)
        return jsonify({'mensaje': 'Marca actualizada', 'modificados': result}), 200
    
    @staticmethod
    def delete(id):
        if not MarcaModel.get_by_id(id):
            return jsonify({'error': 'Marca no encontrada'}), 404
        result = MarcaModel.delete(id)
        return jsonify({'mensaje': 'Marca eliminada', 'eliminados': result}), 200