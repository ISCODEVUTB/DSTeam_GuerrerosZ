import unittest
import sys
import os
from unittest.mock import Mock

# Agregar 'src' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar después de modificar sys.path
from src.invoice import Invoice
from src.payment_method import PaymentMethod

class TestInvoice(unittest.TestCase):
    def setUp(self):
        """Setup: Creates an Invoice with mocked Shipments."""
        self.mock_shipment1 = Mock()
        self.mock_shipment1.total_cost = 50.0

        self.mock_shipment2 = Mock()
        self.mock_shipment2.total_cost = 75.0

        self.shipments = [self.mock_shipment1, self.mock_shipment2]
        self.invoice = Invoice(invoice_id=101, shipments=self.shipments)

    def test_generate_invoice(self):
        """Test that generate_invoice() returns the expected string."""
        expected_output = "Invoice 101 generated for 125.0 USD"
        self.assertEqual(self.invoice.generate_invoice(), expected_output)

    def test_process_payment(self):
        """Test that process_payment() calls the correct method on PaymentMethod."""
        mock_payment_method = Mock(spec=PaymentMethod)
        mock_payment_method.process_payment.return_value = "Payment of 125.0 USD processed"

        result = self.invoice.process_payment(mock_payment_method)

        mock_payment_method.process_payment.assert_called_once_with(125.0)
        self.assertEqual(result, "Payment of 125.0 USD processed")

if __name__ == "__main__":
    unittest.main()
