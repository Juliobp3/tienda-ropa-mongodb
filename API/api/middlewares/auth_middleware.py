from flask import request, jsonify
import jwt
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET', 'mi_clave_secreta_para_tokens_2025')

def verificar_token(f):
    """Decorador para proteger rutas con JWT"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        # 1. Obtener el token del header Authorization
        auth_header = request.headers.get('Authorization')
        
        # 2. Verificar que el token existe y tiene el formato correcto
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({
                'error': 'Acceso denegado. Token no proporcionado'
            }), 401
        
        # 3. Extraer el token (quitar "Bearer ")
        token = auth_header.split(' ')[1]
        
        try:
            # 4. Verificar el token con la clave secreta
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            request.usuario = payload  # Guardar info del usuario
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401
        
        # 5. Si todo está bien, continuar con la función
        return f(*args, **kwargs)
    
    return wrapper