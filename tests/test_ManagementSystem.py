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

    @patch("src.client.Client")
    def test_register_client(self, MockClient):
        mock_client = MockClient.return_value
        self.system.register_client(mock_client)
        self.assertIn(mock_client, self.system.clients)

    @patch("src.package.Package")
    def test_add_package(self, MockPackage):
        mock_package = MockPackage.return_value
        self.system.add_package(mock_package)
        self.assertIn(mock_package, self.system.packages)
        mock_package.approve.assert_called_once()

    @patch("builtins.input", return_value="yes")  # Simular aprobación automática
    @patch("src.shipment.Shipment")
    def test_create_shipment(self, MockShipment, mock_input):
        mock_shipment = MockShipment.return_value
        sender = Mock(spec=Client)
        recipient = Mock(spec=Client)
        recipient.validate.return_value = True
        package = Mock(spec=Package)
        package.package_id = 1
        package.approved = True  
        self.system.packages.append(package)

        self.system.create_shipment(1, sender, recipient, [1], "Test Shipment")
        self.assertIn(mock_shipment, self.system.shipments)

    @patch("src.invoice.Invoice")
    def test_generate_invoice(self, MockInvoice):
        mock_invoice = MockInvoice.return_value
        shipment = Mock(spec=Shipment)
        shipment.shipment_id = 1
        shipment.total_cost = 100  # Agregar el atributo necesario
        self.system.shipments.append(shipment)  

        result = self.system.generate_invoice(1, [1])
        self.assertEqual(result, mock_invoice.generate_invoice.return_value)
        self.assertIn(mock_invoice, self.system.invoices)

if __name__ == "__main__":
    unittest.main()
