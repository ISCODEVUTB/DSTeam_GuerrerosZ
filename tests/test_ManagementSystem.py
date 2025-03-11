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
        mock_package.package_id = 1  # Asignamos un ID al paquete
        self.system.add_package(mock_package)
        self.assertIn(mock_package, self.system.packages)
        mock_package.approve.assert_called_once()

    @patch("builtins.input", return_value="yes")  # Simula aprobación de paquetes
    def test_create_shipment(self, mock_input):
        sender = Client(1, "Alice", "12345678", "555-1234", "alice@example.com", "123 Main St", "DNI")
        recipient = Client(2, "Bob", "87654321", "555-5678", "bob@example.com", "456 Elm St", "DNI")
        package = Package(1, "10x10x10", 5.0, "Test Package")
        package.approve()  # Aprobamos el paquete manualmente

        self.system.packages.append(package)  # Agregamos el paquete al sistema
        self.system.create_shipment(1, sender, recipient, [1], "Test Shipment")

        # Verificamos que el envío real esté en el sistema
        self.assertTrue(any(s.shipment_id == 1 for s in self.system.shipments))
    def test_generate_invoice(self):
        # Creamos un paquete y lo aprobamos
        package = Package(1, "10x10x10", 5.0, "Test Package")
        package.approve()  # ¡Importante! Aprobamos el paquete antes de usarlo.

        # Creamos el envío con paquetes aprobados
        shipment = Shipment(
            shipment_id=1,
            sender=Client(1, "Alice", "12345678", "555-1234", "alice@example.com", "123 Main St", "DNI"),
            recipient=Client(2, "Bob", "87654321", "555-5678", "bob@example.com", "456 Elm St", "DNI"),
            packages=[package],  # Se usa el paquete aprobado
            observation="Test Invoice"
        )

        self.system.shipments.append(shipment)  # Agregamos el envío al sistema
        result = self.system.generate_invoice(1, [1])

        expected_invoice_text = f"Invoice 1 generated for {shipment.total_cost} USD"
        self.assertEqual(result, expected_invoice_text)  # Comparamos con el resultado esperado

        # Verificamos que la factura se haya guardado en el sistema
        self.assertTrue(any(i.invoice_id == 1 for i in self.system.invoices))

if __name__ == "__main__":
    unittest.main()
