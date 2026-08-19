from flask import Blueprint
from api.controllers.usuario_controller import UsuarioController
from api.middlewares.auth_middleware import verificar_token

usuario_bp = Blueprint('usuario', __name__)

# ============================================
# RUTAS PÚBLICAS (no requieren token)
# ============================================

@usuario_bp.route('/register', methods=['POST'])
def register():
    """Registrar usuario (público)"""
    return UsuarioController.register()

@usuario_bp.route('/login', methods=['POST'])
def login():
    """Iniciar sesión (público)"""
    return UsuarioController.login()

# ============================================
# RUTAS PROTEGIDAS (requieren token)
# ============================================

@usuario_bp.route('/', methods=['GET'])
@verificar_token
def get_all():
    return UsuarioController.get_all()

@usuario_bp.route('/<id>', methods=['GET'])
@verificar_token
def get_by_id(id):
    return UsuarioController.get_by_id(id)

@usuario_bp.route('/', methods=['POST'])
@verificar_token
def create():
    return UsuarioController.create()

@usuario_bp.route('/<id>', methods=['PUT'])
@verificar_token
def update(id):
    return UsuarioController.update(id)

@usuario_bp.route('/<id>', methods=['DELETE'])
@verificar_token
def delete(id):
    return UsuarioController.delete(id)