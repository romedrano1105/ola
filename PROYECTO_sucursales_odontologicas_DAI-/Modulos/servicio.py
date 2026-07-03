class Servicio:
    def __init__(self, id_servicio: str, nombre: str, descripcion: str = ""):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.descripcion = descripcion

    def validar_datos(self):
        if not self.id_servicio or not self.nombre:
            raise ValueError("El servicio necesita un id y un nombre")

    def registrar_servicio(self, servicios):
        self.validar_datos()
        servicios[self.id_servicio] = self.to_dict()
        return servicios

    def to_dict(self):
        return {
            "id_servicio": self.id_servicio,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
        }

    def eliminar_servicio(self, servicios):
        if self.id_servicio in servicios:
            del servicios[self.id_servicio]
        return servicios

    def __str__(self):
        return f"Servicio({self.id_servicio}, {self.nombre})"
