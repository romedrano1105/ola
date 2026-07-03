from datetime import datetime


class Expediente:
    def __init__(self, id_expediente: str, id_paciente: str, fecha_apertura: datetime,
                 alergias_medicamentos: str, enfermedades_preexistentes: str, notas_medicas: str):
        self.id_expediente = id_expediente
        self.id_paciente = id_paciente
        self.fecha_apertura = fecha_apertura
        self.alergias_medicamentos = alergias_medicamentos
        self.enfermedades_preexistentes = enfermedades_preexistentes
        self.notas_medicas = notas_medicas

    def registrar_expediente(self, expedientes):
        if not self.id_expediente or not self.id_paciente:
            raise ValueError("El expediente necesita un id de expediente y un id de paciente")

        expedientes[self.id_expediente] = self.to_dict()
        return expedientes

    def to_dict(self):
        return {
            "id_expediente": self.id_expediente,
            "id_paciente": self.id_paciente,
            "fecha_apertura": self.fecha_apertura,
            "alergias_medicamentos": self.alergias_medicamentos,
            "enfermedades_preexistentes": self.enfermedades_preexistentes,
            "notas_medicas": self.notas_medicas,
        }

    def modificar_expediente(self, expedientes, **campos):
        if self.id_expediente not in expedientes:
            raise KeyError("El expediente no existe")
        for clave, valor in campos.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
            expedientes[self.id_expediente][clave] = valor
        return expedientes

    def almacenar_diccionario(self):
        return {
            "id": self.id_expediente,
            "id_paciente": self.id_paciente,
            "fecha_apertura": self.fecha_apertura,
            "alergias_medicamentos": self.alergias_medicamentos,
            "enfermedades_preexistentes": self.enfermedades_preexistentes,
            "notas_medicas": self.notas_medicas,
        }

    def __str__(self):
        return f"Expediente({self.id_expediente}, paciente={self.id_paciente})"
        