from flask import request, jsonify
from api.models.usuario_model import UsuarioModel

class UsuarioController:
    @staticmethod
    def get_all():
        usuarios = UsuarioModel.get_all()
        for u in usuarios:
            u['_id'] = str(u['_id'])
        return jsonify(usuarios), 200
    
    @staticmethod
    def get_by_id(id):
        usuario = UsuarioModel.get_by_id(id)
        if usuario:
            usuario['_id'] = str(usuario['_id'])
            return jsonify(usuario), 200
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    @staticmethod
    def create():
        data = request.get_json()
        if not data or 'nombre' not in data or 'email' not in data:
            return jsonify({'error': 'Nombre y email son requeridos'}), 400
        result = UsuarioModel.create(data)
        return jsonify({'mensaje': 'Usuario creado', 'id': str(result)}), 201
    
    @staticmethod
    def update(id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Datos inválidos'}), 400
        if not UsuarioModel.get_by_id(id):
            return jsonify({'error': 'Usuario no encontrado'}), 404
        result = UsuarioModel.update(id, data)
        return jsonify({'mensaje': 'Usuario actualizado', 'modificados': result}), 200
    
    @staticmethod
    def delete(id):
        if not UsuarioModel.get_by_id(id):
            return jsonify({'error': 'Usuario no encontrado'}), 404
        result = UsuarioModel.delete(id)
        return jsonify({'mensaje': 'Usuario eliminado', 'eliminados': result}), 200