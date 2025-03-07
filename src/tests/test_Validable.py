import unittest
from src.classes.Validable import Validable

class TestValidable(unittest.TestCase):

    class MockValidable(Validable):
        """Clase de prueba que implementa `validate()`."""
        def __init__(self, valid: bool):
            self.valid = valid

        def validate(self) -> bool:
            return self.valid

    def test_valid_object(self):
        """Verifica que un objeto válido pase la validación."""
        obj = self.MockValidable(True)
        self.assertTrue(obj.validate())

    def test_invalid_object(self):
        """Verifica que un objeto inválido no pase la validación."""
        obj = self.MockValidable(False)
        self.assertFalse(obj.validate())

if __name__ == "__main__":
    unittest.main()
