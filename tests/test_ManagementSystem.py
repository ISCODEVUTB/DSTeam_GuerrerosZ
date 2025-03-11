import unittest
import sys
import os
from unittest.mock import Mock
from typing import List

# Agregar 'src' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar después de modificar sys.path
from src.managementSystem import ManagementSystem
from src.client import Client
from src.package import Package
from src.shipment import Shipment
from src.invoice import Invoice

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        """Setup: Crea un ManagementSystem con clientes, paquetes y envíos simulados."""
        self.system = ManagementSystem()

        # Simular Clientes
        self.mock_sender = Mock(spec=Client)
        self.mock_sender.client_id = 1
        self.mock_recipient = Mock(spec=Client)
        self.mock_recipient.client_id = 2

        # Simular Paquetes
        self.mock_package1 = Mock(spec=Package)
        self.mock_package1.package_id = 101
        self.mock_package2 = Mock(spec=Package)
        self.mock_package2.package_id = 102

        # Simular Envíos
        self.mock_shipment = Mock(spec=Shipment)
        self.mock_shipment.shipment_id = 201
        self.mock_shipment.track_shipment.return_value = ["In transit", "Delivered"]

        # Simular Factura
        self.mock_invoice = Mock(spec=Invoice)
        self.mock_invoice.invoice_id = 301
        self.mock_invoice.generate_invoice.return_value = "Invoice 301 generated for 100 USD"

    def test_register_client(self):
        """Prueba que un cliente se registre correctamente."""
        self.system.register_client(self.mock_sender)
        self.assertIn(self.mock_sender, self.system.clients)

    def test_add_package(self):
        """Prueba que un paquete se agregue correctamente."""
        self.system.add_package(self.mock_package1)
        self.assertIn(self.mock_package1, self.system.packages)

    def test_update_package(self):
        """Prueba que un paquete se actualice correctamente."""
        self.system.add_package(self.mock_package1)
        self.mock_package1.update_info.return_value = True
        result = self.system.update_package(101, "10x10x10", 2.5, "Fragile")
        self.mock_package1.update_info.assert_called_once_with("10x10x10", 2.5, "Fragile")
        self.assertTrue(result)

    def test_approve_package(self):
        """Prueba que un paquete sea aprobado correctamente."""
        self.system.add_package(self.mock_package1)
        self.mock_package1.approve.return_value = True
        result = self.system.approve_package(101)
        self.mock_package1.approve.assert_called_once()
        self.assertTrue(result)

    def test_create_shipment(self):
        """Prueba la creación de un envío."""
        self.system.add_package(self.mock_package1)
        self.system.create_shipment(201, self.mock_sender, self.mock_recipient, [101])
        self.assertEqual(len(self.system.shipments), 1)

    def test_track_shipment(self):
        """Prueba el rastreo de un envío."""
        self.system.shipments.append(self.mock_shipment)
        result = self.system.track_shipment(201)
        self.assertEqual(result, ["In transit", "Delivered"])

    def test_generate_invoice(self):
        """Prueba la generación de una factura."""
        self.system.shipments.append(self.mock_shipment)
        result = self.system.generate_invoice(301, [201])
        self.assertEqual(result, "Invoice 301 generated for 100 USD")

if __name__ == "__main__":
    unittest.main()