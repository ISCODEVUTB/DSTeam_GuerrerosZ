import unittest
import sys
import os

# Agregar 'src' al path para importar las clases correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.client import Client  

class TestClient(unittest.TestCase):
    def setUp(self):
        """Setup: Creates a Client object before each test."""
        self.client = Client(
            client_id=1, 
            name="John Doe", 
            document="123456789", 
            phone="555-1234", 
            email="johndoe@email.com", 
            address="123 Main St", 
            document_type="CC"
        )

    def test_validate_with_address(self):
        """Test that validate() returns True when the address is not empty."""
        self.assertTrue(self.client.validate())

    def test_validate_with_empty_address(self):
        """Test that validate() returns False when the address is empty."""
        self.client.address = " "  # Simulating an empty address
        self.assertFalse(self.client.validate())

    def test_get_information_format(self):
        """Test that get_information() returns a correctly formatted string."""
        expected_output = (
            "ID: 1\n-Document Type: CC\n-Document: 123456789"
            "\n-Name: John Doe\n-Phone 555-1234\n-Email: johndoe@email.com"
            "\n-Address123 Main St."
        )
        self.assertEqual(self.client.get_information(), expected_output)

if __name__ == "__main__":
    unittest.main()
