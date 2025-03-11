import unittest
from unittest.mock import Mock, patch
from src.managementSystem import ManagementSystem
from src.client import Client
from src.package import Package
from src.shipment import Shipment
from src.invoice import Invoice

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        self.system = ManagementSystem()

    @patch("src.managementSystem.Client")
    def test_add_client(self, MockClient):
        mock_client = MockClient.return_value
        self.system.add_client(mock_client)
        self.assertIn(mock_client, self.system.clients)

    @patch("src.managementSystem.Package")
    def test_add_package(self, MockPackage):
        mock_package = MockPackage.return_value
        self.system.add_package(mock_package)
        self.assertIn(mock_package, self.system.packages)

    @patch("src.managementSystem.Shipment")
    def test_create_shipment(self, MockShipment):
        mock_shipment = MockShipment.return_value
        sender = Mock()
        recipient = Mock()
        packages = [Mock()]
        self.system.create_shipment(1, sender, recipient, packages, "Test Shipment")
        self.assertIn(mock_shipment, self.system.shipments)

    @patch("src.managementSystem.Invoice")
    def test_generate_invoice(self, MockInvoice):
        mock_invoice = MockInvoice.return_value
        shipments = [Mock()]
        invoice = self.system.generate_invoice(1, shipments)
        self.assertEqual(invoice, mock_invoice)
        self.assertIn(mock_invoice, self.system.invoices)

if __name__ == "__main__":
    unittest.main()
