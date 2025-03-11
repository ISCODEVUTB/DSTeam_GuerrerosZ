import unittest
from unittest.mock import Mock, patch
from src.operator import Operator
class TestOperator(unittest.TestCase):
    
    def setUp(self):
        self.mock_package1 = Mock()
        self.mock_package2 = Mock()
        self.mock_shipment = Mock()
        self.mock_shipment.total_cost = 50.0  # Asegurar que tiene este atributo
        self.mock_sender = Mock()
        self.mock_recipient = Mock()
        self.system = Operator()
    
    def test_approve_package(self):
        self.mock_package1.approve.reset_mock()
        self.system.approve_package(self.mock_package1)
        self.mock_package1.approve.assert_called_once()
    
    @patch('builtins.input', lambda _: "yes")
    def test_create_shipment(self):
        self.system.create_shipment(201, self.mock_sender, self.mock_recipient, [101], "Handle with care")
    
    def test_generate_invoice(self):
        invoice = self.system.generate_invoice(self.mock_shipment)
        self.assertIn("Total Cost: 50.0", invoice)
    
    def test_get_information(self):
        self.mock_operator = Operator("John Doe", "123456789", "ID")
        expected_output = "ID: 1\n- Document Type: ID\n- Document: 123456789"
        self.assertEqual(self.mock_operator.get_information().strip(), expected_output.strip())
    
    def test_validate(self):
        operator = Operator("John Doe", "123456789", "ID")
        self.assertTrue(operator.validate())
    
    @patch.object(Operator, 'calculate_cost')
    def test_update_info(self, mock_calculate_cost):
        mock_calculate_cost.return_value = 10.0
        self.system.update_info(self.mock_shipment)
        mock_calculate_cost.assert_called_once_with(10.0, "Standard")
    
    def test_calculate_cost(self):
        result = self.system.calculate_cost(10.0, "Standard")
        self.assertEqual(result, 17.0)  # Ajustado al valor esperado correcto

if __name__ == '__main__':
    unittest.main()
