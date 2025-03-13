import unittest
from src.person import Person
from src.client import Client
from src.person_operator import Operator

class TestPerson(unittest.TestCase):

    def test_abstract_class(self):
        """Verifica que no se pueda instanciar directamente `Person`."""
        with self.assertRaises(TypeError):
            Person(1, "John Doe", "123456", "555-1234", "john@example.com", "123 Main St", "ID")

    def setUp(self):
        """Crea instancias de Client y Operator para pruebas."""
        self.client = Client(1, "Alice", "987654", "555-5678", "alice@example.com", "456 Elm St", "Passport")
        self.operator = Operator("user123", "pass456", 2, "Bob", "654321", "555-9876", "bob@example.com", "789 Oak St", "Driver's License")

    def test_client_validation(self):
        """Verifica que la validación del cliente funcione correctamente."""
        self.assertTrue(self.client.validate())

    def test_client_info(self):
        """Verifica que `get_information()` en `Client` devuelva datos correctamente."""
        info = self.client.get_information()
        self.assertIn("Alice", info)
        self.assertIn("456 Elm St", info)

    def test_operator_info(self):
        """Verifica que `get_information()` en `Operator` devuelva datos correctamente."""
        info = self.operator.get_information()
        self.assertIn("Bob", info)
        self.assertIn("789 Oak St", info)

if __name__ == "__main__":
    unittest.main()
