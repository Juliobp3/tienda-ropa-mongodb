// =============================================
// CONFIGURACIÓN DE LA API
// =============================================

// IMPORTANTE: La URL debe terminar con /
const API_URL = 'http://127.0.0.1:5000/api/';

function getToken() {
    return localStorage.getItem('token');
}

// =============================================
// FUNCIONES GENÉRICAS PARA LA API
// =============================================

async function peticionAPI(endpoint, metodo = 'GET', datos = null) {
    const token = getToken();
    
    if (!token) {
        throw new Error('No hay token guardado. Por favor, inicia sesión.');
    }

    // Asegurar que el endpoint no tenga / al inicio
    const endpointLimpio = endpoint.startsWith('/') ? endpoint.slice(1) : endpoint;
    const url = `${API_URL}${endpointLimpio}`;

    const opciones = {
        method: metodo,
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    };

    if (datos) {
        opciones.body = JSON.stringify(datos);
    }

    try {
        console.log(`📡 ${metodo} ${url}`);
        const response = await fetch(url, opciones);
        
        if (!response.ok) {
            let errorMsg = `Error ${response.status}: ${response.statusText}`;
            try {
                const error = await response.json();
                if (error.error) errorMsg = error.error;
            } catch (e) {}
            throw new Error(errorMsg);
        }

        return await response.json();
    } catch (error) {
        console.error('❌ Error en peticionAPI:', error);
        throw error;
    }
}

// =============================================
// FUNCIONES POR ENDPOINT
// =============================================

// ---------- PRENDAS ----------
export async function obtenerPrendas() {
    const data = await peticionAPI('prendas');
    return data.data || [];
}

export async function crearPrenda(prenda) {
    return await peticionAPI('prendas', 'POST', prenda);
}

export async function actualizarPrenda(id, datos) {
    return await peticionAPI(`prendas/${id}`, 'PUT', datos);
}

export async function eliminarPrenda(id) {
    return await peticionAPI(`prendas/${id}`, 'DELETE');
}

// ---------- MARCAS ----------
export async function obtenerMarcas() {
    const data = await peticionAPI('marcas');
    return data.data || [];
}

// ---------- REPORTES ----------
export async function obtenerMarcasConVentas() {
    const data = await peticionAPI('reportes/marcas-con-ventas');
    return data.data || [];
}

export async function obtenerStockRestante() {
    const data = await peticionAPI('reportes/stock-restante');
    return data.data || [];
}

export async function obtenerTopMarcas() {
    const data = await peticionAPI('reportes/top-marcas');
    return data.data || [];
}