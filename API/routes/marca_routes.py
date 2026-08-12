from flask import Blueprint
from api.controllers.marca_controller import MarcaController
from api.middlewares.auth_middleware import verificar_token

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/', methods=['GET'])
@verificar_token
def get_all():
    return MarcaController.get_all()

@marca_bp.route('/<id>', methods=['GET'])
@verificar_token
def get_by_id(id):
    return MarcaController.get_by_id(id)

@marca_bp.route('/', methods=['POST'])
@verificar_token
def create():
    return MarcaController.create()

@marca_bp.route('/<id>', methods=['PUT'])
@verificar_token
def update(id):
    return MarcaController.update(id)

@marca_bp.route('/<id>', methods=['DELETE'])
@verificar_token
def delete(id):
    return MarcaController.delete(id)