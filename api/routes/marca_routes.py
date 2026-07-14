from flask import Blueprint
from api.controllers.marca_controller import MarcaController

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/', methods=['GET'])
def get_all():
    return MarcaController.get_all()

@marca_bp.route('/<id>', methods=['GET'])
def get_by_id(id):
    return MarcaController.get_by_id(id)

@marca_bp.route('/', methods=['POST'])
def create():
    return MarcaController.create()

@marca_bp.route('/<id>', methods=['PUT'])
def update(id):
    return MarcaController.update(id)

@marca_bp.route('/<id>', methods=['DELETE'])
def delete(id):
    return MarcaController.delete(id)