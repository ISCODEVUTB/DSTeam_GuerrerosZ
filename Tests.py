import unittest
from cls import clases as cl

import unittest
from cls import clases as cl  # Importamos clases.py desde la carpeta cls

class TestCliente(unittest.TestCase):

    def test_cliente_valido(self):
        cliente = cl.Cliente(1, "Juan Pérez", "12345678", "987654321", "juan@email.com", "Calle Falsa 123", "DNI")
        self.assertTrue(cliente.validar())  # Debe ser verd.

    def test_cliente_sin_direccion(self):
        cliente = cl.Cliente(2, "Ana López", "87654321", "123456789", "ana@email.com", "   ", "DNI")
        self.assertFalse(cliente.validar())  # Debe ser False (solo espacios)

    def test_cliente_direccion_vacia(self):
        cliente = cl.Cliente(3, "Carlos Gómez", "13579246", "111222333", "carlos@email.com", "", "DNI")
        self.assertFalse(cliente.validar())  # Debe ser False


unittest.main()
