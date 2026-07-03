from flask import Blueprint, jsonify, request
from Domain.cita_rules import CitaRules

citas_bp = Blueprint('citas', __name__)

citas = {
    701: {
        "id": 701,
        "id_paciente": 501,
        "fecha_hora": "2026-07-03 09:00",
        "motivo": "Limpieza",
        "estado": "programada"
    }
}

@citas_bp.get("/citas")
def mostrar_citas():
    return jsonify(list(citas.values()))

@citas_bp.get("/citas/<int:id>")
def obtener_cita(id):
    cita = citas.get(id)

    if cita:
        return jsonify(cita)
    return jsonify({"error": "Esta cita no ha sido registrada en el sistema"})

@citas_bp.post("/citas")
def agregar_cita():
    datos = request.get_json()

    try:
        CitaRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    nuevo_id = max(citas.keys()) + 1

    citas[nuevo_id] = {
        "id": nuevo_id,
        "id_paciente": datos["id_paciente"],
        "fecha_hora": datos["fecha_hora"],
        "motivo": datos["motivo"],
        "estado": datos.get("estado", "programada")
    }

    return jsonify(citas[nuevo_id]), 201