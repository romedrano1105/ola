from flask import jsonify, Blueprint, request
from rutas.paciente import pacientes
from Domain.expediente_rules import ExpedienteRules

expedientes_bp = Blueprint('expediente', __name__)

expedientes = {
    601: {
        "id": 601,
        "id_paciente": pacientes[501]["id"],
        "fecha_apertura": "01/07/2026",
        "alergias_medicamentos": "Alergia a Gaby",
        "enfermedades_existentes": "cancer",
        "notas_medicas": "El paciente esta bien, dejar de alta",
    }
}


@expedientes_bp.get("/expediente")
def mostrar_expedientes():
    return jsonify(list(expedientes.values()))


@expedientes_bp.get("/expediente/<int:id>")
def obtener_expediente(id):
    expediente = expedientes.get(id)

    if expediente:
        return jsonify(expediente)
    return jsonify({"error": "Este expediente no ha sido registrado en el sistema"})


@expedientes_bp.post("/expediente")
def agregar_expediente():
    datos = request.get_json()

    try:
        ExpedienteRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    nuevo_id = max(expedientes.keys()) + 1

    expedientes[nuevo_id] = {
        "id": nuevo_id,
        "id_paciente": datos["id_paciente"],
        "fecha_apertura": datos["fecha_apertura"],
        "alergias_medicamentos": datos["alergias_medicamentos"],
        "enfermedades_existentes": datos["enfermedades_existentes"],
        "notas_medicas": datos["notas_medicas"],
    }

    return jsonify(expedientes[nuevo_id]), 201