import unittest
from src.classes.Operator import Operator

class TestOperator(unittest.TestCase):
    def setUp(self):
        """Setup: Crea un operador con atributos de prueba."""
        self.operator = Operator(
            user_token="user123",
            password_token="pass123",
            client_id=1,
            name="John Doe",
            document="123456789",
            phone="123-456-7890",
            email="johndoe@email.com",
            address="123 Street, City",
            document_type="ID"
        )

    def test_validate(self):
        """Prueba que la validación de dirección funcione correctamente."""
        self.assertTrue(self.operator.validate())

        self.operator.address = "  "  # Dirección vacía (solo espacios)
        self.assertFalse(self.operator.validate())

    def test_get_information(self):
        """Prueba que `get_information` retorne la información correctamente."""
        expected_output = (
            "ID: 1\n- Document Type: ID"
            "\n- Document: 123456789\n- Name: John Doe"
            "\n- Phone: 123-456-7890\n- Email: johndoe@email.com"
            "\n- Address: 123 Street, City."
        )
        self.assertEqual(self.operator.get_information(), expected_output)

if __name__ == "__main__":
    unittest.main()
