from flask import Flask, jsonify, send_from_directory  # Agregar send_from_directory
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv
import os

load_dotenv()

from api.routes.usuario_routes import usuario_bp
from api.routes.marca_routes import marca_bp
from api.routes.prenda_routes import prenda_bp
from api.routes.venta_routes import venta_bp
from api.routes.reportes_routes import reportes_bp

app = Flask(__name__, static_folder='static')  # Agregar static_folder
CORS(app)

app.config['SWAGGER'] = {
    'title': 'API Tienda de Ropa',
    'description': 'API para gestionar una tienda de ropa',
    'version': '1.0.0'
}
Swagger(app)

app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
app.register_blueprint(marca_bp, url_prefix='/api/marcas')
app.register_blueprint(prenda_bp, url_prefix='/api/prendas')
app.register_blueprint(venta_bp, url_prefix='/api/ventas')
app.register_blueprint(reportes_bp, url_prefix='/api/reportes')

@app.route('/')
def index():
    return jsonify({
        'mensaje': 'API de Tienda de Ropa funcionando',
        'version': '1.0.0',
        'endpoints': {
            'usuarios': '/api/usuarios',
            'marcas': '/api/marcas',
            'prendas': '/api/prendas',
            'ventas': '/api/ventas',
            'reportes': '/api/reportes'
        },
        'documentacion': '/apidocs',
        'frontend': '/listado.html'  # NUEVO: acceso al HTML
    })

# NUEVA RUTA: Servir el archivo HTML
@app.route('/listado.html')
def servir_listado():
    return send_from_directory('static', 'listado.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)