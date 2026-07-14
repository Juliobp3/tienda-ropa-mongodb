from flask import Blueprint
from api.controllers.venta_controller import VentaController

venta_bp = Blueprint('venta', __name__)

@venta_bp.route('/', methods=['GET'])
def get_all():
    return VentaController.get_all()

@venta_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    return VentaController.get_by_id(id)

@venta_bp.route('/', methods=['POST'])
def create():
    return VentaController.create()

@venta_bp.route('/<id>', methods=['PUT'])
def update(id):
    return VentaController.update(id)

@venta_bp.route('/<id>', methods=['DELETE'])
def delete(id):
    return VentaController.delete(id)