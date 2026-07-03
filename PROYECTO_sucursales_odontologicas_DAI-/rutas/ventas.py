from flask import jsonify, Blueprint, request
from rutas.sucursal import sucursales
from Domain.venta_rules import VentaRules

ventas_bp = Blueprint('ventas', __name__)


ventas = {
    101: {"id": 101, "fecha_venta": "15/06/2026", "monto_venta": 45.99, "id_sucursal": sucursales[201]["id"]}
}

@ventas_bp.get("/ventas")
def mostrar_ventas():
    return jsonify(list(ventas.values()))

@ventas_bp.get("/ventas/<int:id>")
def obtener_venta(id):
    venta = ventas.get(id)

    if venta:
        return jsonify(venta)
    return jsonify({"error": "Esta venta no se ha encontrado"})

@ventas_bp.post("/ventas")
def agregar_venta():
    datos = request.get_json()

    try:
        VentaRules.validar_creacion(datos)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    
    nuevo_id = max(ventas.keys()) + 1

    ventas[nuevo_id] = {
        "id": nuevo_id,
        "fecha_venta": datos["fecha_venta"],
        "monto_venta": datos["monto_venta"],
        "id_sucursal": datos["id_sucursal"]
    }

    return jsonify(ventas[nuevo_id]), 201

