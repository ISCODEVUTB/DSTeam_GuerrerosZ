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

    def creacion_cliente(self):
        cliente = cl.Cliente(1, "Juan Pérez", "12345678", "987654321", "juan@email.com", "Calle Falsa 123", "DNI")
        self.assertEqual(cliente.id_cliente, 1)
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.documento, "12345678")
        self.assertEqual(cliente.celular, "987654321")
        self.assertEqual(cliente.correo, "juan@email.com")
        self.assertEqual(cliente.direccion, "Calle Falsa 123")
        self.assertEqual(cliente.tipo_documento, "DNI")

class Testclasificar (unittest.TestCase):
    def test_clasificar_basico(self):
        self.assertEqual(cl.ClasificadorPaquete.clasificar(-1), "básico") #Caso negativo
        self.assertEqual(cl.ClasificadorPaquete.clasificar(0.5), "básico") #Caso estandar 
        self.assertEqual(cl.ClasificadorPaquete.clasificar(0.999), "básico") #Caso limite

    def test_clasificar_estandar(self):
        self.assertEqual(cl.ClasificadorPaquete.clasificar(1), "estándar") # Caso limite
        self.assertEqual(cl.ClasificadorPaquete.clasificar(3), "estándar") # Caso estandar
        self.assertEqual(cl.ClasificadorPaquete.clasificar(5), "estándar")  # Caso limite

    def test_clasificar_dimensionado(self):
        self.assertEqual(cl.ClasificadorPaquete.clasificar(5.01), "dimensionado") # Caso limite
        self.assertEqual(cl.ClasificadorPaquete.clasificar(10), "dimensionado") # Caso estandar

class Testcalcular_costo (unittest.TestCase):
    def test_costo_basico(self):
        self.assertEqual(cl.ClasificadorPaquete.calcular_costo(0.5, "básico"), 5.0) # Caso basico

    def test_costo_estandar(self):
        self.assertEqual(cl.ClasificadorPaquete.calcular_costo(2, "estándar"), 7.5)

    def test_costo_dimensionado(self):
        var=5.01
        self.assertEqual(cl.ClasificadorPaquete.calcular_costo(5.01, "dimensionado"), (10+(var*0.5)))

class TestPaquete(unittest.TestCase):

    def test_creacion_paquete(self):
        """Prueba la creación de un paquete y sus valores iniciales"""
        paquete = cl.Paquete(1, "30x30x30", 3.0, "Frágil")

        self.assertEqual(paquete.id_paquete, 1) # Verificar el id del paquete
        #self.assertEqual(paquete.tipo, cl.ClasificadorPaquete.clasificar(3.0)) # Verificar en la noche
        self.assertEqual(paquete.costo_envio, cl.ClasificadorPaquete.calcular_costo(3.0, "estándar")) # verificar el costo del envio
        self.assertFalse(paquete.aprobado) # verificar si el paquete esta aprobado

    def test_actualizar_info(self):
        paquete = cl.Paquete(2, "20x20x20", 0.5, "Pequeño") 
        paquete.actualizar_info("40x40x40", 6.0, "Pesado") 
        self.assertEqual(paquete.costo_envio, cl.ClasificadorPaquete.calcular_costo(6.0, "dimensionado")) # Verificar el costo del envio
        self.assertEqual(paquete.dimensiones, "40x40x40") # Verificar las dimensiones
        self.assertEqual(paquete.peso, 6.0) # Verificar el peso
    def test_aprobar_paquete(self):
        paquete = cl.Paquete(3, "50x50x50", 2.0, "Normal")
        self.assertFalse(paquete.aprobado)  # Antes de aprobarlo
        paquete.aprobar()
        self.assertTrue(paquete.aprobado)  # Después de aprobarlo

unittest.main()
