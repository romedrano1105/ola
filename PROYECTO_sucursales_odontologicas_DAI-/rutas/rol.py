from flask import jsonify, Blueprint, request
from Domain.rol_rules import RolRules

rol_bp = Blueprint('rol', __name__)

roles = {
    401:{"id": 401, "nombre_rol": "Dentista", "descripcion": "Es dentista JHJAJJA"}
}

@rol_bp.get("/rol")
def mostrar_roles():
    return jsonify(list(roles.values()))

@rol_bp.get("/rol/<int:id>")
def obtener_rol(id):
    rol = roles.get(id)

    if rol:
        return jsonify(rol)
    return jsonify({"error": "Rol no disponible"})

@rol_bp.post("/rol")
def agregar_rol():
    datos = request.get_json()

    try:
        RolRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    
    nuevo_id = max(roles.keys()) + 1

    roles[nuevo_id] = {
        "id": nuevo_id,
        "nombre_rol": datos["nombre_rol"],
        "descripcion": datos["descripcion"]
    }

    return jsonify(roles[nuevo_id]), 201