class Doctor:
    def __init__(self, id_doctor: str, nombre: str, jvpo_doctor: str, id_sucursal: str, id_especialidad: str):
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.jvpo_doctor = jvpo_doctor
        self.id_sucursal = id_sucursal
        self.id_especialidad = id_especialidad

    def validar_datos(self):
        if not self.id_doctor or not self.nombre or not self.id_sucursal or not self.id_especialidad:
            raise ValueError("Faltan datos obligatorios del doctor")

    def registrar_doctor(self, doctores):
        self.validar_datos()
        doctores[self.id_doctor] = self.to_dict()
        return doctores

    def to_dict(self):
        return {
            "id_doctor": self.id_doctor,
            "nombre": self.nombre,
            "jvpo_doctor": self.jvpo_doctor,
            "id_sucursal": self.id_sucursal,
            "id_especialidad": self.id_especialidad
        }

    def Disponibilidad(self):
        return True

    def __str__(self):
        return f"Doctor({self.id_doctor}, {self.nombre}, especialidad={self.id_especialidad})"
