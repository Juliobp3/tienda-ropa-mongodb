from flask import Blueprint
from api.controllers.venta_controller import VentaController
from api.middlewares.auth_middleware import verificar_token

venta_bp = Blueprint('venta', __name__)

@venta_bp.route('/', methods=['GET'])
@verificar_token
def get_all():
    return VentaController.get_all()

@venta_bp.route('/<id>', methods=['GET'])
@verificar_token
def get_by_id(id):
    return VentaController.get_by_id(id)

@venta_bp.route('/', methods=['POST'])
@verificar_token
def create():
    return VentaController.create()

@venta_bp.route('/<id>', methods=['PUT'])
@verificar_token
def update(id):
    return VentaController.update(id)

@venta_bp.route('/<id>', methods=['DELETE'])
@verificar_token
def delete(id):
    return VentaController.delete(id)