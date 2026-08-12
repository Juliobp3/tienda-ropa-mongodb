from flask import Blueprint
from api.controllers.prenda_controller import PrendaController
from api.middlewares.auth_middleware import verificar_token

prenda_bp = Blueprint('prenda', __name__)

@prenda_bp.route('/', methods=['GET'])
@verificar_token
def get_all():
    return PrendaController.get_all()

@prenda_bp.route('/<id>', methods=['GET'])
@verificar_token
def get_by_id(id):
    return PrendaController.get_by_id(id)

@prenda_bp.route('/', methods=['POST'])
@verificar_token
def create():
    return PrendaController.create()

@prenda_bp.route('/<id>', methods=['PUT'])
@verificar_token
def update(id):
    return PrendaController.update(id)

@prenda_bp.route('/<id>', methods=['DELETE'])
@verificar_token
def delete(id):
    return PrendaController.delete(id)