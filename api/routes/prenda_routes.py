from flask import Blueprint
from api.controllers.prenda_controller import PrendaController

prenda_bp = Blueprint('prenda', __name__)

@prenda_bp.route('/', methods=['GET'])
def get_all():
    return PrendaController.get_all()

@prenda_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    return PrendaController.get_by_id(id)

@prenda_bp.route('/', methods=['POST'])
def create():
    return PrendaController.create()

@prenda_bp.route('/<id>', methods=['PUT'])
def update(id):
    return PrendaController.update(id)

@prenda_bp.route('/<id>', methods=['DELETE'])
def delete(id):
    return PrendaController.delete(id)