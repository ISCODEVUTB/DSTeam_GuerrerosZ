import unittest
from src.operator import Operator

class TestOperator(unittest.TestCase):
    def setUp(self):
        """Setup a sample Operator instance for testing."""
        self.operator = Operator(
            user_token="test_token",
            password_token="test_password",
            client_id=1,
            name="John Doe",
            document="12345678",
            phone="123-456-7890",
            email="johndoe@example.com",
            address="123 Main St",
            document_type="DNI"
        )
    
    def test_initialization(self):
        """Test that the Operator is initialized correctly."""
        self.assertEqual(self.operator._user_token, "test_token")
        self.assertEqual(self.operator._password_token, "test_password")
        self.assertEqual(self.operator._person_id, 1)
        self.assertEqual(self.operator._name, "John Doe")
        self.assertEqual(self.operator._document, "12345678")
        self.assertEqual(self.operator._phone, "123-456-7890")
        self.assertEqual(self.operator._email, "johndoe@example.com")
        self.assertEqual(self.operator._address, "123 Main St")
        self.assertEqual(self.operator._document_type, "DNI")
    
    def test_validate_address_not_empty(self):
        """Test that the validate method returns True when the address is not empty."""
        self.assertTrue(self.operator.validate())

    def test_validate_address_empty(self):
        """Test that the validate method returns False when the address is empty."""
        self.operator._address = ""
        self.assertFalse(self.operator.validate())
    
    def test_get_information(self):
        """Test that the get_information method returns the expected string."""
        expected_info = (
            "ID: 1\n-Document Type: DNI\n-Document: 12345678\n-Name: John Doe"
            "\n-Phone 123-456-7890\n-Email: johndoe@example.com\n-Address123 Main St."
        )
        self.assertEqual(self.operator.get_information(), expected_info)

if __name__ == "__main__":
    unittest.main()