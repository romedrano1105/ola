from flask import jsonify, Blueprint, request
from Domain.sucursal_rules import SucursalRules

sucursal_bp = Blueprint('sucursal', __name__)

sucursales = {
    201: {"id": 201, "nombre": "Alvincito Dental", "direccion": "Soyapango", "telefono": "8732-9122"}
}

@sucursal_bp.get("/sucursal")
def mostrar_sucursales():
    return jsonify(list(sucursales.values()))

@sucursal_bp.get("/sucursal/<int:id>")
def obtener_sucursal(id):
    sucursal = sucursales.get(id)

    if sucursal:
        return jsonify(sucursal)
    return jsonify({"error": "Esta sucursal no se ha encontrado"})

@sucursal_bp.post("/sucursal")
def agregar_sucursal():
    datos = request.get_json()

    try:
        SucursalRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    
    nuevo_id = max(sucursales.keys()) + 1

    sucursales[nuevo_id] = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "direccion": datos["direccion"],
        "telefono": datos["telefono"]
    }

    return jsonify(sucursales[nuevo_id]), 201