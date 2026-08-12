from flask import Blueprint
from api.controllers.reportes_controller import ReportesController
from api.middlewares.auth_middleware import verificar_token

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/marcas-con-ventas', methods=['GET'])
@verificar_token
def marcas_con_ventas():
    return ReportesController.marcas_con_ventas()

@reportes_bp.route('/stock-restante', methods=['GET'])
@verificar_token
def stock_restante():
    return ReportesController.stock_restante()

@reportes_bp.route('/top-marcas', methods=['GET'])
@verificar_token
def top_marcas():
    return ReportesController.top_marcas()