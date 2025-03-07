import unittest
from src.classes.Package import Package
from src.classes.PackageClassifier import PackageClassifier
from unittest.mock import patch

class TestPackage(unittest.TestCase):
    def setUp(self):
        """Setup: Crea un paquete con atributos de prueba."""
        self.package = Package(
            package_id=1,
            dimensions="10x10x10",
            weight=5.0,
            observations="Fragile"
        )

    @patch.object(PackageClassifier, 'classify', return_value="Standard")
    @patch.object(PackageClassifier, 'calculate_cost', return_value=10.0)
    def test_update_info(self, mock_classify, mock_calculate_cost):
        """Prueba que la actualización de información del paquete funcione correctamente."""
        self.package.update_info("20x20x20", 10.0, "Handle with care")

        self.assertEqual(self.package.dimensions, "20x20x20")
        self.assertEqual(self.package.weight, 10.0)
        self.assertEqual(self.package.observations, "Handle with care")
        self.assertEqual(self.package.type, "Standard")
        self.assertEqual(self.package.shipping_cost, 10.0)

        mock_classify.assert_called_once_with(10.0)
        mock_calculate_cost.assert_called_once_with(10.0, "Standard")

    def test_approve(self):
        """Prueba que `approve()` cambia correctamente el estado del paquete."""
        self.assertFalse(self.package.approved)  # Antes de aprobar
        self.package.approve()
        self.assertTrue(self.package.approved)   # Después de aprobar

if __name__ == "__main__":
    unittest.main()
