import clases
import re
from typing import Optional, List

class Terminal:
    def __init__(self):
        self.__sistemaGestion = clases.SistemaGestion()
        self.__conjuntoCredencialesOperarios = [("operario1", "12345")]

    def mostrar_mensaje_principal(self):
        print("Mensaje texto plano mensaje de entrada")

    def autenticar_credencial(self, token_usuario: str, token_contraseña: str) -> bool:
        return (token_usuario, token_contraseña) in self.__conjuntoCredencialesOperarios

    def solicitar_info_remitente(self) -> clases.Cliente:
        return self.__solicitar_info_cliente("remitente")

    def solicitar_info_destinatario(self) -> clases.Cliente:
        return self.__solicitar_info_cliente("destinatario")

    def __solicitar_info_cliente(self, tipo: str) -> clases.Cliente:
        """Solicita la información de un cliente (remitente o destinatario) con validación de datos"""
        print(f"\n📌 Ingrese los datos del {tipo}:")

        def validar_numero(mensaje: str) -> int:
            while True:
                try:
                    valor = int(input(mensaje).strip())
                    if valor > 0:
                        return valor
                    print("❌ Error: Debe ingresar un número positivo.")
                except ValueError:
                    print("❌ Entrada inválida. Ingrese un número válido.")

        id_cliente = validar_numero("Ingrese ID del cliente: ")

        def validar_texto(mensaje: str) -> str:
            while True:
                texto = input(mensaje).strip()
                if texto:
                    return texto
                print("❌ Error: El campo no puede estar vacío.")

        def validar_opcion(mensaje, opciones_validas):
            while True:
                opcion = input(mensaje).strip().upper()
                if opcion in opciones_validas:
                    return opcion
                print(f"❌ Opción inválida. Debe ser una de: {', '.join(opciones_validas)}.")

        tipo_cedula = validar_opcion("Ingrese tipo de cédula (CC/CE/PAS): ", ["CC", "CE", "PAS"])
        cedula = validar_texto("Ingrese cédula: ")
        nombre = validar_texto("Ingrese nombre: ")
        celular = validar_texto("Ingrese celular: ")
        correo = validar_texto("Ingrese correo: ")
        direccion = validar_texto("Ingrese dirección: ")

        return clases.Cliente(id_cliente, nombre, cedula, celular, correo, direccion, tipo_cedula)

    def solicitar_info_paquete(self, n: int, id_paquete: int) -> List[clases.Paquete]:
        """Solicita la información de 'n' paquetes y los devuelve en una lista de objetos Paquete."""
        paquetes = []

        def validar_numero(mensaje: str) -> float:
            while True:
                try:
                    valor = float(input(mensaje).strip())
                    if valor > 0:
                        return valor
                    print("❌ Error: Debe ingresar un número positivo.")
                except ValueError:
                    print("❌ Entrada inválida. Ingrese un número válido.")

        for _ in range(n):
            print("\n📦 Ingrese los datos del paquete:")
            id_paquete += 1  # Incrementa correctamente en cada iteración
            peso = validar_numero("Ingrese el peso del paquete (kg): ")
            largo = validar_numero("Ingrese el largo del paquete (cm): ")
            ancho = validar_numero("Ingrese el ancho del paquete (cm): ")
            alto = validar_numero("Ingrese el alto del paquete (cm): ")
            dimensiones = f"{largo},{ancho},{alto}"
            observaciones = input("Ingrese observaciones del paquete (opcional): ").strip()

            paquete = clases.Paquete(id_paquete, dimensiones, peso, observaciones)
            paquetes.append(paquete)

        print(f"\n✅ Se han registrado {n} paquetes correctamente.")
        return paquetes

    def crear_envio(self) -> str:
        """Crea un nuevo envío con datos ingresados por el usuario"""
        remitente = self.solicitar_info_remitente()
        destinatario = self.solicitar_info_destinatario()
        num_paquetes = int(input("Ingrese la cantidad de paquetes: "))
        lista_paquetes = self.solicitar_info_paquete(num_paquetes, id_paquete=len(self.__sistemaGestion.paquetes))

        self.__sistemaGestion.registrar_cliente(remitente)
        self.__sistemaGestion.registrar_cliente(destinatario)

        for paquete in lista_paquetes:
            self.__sistemaGestion.agregar_paquete(paquete)

        observacion = input("Ingrese observaciones para el envío (opcional): ").strip()

        nuevo_id_envio = len(self.__sistemaGestion.envios) + 1  # Genera un nuevo ID de envío único
        envio = self.__sistemaGestion.crear_envio(nuevo_id_envio, remitente, destinatario, [p.id_paquete for p in lista_paquetes], observacion)

        print("\n📦 Envío creado exitosamente.")
        return envio

