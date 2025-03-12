import unittest
from src.package_classifier import PackageClassifier

class TestPackageClassifier(unittest.TestCase):

    def test_classify(self):
        """Prueba la clasificación de paquetes según su peso."""
        self.assertEqual(PackageClassifier.classify(0.5), "basic")       # Peso menor a 1
        self.assertEqual(PackageClassifier.classify(1), "standard")      # Peso en el límite inferior de standard
        self.assertEqual(PackageClassifier.classify(3), "standard")      # Peso dentro del rango estándar
        self.assertEqual(PackageClassifier.classify(5), "standard")      # Peso en el límite superior de standard
        self.assertEqual(PackageClassifier.classify(6), "oversized")     # Peso mayor a 5

    def test_calculate_cost(self):
        """Prueba el cálculo de costo de envío según peso y tipo de paquete."""
        self.assertEqual(PackageClassifier.calculate_cost(0.5, "basic"), 5.0)        # Básico siempre es 5.0
        self.assertEqual(PackageClassifier.calculate_cost(3, "standard"), 10.35)       # 5.0 * 1.5
        self.assertEqual(PackageClassifier.calculate_cost(6, "oversized"), 21.2)     # 5.0 * 2 + (6 * 0.5)

if __name__ == "__main__":
    unittest.main()
