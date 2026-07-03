from flask import jsonify, Blueprint, request
from rutas.sucursal import sucursales
from Domain.paciente_rules import PacienteRules

paciente_bp = Blueprint('paciente', __name__)

pacientes = {
    501: {"id": 501, "nombre_paciente": "Carlo", "dui_paciente": "12345678-9", "telefono": "8923-1232", "id_sucursal": sucursales[201]["id"]}
}

@paciente_bp.get("/paciente")
def mostrar_pacientes():
    return jsonify(list(pacientes.values()))

@paciente_bp.get("/paciente/<int:id>")
def obtener_paciente(id):
    paciente = pacientes.get(id)

    if paciente:
        return jsonify(paciente)
    return jsonify({"error": "Este paciente no ha sido registrado en el sistema"})

@paciente_bp.post("/paciente")
def agregar_paciente():
    datos = request.get_json()

    try:
        PacienteRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    
    nuevo_id = max(pacientes.keys()) + 1

    pacientes[nuevo_id] = {
        "id": nuevo_id,
        "nombre_paciente": datos["nombre_paciente"],
        "dui_paciente": datos["dui_paciente"],
        "telefono": datos["telefono"],
        "id_sucursal": datos["id_sucursal"]
    }

    return jsonify(pacientes[nuevo_id]), 201
