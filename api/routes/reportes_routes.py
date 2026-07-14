from flask import Blueprint
from api.controllers.reportes_controller import ReportesController

reportes_bp = Blueprint('reportes', __name__)

@reportes_bp.route('/marcas-con-ventas', methods=['GET'])
def marcas_con_ventas():
    return ReportesController.marcas_con_ventas()

@reportes_bp.route('/stock-restante', methods=['GET'])
def stock_restante():
    return ReportesController.stock_restante()

@reportes_bp.route('/top-marcas', methods=['GET'])
def top_marcas():
    return ReportesController.top_marcas()