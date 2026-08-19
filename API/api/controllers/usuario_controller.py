from flask import request, jsonify
from api.models.usuario_model import UsuarioModel
import jwt
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET', 'mi_clave_secreta_para_tokens_2025')

class UsuarioController:
    # ... (otros métodos: get_all, get_by_id, create, update, delete)

    # ============================================
    # NUEVOS ENDPOINTS PARA AUTENTICACIÓN
    # ============================================

    @staticmethod
    def register():
        """Registrar un nuevo usuario (público)"""
        data = request.get_json()
        
        # Validar campos requeridos
        required = ['nombre', 'email', 'password']
        for field in required:
            if field not in data:
                return jsonify({'error': f'El campo {field} es requerido'}), 400
        
        # Verificar si el usuario ya existe
        if UsuarioModel.get_by_email(data['email']):
            return jsonify({'error': 'El email ya está registrado'}), 400
        
        # Crear usuario
        result = UsuarioModel.create(data)
        
        # Generar token JWT
        token = jwt.encode({
            'id': str(result),
            'email': data['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }, JWT_SECRET, algorithm='HS256')
        
        return jsonify({
            'mensaje': 'Usuario registrado exitosamente',
            'token': token,
            'usuario': {
                'id': str(result),
                'nombre': data['nombre'],
                'email': data['email']
            }
        }), 201
    
    @staticmethod
    def login():
        """Iniciar sesión (público)"""
        data = request.get_json()
        
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email y password son requeridos'}), 400
        
        # Buscar usuario por email
        usuario = UsuarioModel.get_by_email(data['email'])
        if not usuario:
            return jsonify({'error': 'Credenciales inválidas'}), 401
        
        # Verificar contraseña
        if not UsuarioModel.verify_password(usuario, data['password']):
            return jsonify({'error': 'Credenciales inválidas'}), 401
        
        # Generar token JWT
        token = jwt.encode({
            'id': str(usuario['_id']),
            'email': usuario['email'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7)
        }, JWT_SECRET, algorithm='HS256')
        
        return jsonify({
            'mensaje': 'Login exitoso',
            'token': token,
            'usuario': {
                'id': str(usuario['_id']),
                'nombre': usuario['nombre'],
                'email': usuario['email']
            }
        }), 200