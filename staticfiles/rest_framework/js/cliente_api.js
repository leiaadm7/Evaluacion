/*
    Funciones:
      - obtenerToken()
      - mostrarPanelDatos()
      - cerrarSesion()
      - cargarVisitas()
   Todo el JS está separado del HTML para evitar errores.
*/

// Detecta automáticamente la URL base donde está corriendo la API.
const API_BASE_URL = window.location.origin + "/api";

// Obtener token
async function obtenerToken() {
    const username = document.getElementById("api-username").value;
    const password = document.getElementById("api-password").value;
    const msgLabel = document.getElementById("login-message");

    if (!username || !password) {
        msgLabel.innerText = "Por favor ingresa usuario y contraseña.";
        msgLabel.className = "text-red-500";
        return;
    }

    // Mensaje temporal
    msgLabel.innerText = "Conectando...";
    msgLabel.className = "text-gray-500";

    try {
        const response = await fetch(`${API_BASE_URL}/token/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });

        if (!response.ok) {
            msgLabel.innerText = "Credenciales incorrectas.";
            msgLabel.className = "text-red-600";
            return;
        }

        const data = await response.json();

        // Guardamos tokens en el navegador
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);

        msgLabel.innerText = "¡Autenticación exitosa!";
        msgLabel.className = "text-green-600";

        // Cambiamos a la vista de datos
        setTimeout(mostrarPanelDatos, 800);
    } catch (error) {
        msgLabel.innerText = "Error de conexión con el servidor.";
        msgLabel.className = "text-red-600";
        console.error("Error al obtener token:", error);
    }
}

// Mostrar panel de datos si ya se tiene token 
function mostrarPanelDatos() {
    const token = localStorage.getItem("access_token");

    if (token) {
        document.getElementById("login-section").classList.add("hidden");
        document.getElementById("data-section").classList.remove("hidden");

        // Mostrar parte del token por estética
        document.getElementById("token-display").innerText =
            token.substring(0, 50) + "...";
    }
}

// Cerrar sesión y limpiar tokens
function cerrarSesion() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");

    document.getElementById("data-section").classList.add("hidden");
    document.getElementById("login-section").classList.remove("hidden");
    document.getElementById("login-message").innerText = "";
}

// Cargar visitas usando token
async function cargarVisitas() {
    const token = localStorage.getItem("access_token");
    const tabla = document.getElementById("tabla-body");
    const loader = document.getElementById("loading-indicator");

    if (!token) {
        alert("Tu sesión ha expirado. Por favor inicia sesión nuevamente.");
        cerrarSesion();
        return;
    }

    loader.classList.remove("hidden");

    try {
        const response = await fetch(`${API_BASE_URL}/visita/`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`, // Se envía el token al servidor
                "Content-Type": "application/json",
            },
        });

        if (!response.ok) {
            tabla.innerHTML =
                `<tr><td colspan="5" class="text-center py-6 text-red-500">Error al cargar datos.</td></tr>`;
            return;
        }

        const data = await response.json();

        tabla.innerHTML = "";

        // DRF puede devolver lista [] o { results: [] }
        const lista = Array.isArray(data) ? data : data.results || [];

        if (lista.length === 0) {
            tabla.innerHTML =
                `<tr><td colspan="5" class="text-center py-6 text-gray-500">No hay visitas registradas en la API.</td></tr>`;
            return;
        }

        lista.forEach((v) => {
            tabla.innerHTML += `
                <tr class="hover:bg-pink-50 transition">
                    <td class="px-4 py-3">${v.id}</td>
                    <td class="px-4 py-3">${v.nombre} ${v.apellido ?? ""}</td>
                    <td class="px-4 py-3">${v.rut}</td>
                    <td class="px-4 py-3">
                        <span class="px-2 py-1 rounded-full text-xs font-bold
                            ${v.estado === "FINALIZADA" 
                                ? "bg-gray-200 text-gray-700" 
                                : "bg-green-100 text-green-700"}">
                            ${v.estado}
                        </span>
                    </td>
                    <td class="px-4 py-3">${v.fecha}</td>
                </tr>
            `;
        });

    } catch (error) {
        console.error("Error al cargar visitas:", error);
    } finally {
        loader.classList.add("hidden");
    }
}

// Auto-ejecución al abrir pagina
document.addEventListener("DOMContentLoaded", () => {
    if (localStorage.getItem("access_token")) {
        mostrarPanelDatos();
    }
});
