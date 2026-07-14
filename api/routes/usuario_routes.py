from flask import Blueprint
from api.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/', methods=['GET'])
def get_all():
    return UsuarioController.get_all()

@usuario_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    return UsuarioController.get_by_id(id)

@usuario_bp.route('/', methods=['POST'])
def create():
    return UsuarioController.create()

@usuario_bp.route('/<id>', methods=['PUT'])
def update(id):
    return UsuarioController.update(id)

@usuario_bp.route('/<id>', methods=['DELETE'])
def delete(id):
    return UsuarioController.delete(id)