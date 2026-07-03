from flask import Flask, jsonify

from rutas.citas import citas_bp
from rutas.expediente import expedientes_bp
from rutas.paciente import paciente_bp
from rutas.personal_administrativo import personal_admin_bp
from rutas.rol import rol_bp
from rutas.sucursal import sucursal_bp
from rutas.ventas import ventas_bp

app = Flask(__name__)

# Registrar blueprints en el servidor principal
app.register_blueprint(citas_bp)
app.register_blueprint(expedientes_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(personal_admin_bp)
app.register_blueprint(rol_bp)
app.register_blueprint(sucursal_bp)
app.register_blueprint(ventas_bp)


@app.get("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la app de sucursales odontológicas",
        "version": "1.0",
        "endpoints": [
            "GET    /ventas",
            "GET    /ventas/<id>",
            "POST   /ventas",
            "GET    /sucursal",
            "GET    /sucursal/<id>",
            "POST   /sucursal",
            "GET    /expediente",
            "GET    /expediente/<id>",
            "POST   /expediente",
            "GET    /personal_admin",
            "GET    /personal_admin/<id>",
            "POST   /personal_admin",
            "GET    /rol",
            "GET    /rol/<id>",
            "POST   /rol",
            "GET    /paciente",
            "GET    /paciente/<id>",
            "POST   /paciente",
            "GET    /citas",
            "GET    /citas/<id>",
            "POST   /citas",
        ],
    })


if __name__ == "__main__":
    app.run(debug=True)