import { 
    obtenerMarcasConVentas, 
    obtenerStockRestante, 
    obtenerTopMarcas 
} from './api.js';

export async function cargarMarcasConVentas() {
    const contenedor = document.getElementById('reporteMarcasConVentas');
    try {
        contenedor.innerHTML = '<div class="cargando">⏳ Cargando...</div>';
        const data = await obtenerMarcasConVentas();
        mostrarReporte(contenedor, data, 'Marcas con Ventas', '_id');
    } catch (error) {
        contenedor.innerHTML = `<div class="error">❌ ${error.message}</div>`;
    }
}

export async function cargarStockRestante() {
    const contenedor = document.getElementById('reporteStockRestante');
    try {
        contenedor.innerHTML = '<div class="cargando">⏳ Cargando...</div>';
        const data = await obtenerStockRestante();
        
        if (data.length === 0) {
            contenedor.innerHTML = '<div class="cargando">📭 No hay datos de stock</div>';
            return;
        }

        let html = `<div class="exito">✅ ${data.length} registros</div>
            <table><thead><tr>
                <th>Prenda</th><th>Vendido</th>
                <th>Stock Original</th><th>Stock Restante</th>
            </tr></thead><tbody>`;

        data.forEach(item => {
            html += `<tr>
                <td><strong>${item.nombre || 'N/A'}</strong></td>
                <td>${item.vendido || 0}</td>
                <td>${item.stockOriginal || 0}</td>
                <td>${item.stockRestante || 0}</td>
            </tr>`;
        });

        html += `</tbody></table>`;
        contenedor.innerHTML = html;
    } catch (error) {
        contenedor.innerHTML = `<div class="error">❌ ${error.message}</div>`;
    }
}

export async function cargarTopMarcas() {
    const contenedor = document.getElementById('reporteTopMarcas');
    try {
        contenedor.innerHTML = '<div class="cargando">⏳ Cargando...</div>';
        const data = await obtenerTopMarcas();
        
        if (data.length === 0) {
            contenedor.innerHTML = '<div class="cargando">📭 No hay datos de marcas</div>';
            return;
        }

        let html = `<div class="exito">🏆 Top ${data.length} marcas más vendidas</div>
            <table><thead><tr>
                <th>#</th><th>Marca</th><th>Total Ventas</th>
            </tr></thead><tbody>`;

        data.forEach((item, index) => {
            html += `<tr>
                <td><strong>${index + 1}</strong></td>
                <td><strong>${item._id || 'N/A'}</strong></td>
                <td>${item.totalVentas || 0}</td>
            </tr>`;
        });

        html += `</tbody></table>`;
        contenedor.innerHTML = html;
    } catch (error) {
        contenedor.innerHTML = `<div class="error">❌ ${error.message}</div>`;
    }
}

function mostrarReporte(contenedor, data, titulo, campo) {
    if (data.length === 0) {
        contenedor.innerHTML = `<div class="cargando">📭 No hay datos para ${titulo}</div>`;
        return;
    }

    let html = `<div class="exito">✅ ${data.length} registros</div>
        <table><thead><tr><th>${titulo}</th></tr></thead><tbody>`;

    data.forEach(item => {
        html += `<tr><td>${item[campo] || 'N/A'}</td></tr>`;
    });

    html += `</tbody></table>`;
    contenedor.innerHTML = html;
}