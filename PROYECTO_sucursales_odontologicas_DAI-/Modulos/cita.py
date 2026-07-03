from datetime import datetime


class Cita:
    def __init__(self, id_cita: str, id_sucursal: str, horario_cita: datetime, id_doctor: str, id_expediente: str, id_servicio: str):
        self.id_cita = id_cita
        self.id_sucursal = id_sucursal
        self.horario_cita = horario_cita
        self.id_doctor = id_doctor
        self.id_expediente = id_expediente
        self.id_servicio = id_servicio

    def validar_datos(self):
        if not self.id_cita or not self.id_sucursal or not self.id_doctor or not self.id_expediente or not self.id_servicio:
            raise ValueError("Todos los identificadores de la cita son requeridos")
        if not self.horario_cita:
            raise ValueError("El horario de la cita no puede estar vacío")

    def registrar_cita(self, citas):
        self.validar_datos()
        citas[self.id_cita] = self.to_dict()
        return citas

    def to_dict(self):
        return {
            "id_cita": self.id_cita,
            "id_sucursal": self.id_sucursal,
            "horario_cita": self.horario_cita,
            "id_doctor": self.id_doctor,
            "id_expediente": self.id_expediente,
            "id_servicio": self.id_servicio,
        }

    def modificar_cita(self, citas, **campos):
        if self.id_cita not in citas:
            raise KeyError("La cita no existe")
        for clave, valor in campos.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
            citas[self.id_cita][clave] = valor
        return citas

    def eliminar_cita(self, citas):
        if self.id_cita in citas:
            del citas[self.id_cita]
        return citas

    def __str__(self):
        return f"Cita({self.id_cita}, {self.horario_cita}, servicio={self.id_servicio})"
