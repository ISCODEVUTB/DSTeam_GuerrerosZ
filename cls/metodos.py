import clases
import re
from typing import Optional

class Terminal:
    def __init__(self):
        self.__sistemaGestion = clases.SistemaGestion()
        self.__conjuntoCredencialesOperarios = [("operario1", "12345")]

    def mostrar_mensaje_principal(self):
        print("Mensaje texto plano mensaje de entrada")

    def autenticar_credencial(self, token_usuario: str, token_contraseña: str) -> bool:
        for usuario, contraseña in self.__conjuntoCredencialesOperarios:
            if usuario == token_usuario and contraseña == token_contraseña:
                return True
        return False

    def solicitar_info_remitente(self) -> clases.Cliente:
        return self.__solicitar_info_cliente("remitente")

    def solicitar_info_destinatario(self) -> clases.Cliente:
        return self.__solicitar_info_cliente("destinatario")

    def __solicitar_info_cliente(self, tipo: str) -> clases.Cliente:
        """Solicita la información de un cliente (remitente o destinatario)"""
        print(f"\nIngrese los datos del {tipo}:")

        def validar_opcion(mensaje, opciones_validas):
            while True:
                opcion = input(mensaje).strip().upper()
                if opcion in opciones_validas:
                    return opcion
                print(f"Opción inválida. Debe ser una de: {', '.join(opciones_validas)}.")

        def validar_cedula(mensaje):
            while True:
                cedula = input(mensaje).strip()
                if cedula.isdigit() and 7 <= len(cedula) <= 10:
                    return cedula
                print("Cédula inválida. Debe contener solo números y tener entre 7 y 10 dígitos.")

        def validar_nombre(mensaje):
            while True:
                nombre = input(mensaje).strip()
                if re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", nombre):
                    return nombre
                print("Nombre inválido. Debe contener solo letras y espacios.")

        def validar_celular(mensaje):
            while True:
                celular = input(mensaje).strip()
                if celular.isdigit() and len(celular) == 10:
                    return celular
                print("Celular inválido. Debe contener exactamente 10 dígitos numéricos.")

        def validar_correo(mensaje):
            while True:
                correo = input(mensaje).strip()
                if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
                    return correo
                print("Correo inválido. Debe ser un correo con formato correcto (ejemplo@dominio.com).")

        def validar_direccion(mensaje):
            while True:
                direccion = input(mensaje).strip()
                if direccion:
                    return direccion
                print("Dirección inválida. No puede estar vacía.")

        # Solicitar datos con validación
        tipo_cedula = validar_opcion("Ingrese tipo de cédula (CC/CE/PAS): ", ["CC", "CE", "PAS"])
        cedula = validar_cedula("Ingrese cédula: ")
        nombre = validar_nombre("Ingrese nombre: ")
        celular = validar_celular("Ingrese celular: ")
        correo = validar_correo("Ingrese correo: ")
        direccion = validar_direccion("Ingrese dirección: ")

        return clases.Cliente(tipo_cedula, cedula, nombre, celular, correo, direccion)

    def solicitar_info_paquete(self) -> clases.Paquete:
        """Solicita la información de un paquete y la devuelve como objeto Paquete."""

        def validar_numero(mensaje):
            """Solicita un número positivo (para peso, dimensiones)."""
            while True:
                try:
                    valor = float(input(mensaje).strip())
                    if valor > 0:
                        return valor
                    print("El valor debe ser un número positivo.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")

        def validar_texto(mensaje):
            """Solicita un texto no vacío."""
            while True:
                texto = input(mensaje).strip()
                if texto:
                    return texto
                print("El campo no puede estar vacío.")

        def validar_opcion(mensaje, opciones_validas):
            """Solicita una opción y valida que esté dentro de las permitidas."""
            while True:
                opcion = input(mensaje).strip().upper()
                if opcion in opciones_validas:
                    return opcion
                print(f"Opción inválida. Debe ser una de: {', '.join(opciones_validas)}.")

        print("\nIngrese los datos del paquete:")

        peso = validar_numero("Ingrese el peso del paquete (kg): ")
        largo = validar_numero("Ingrese el largo del paquete (cm): ")
        ancho = validar_numero("Ingrese el ancho del paquete (cm): ")
        dimensiones = str(largo + "," + ancho)
        alto = validar_numero("Ingrese el alto del paquete (cm): ")
        observaciones = validar_texto("Ingrese observaciones del paquete: ")   







    def crear_envio(self) -> str:
        remitente = self.solicitar_info_remitente()
        destinatario = self.solicitar_info_destinatario()
        self.__sistemaGestion.registrar_cliente(remitente)
        self.__sistemaGestion.registrar_cliente(destinatario)

        envio = self.__sistemaGestion.crear_envio(remitente, destinatario)
        
        print("\n📦 Envío creado exitosamente.")
        return envio
