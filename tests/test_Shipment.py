import unittest
from src.classes.Client import Client
from src.classes.Package import Package
from src.classes.Shipment import Shipment

class TestShipment(unittest.TestCase):

    def setUp(self):
        """Crea instancias de Client y Package para pruebas."""
        self.sender = Client(1, "Alice", "987654", "555-5678", "alice@example.com", "456 Elm St", "Passport")
        self.recipient = Client(2, "Bob", "654321", "555-9876", "bob@example.com", "789 Oak St", "Driver's License")

        self.package1 = Package(101, "10x10x10", 2.0, "Fragile")
        self.package2 = Package(102, "15x15x15", 3.5, "Handle with care")
        
        self.package1.approve()
        self.package2.approve()

    def test_shipment_creation(self):
        """Verifica que un envío se cree correctamente si los paquetes están aprobados."""
        shipment = Shipment(1, self.sender, self.recipient, [self.package1, self.package2], "Express delivery")
        self.assertEqual(shipment.shipment_id, 1)
        self.assertEqual(shipment.total_cost, self.package1.shipping_cost + self.package2.shipping_cost)
        self.assertIn("Shipment created", shipment.track_shipment())

    def test_shipment_creation_with_unapproved_package(self):
        """Verifica que se genere un error si hay un paquete no aprobado."""
        unapproved_package = Package(103, "20x20x20", 5.0, "Heavy item")
        with self.assertRaises(ValueError) as context:
            Shipment(2, self.sender, self.recipient, [unapproved_package], "Standard delivery")
        self.assertIn("All packages must be approved", str(context.exception))

    def test_shipment_creation_with_invalid_recipient(self):
        """Verifica que se genere un error si el destinatario no tiene dirección válida."""
        self.recipient.address = "  "  # Dirección inválida
        with self.assertRaises(ValueError) as context:
            Shipment(3, self.sender, self.recipient, [self.package1], "Standard delivery")
        self.assertIn("Recipient's address is invalid", str(context.exception))

    def test_update_tracking(self):
        """Verifica que el seguimiento del envío se actualiza correctamente."""
        shipment = Shipment(4, self.sender, self.recipient, [self.package1], "Standard delivery")
        shipment.update_status("In transit")
        shipment.update_status("Delivered")
        self.assertEqual(shipment.track_shipment(), ["Shipment created", "In transit", "Delivered"])

if __name__ == "__main__":
    unittest.main()
