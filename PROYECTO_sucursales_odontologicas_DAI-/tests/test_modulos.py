import unittest
from datetime import datetime

from Modulos.cita import Cita
from Modulos.Doctor import Doctor
from Modulos.expediente import Expediente
from Modulos.servicio import Servicio


class ModulosTests(unittest.TestCase):
    def test_cita_registrar_modificar_y_eliminar(self):
        citas = {}
        cita = Cita("C1", "S1", datetime(2026, 7, 3, 10, 0), "D1", "E1", "SV1")
        cita.registrar_cita(citas)
        self.assertIn("C1", citas)

        cita.modificar_cita(citas, horario_cita=datetime(2026, 7, 3, 11, 0))
        self.assertEqual(citas["C1"]["horario_cita"], datetime(2026, 7, 3, 11, 0))

        cita.eliminar_cita(citas)
        self.assertNotIn("C1", citas)

    def test_doctor_registrar_y_disponibilidad(self):
        doctores = {}
        doctor = Doctor("D1", "Dr. Pérez", "JVPO1", "S1", "ES1")
        doctor.registrar_doctor(doctores)
        self.assertIn("D1", doctores)
        self.assertTrue(doctor.Disponibilidad())

    def test_expediente_registrar_y_actualizar(self):
        expedientes = {}
        expediente = Expediente("E1", "P1", datetime(2026, 7, 3), "Penicilina", "Diabetes", "Seguimiento")
        expediente.registrar_expediente(expedientes)
        self.assertIn("E1", expedientes)

        expediente.modificar_expediente(expedientes, notas_medicas="Nueva nota")
        self.assertEqual(expedientes["E1"]["notas_medicas"], "Nueva nota")

    def test_servicio_registrar_y_eliminar(self):
        servicios = {}
        servicio = Servicio("SV1", "Limpieza", "Limpieza dental")
        servicio.registrar_servicio(servicios)
        self.assertIn("SV1", servicios)

        servicio.eliminar_servicio(servicios)
        self.assertNotIn("SV1", servicios)


if __name__ == "__main__":
    unittest.main()
