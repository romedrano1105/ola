from flask import Flask, jsonify, request

app = Flask(__name__)


doctores = {
    "DOC000001": {
        "ID_doctor": "DOC000001", "Nombre_doctor": "Juan Pérez López",
        "JVPO_doctor": "1234", "ID_sucursal": "SUC0001", "ID_especialidad": "Ortodoncia"},
    "DOC000002": {
        "ID_doctor": "DOC000002", "Nombre_doctor": "María Fernández Rivas",
        "JVPO_doctor": "2345", "ID_sucursal": "SUC0001", "ID_especialidad": "Endodoncia"},
    "DOC000003": {
        "ID_doctor": "DOC000003", "Nombre_doctor": "Carlos Martínez Gómez",
        "JVPO_doctor": "3456", "ID_sucursal": "SUC0002", "ID_especialidad": "Periodoncia"},
    "DOC000004": {
        "ID_doctor": "DOC000004", "Nombre_doctor": "Ana Sofía Ramírez",
        "JVPO_doctor": "4567", "ID_sucursal": "SUC0002", "ID_especialidad": "Odontopediatría"},
    "DOC000005": {
        "ID_doctor": "DOC000005", "Nombre_doctor": "Roberto Castillo Díaz",
        "JVPO_doctor": "5678", "ID_sucursal": "SUC0003", "ID_especialidad": "Cirugía Maxilofacial"},
}

@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "API REST de Clínica Odontológica",
            "version": "1.0",
            "EndPoints": [
            "GET /doctores", # muestra todos los doctores,
            "GET /doctores/<id>", # Informacion de UN doctor,
            "POST /doctores", # crear un nuevo doctor
            "PUT /doctores/<id>", # modificar un doctor
            "DELETE /doctores/<id>", # BORRAR UN DOCTOR
            ]
        }
    )


@app.get("/doctores")
def obtener_doctores():
    return jsonify(list(doctores.values()))


@app.get("/doctores/<id>")
def obtener_doctor(id):
    doctor = doctores.get(id)

    if doctor:
        return jsonify(doctor)

    return jsonify({"error": "Doctor no encontrado"}), 404


@app.post("/doctores")
def agregar_doctor():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar informacion"}), 400
    if "ID_doctor" not in datos or "Nombre_doctor" not in datos or "ID_especialidad" not in datos:
        return jsonify({"error": "Los campos son requeridos"}), 400

    nuevo_id = datos["ID_doctor"]
    doctores[nuevo_id] = {
        "ID_doctor": nuevo_id,
        "Nombre_doctor": datos["Nombre_doctor"],
        "JVPO_doctor": datos.get("JVPO_doctor", ""),
        "ID_sucursal": datos.get("ID_sucursal", ""),
        "ID_especialidad": datos["ID_especialidad"]
    }

    return jsonify(doctores[nuevo_id]), 201


@app.put("/doctores/<id>")
def actualizar_doctor(id):
    if id not in doctores:
        return jsonify({"error": "Doctor no encontrado"}), 404

    datos = request.get_json()
    doctores[id].update(datos)

    return jsonify(doctores[id])


@app.delete("/doctores/<id>")
def eliminar_doctor(id):
    if id not in doctores:
        return jsonify({"error": "Doctor no encontrado"}), 404

    del doctores[id]
    return jsonify({"mensaje": "Doctor eliminado correctamente"})


if __name__ == "__main__":
    app.run(debug=True)