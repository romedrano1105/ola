import unittest

from domain.cita_rules import CitaRules
from domain.paciente_rules import PacienteRules
from domain.personal_administrativo_rules import PersonalAdministrativoRules
from domain.rol_rules import RolRules
from domain.sucursal_rules import SucursalRules


class DomainRulesTests(unittest.TestCase):
    def test_identificador_rechaza_simbolos(self):
        with self.assertRaises(ValueError):
            PacienteRules.validar_identificador("ABC-123")

        with self.assertRaises(ValueError):
            RolRules.validar_identificador("ABC#123")

    def test_textos_rechazan_simbolos(self):
        with self.assertRaises(ValueError):
            CitaRules.validar_texto("Consulta@Dental", "motivo")

        with self.assertRaises(ValueError):
            PersonalAdministrativoRules.validar_texto("José#Perez", "nombre")

    def test_sucursal_nombre_rechaza_simbolos(self):
        with self.assertRaises(ValueError):
            SucursalRules.validar_texto("Sucursal@1", "nombre")


if __name__ == "__main__":
    unittest.main()
