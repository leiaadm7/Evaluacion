Plataforma de Gestión de Visitas

API + Cliente Web con Autenticación JWT

Descripción del caso

Este proyecto implementa un sistema para gestionar visitas utilizando una API REST con autenticación JWT y un cliente web que permite consumir dicha API.

El sistema está compuesto por dos repositorios:

Backend / API: https://github.com/leiaadm7/Evaluacion.git

API desarrollada en Node.js + Express, con rutas públicas y protegidas, manejo de tokens JWT y políticas CORS.

Cliente Web: https://github.com/leiaadm7/cliente-visita.git

Aplicación web que permite autenticarse, obtener el token JWT y consumir rutas protegidas mostrando los datos en tablas y gráficos.

Este proyecto demuestra cómo se implementa un flujo completo de autenticación, autorización y consumo de datos protegidos.

Instalación y ejecución local
Backend (API)

Repositorio: Evaluacion

Clonar
git clone https://github.com/leiaadm7/Evaluacion.git
cd Evaluacion

Instalar dependencias
npm install

Configurar variables de entorno

Crear un archivo .env en la raíz 
Ejecutar API

Render: https://evaluacion-s29l.onrender.com 

Cliente web

Repositorio: cliente-visita

Clonar
git clone https://github.com/leiaadm7/cliente-visita.git
cd cliente-visita

Ejecutar cliente

Este proyecto NO requiere instalación.
Solo abre:
https://leiaadm7.github.io/cliente-visita/ 

Autenticación (JWT)

El sistema utiliza JSON Web Tokens para proteger rutas.
Primero se debe obtener un token desde el endpoint de autenticación.

Endpoint para login
POST /api/auth/login

Ejemplo de payload
{
  "username": "admin",
  "password": "123456"
}

Respuesta esperada
{
  "token": "eyJh..."
}

Cómo acceder a rutas protegidas

Agregar en el header:

Authorization: Bearer <token>

Rutas principales de la API
Públicas
Login
POST /api/auth/login

Protegidas (requieren token)
 Obtener todas las visitas
GET /api/visitas

Registrar una visita
POST /api/visitas


Body ejemplo:

{
  "nombre": "Juan Pérez",
  "motivo": "Reunión"
}

Estadísticas de visitas
GET /api/visitas/stats

URL de despliegue en la nube

La API está desplegada en Render:

https://evaluacion-s29l.onrender.com/api


El cliente puede configurarse para apuntar directo a esta API en producción.

Repositorio del Cliente

El cliente web permite:

Iniciar sesión contra la API

Obtener el token JWT

Guardarlo temporalmente

Consumir rutas protegidas

Mostrar datos en tablas y gráficos con Chart.js

Visualizar estadísticas en tiempo real

Incluye:

cliente_api.js   → Manejo de token y consumo de la API
index.html       → Interfaz principal
styles.css       → Estilos
Gráficos y secciones para pruebas

Instrucciones para usar el cliente

Abrir index.html

Ingresar usuario y contraseña

Hacer clic en Login

El cliente:

Obtiene token desde la API

Lo almacena en memoria

Habilita los botones protegidos

Registrar nuevas visitas

Visualizar datos en tablas y gráficos

Problema que resuelve

El cliente web actúa como una herramienta que facilita probar la API sin Postman.
Permite visualizar:

Funcionamiento de la autenticación JWT

Cómo se envía el token en peticiones

Cómo responde la API a errores 401

Estadísticas en tiempo real representadas en gráficos

Es útil para demostración, pruebas y validación del backend.

