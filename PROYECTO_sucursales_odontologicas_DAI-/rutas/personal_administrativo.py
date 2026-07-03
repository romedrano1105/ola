from flask import jsonify, Blueprint, request
from rutas.rol import roles
from rutas.sucursal import sucursales
from Domain.personal_administrativo_rules import PersonalAdministrativoRules

personal_admin_bp = Blueprint('personal_admin', __name__)

empleados_admin = {
    301: {"id": 301, "nombre": "Juanito", "id_rol": roles[401]["id"], "id_sucursal": sucursales[201]["id"]}
}

@personal_admin_bp.get("/personal_admin")
def mostrar_personal():
    return jsonify(list(empleados_admin.values()))

@personal_admin_bp.get("/personal_admin/<int:id>")
def obtener_empleado(id):
    empleado = empleados_admin.get(id)

    if empleado:
        return jsonify(empleado)
    return jsonify({"error": "Este empleado no esta registrado en el sistema"})

@personal_admin_bp.post("/personal_admin")
def agregar_empleado():
    datos = request.get_json()

    try:
        PersonalAdministrativoRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    
    nuevo_id = max(empleados_admin.keys()) + 1

    empleados_admin[nuevo_id] = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "id_rol": datos["id_rol"],
        "id_sucursal": datos["id_sucursal"]
    }

    return jsonify(empleados_admin[nuevo_id]), 201