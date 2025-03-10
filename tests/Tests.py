import unittest
from src import client, package, shipment, invoice, paymentmethod, cardpayment, paypalpayment, cashpayment, managementSystem,packageclassifier

class TestManagementSystem(unittest.TestCase):
    def setUp(self):
        """Initial setup of objects required for testing."""
        self.client1 = client(1, "Juan Perez", "12345678", "987654321", "juan@example.com", "Street 123", "ID")
        self.client2 = client(2, "Maria Gomez", "87654321", "123456789", "maria@example.com", "Avenue 456", "ID")
        self.package1 = package(1, "10x10x10", 2.0, "Fragile")
        self.package2 = package(2, "20x20x20", 6.0, "Heavy")
        self.system = managementSystem()

    def test_register_client(self):
        """Test the registration of clients in the system."""
        self.system.register_client(self.client1)
        self.assertIn(self.client1, self.system.clients)

    def test_add_package(self):
        """Test the addition of packages to the system."""
        self.system.add_package(self.package1)
        self.assertIn(self.package1, self.system.packages)

    def test_approve_package(self):
        """Test the approval of a package before shipping."""
        self.system.add_package(self.package1)
        self.assertFalse(self.package1.approved)  # Verify that the package is not approved initially
        self.system.approve_package(1)
        self.assertTrue(self.package1.approved)  # Verify that the package has been approved

    def test_create_shipment(self):
        """Test the creation of a shipment only with approved packages."""
        self.system.register_client(self.client1)
        self.system.register_client(self.client2)
        self.system.add_package(self.package1)
        self.system.approve_package(1)
        self.system.create_shipment(1, self.client1, self.client2, [1])
        self.assertEqual(len(self.system.shipments), 1)  # Verify that the shipment was created correctly

    def test_track_shipment(self):
        """Test the tracking of a shipment."""
        self.system.register_client(self.client1)
        self.system.register_client(self.client2)
        self.system.add_package(self.package1)
        self.system.approve_package(1)
        self.system.create_shipment(1, self.client1, self.client2, [1])
        status = self.system.track_shipment(1)
        self.assertIsInstance(status, list)  # Verify that tracking returns a list of statuses

    def test_generate_invoice(self):
        """Test the generation of an invoice."""
        self.system.register_client(self.client1)
        self.system.register_client(self.client2)
        self.system.add_package(self.package1)
        self.system.approve_package(1)
        self.system.create_shipment(1, self.client1, self.client2, [1])
        invoice = self.system.generate_invoice(1, [1])
        self.assertIn("Invoice", invoice)  # Verify that the text "Invoice" is present in the output


unittest.main()
