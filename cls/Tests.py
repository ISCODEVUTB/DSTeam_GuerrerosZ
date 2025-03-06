import unittest
import clases as cl  # Importamos todas las clases del módulo cls

class TestSistemaGestion(unittest.TestCase):
    def setUp(self):
        """Configuración inicial de los objetos necesarios para las pruebas."""
        self.cliente1 = cl.Cliente(1, "Juan Perez", "12345678", "987654321", "juan@example.com", "Calle 123", "DNI")
        self.cliente2 = cl.Cliente(2, "Maria Gomez", "87654321", "123456789", "maria@example.com", "Avenida 456", "DNI")
        self.paquete1 = cl.Paquete(1, "10x10x10", 2.0, "Frágil")
        self.paquete2 = cl.Paquete(2, "20x20x20", 6.0, "Pesado")
        self.sistema = cl.SistemaGestion()

    def test_registrar_cliente(self):
        """Prueba el registro de clientes en el sistema."""
        self.sistema.registrar_cliente(self.cliente1)
        self.assertIn(self.cliente1, self.sistema.clientes)

    def test_agregar_paquete(self):
        """Prueba la adición de paquetes al sistema."""
        self.sistema.agregar_paquete(self.paquete1)
        self.assertIn(self.paquete1, self.sistema.paquetes)

    def test_aprobar_paquete(self):
        """Prueba la aprobación de un paquete antes del envío."""
        self.sistema.agregar_paquete(self.paquete1)
        self.assertFalse(self.paquete1.aprobado)  # Verifica que el paquete no está aprobado inicialmente
        self.sistema.aprobar_paquete(1)
        self.assertTrue(self.paquete1.aprobado)  # Verifica que el paquete ha sido aprobado

    def test_crear_envio(self):
        """Prueba la creación de un envío solo con paquetes aprobados."""
        self.sistema.registrar_cliente(self.cliente1)
        self.sistema.registrar_cliente(self.cliente2)
        self.sistema.agregar_paquete(self.paquete1)
        self.sistema.aprobar_paquete(1)
        self.sistema.crear_envio(1, self.cliente1, self.cliente2, [1])
        self.assertEqual(len(self.sistema.envios), 1)  # Verifica que el envío fue creado correctamente

    def test_rastrear_envio(self):
        """Prueba el rastreo de un envío."""
        self.sistema.registrar_cliente(self.cliente1)
        self.sistema.registrar_cliente(self.cliente2)
        self.sistema.agregar_paquete(self.paquete1)
        self.sistema.aprobar_paquete(1)
        self.sistema.crear_envio(1, self.cliente1, self.cliente2, [1])
        estado = self.sistema.rastrear_envio(1)
        self.assertIsInstance(estado, list)  # Verifica que el rastreo devuelve una lista de estados

    def test_generar_factura(self):
        """Prueba la generación de una factura."""
        self.sistema.registrar_cliente(self.cliente1)
        self.sistema.registrar_cliente(self.cliente2)
        self.sistema.agregar_paquete(self.paquete1)
        self.sistema.aprobar_paquete(1)
        self.sistema.crear_envio(1, self.cliente1, self.cliente2, [1])
        factura = self.sistema.generar_factura(1, [1])
        self.assertIn("Factura", factura)  # Verifica que el texto "Factura" esté presente en la salida


unittest.main()
