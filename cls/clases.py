from abc import ABC, abstractmethod
from typing import List, Optional

# Clase base para validaciones
class Validable(ABC):
    """
    Clase base abstracta para objetos validables.
    """
    @abstractmethod
    def validar(self) -> bool:
        pass


class Persona(ABC):
    """
    Clase base abstracta para representar a una persona con información básica.
    """
    def __init__(self, id_persona: int, nombre: str, documento: str, celular: str, 
                 correo: str, direccion: str, tipo_documento: str):
        """
        Inicializa los atributos comunes de una persona.
        """
        self._id_persona = id_persona
        self._nombre = nombre
        self._tipo_documento = tipo_documento
        self._documento = documento
        self._celular = celular
        self._correo = correo
        self.direccion = direccion

    @abstractmethod
    def obtenerinformacion(self) -> str:
        """
        Retorna la información de la persona en formato de cadena de texto.
        """
        return (f"ID: {self.id_persona}\n-Tipo Documento: {self.tipo_documento}"
                f"\n-Documento: {self.documento}\n-Nombre: {self.nombre}"
                f"\n-Celular {self.celular}\n-Correo: {self.correo}"
                f"\n-Direccion{self.direccion}.")


class Cliente(Persona):
    """
    Representa a un cliente, heredando de la clase Persona.
    """
    def __init__(self, id_cliente: int, nombre: str, documento: str, celular: str, 
                 correo: str, direccion: str, tipo_documento: str):
        """
        Inicializa los atributos del cliente.
        """
        super().__init__(id_cliente, nombre, documento, celular, correo, direccion, tipo_documento)

    def validar(self) -> bool:
        """
        Valida que la dirección del cliente no esté vacía.
        """
        return bool(self.direccion.strip())

    def obtenerinformacion(self) -> str:
        """
        Retorna la información del cliente.
        """
        return (f"ID: {self.id_persona}\n-Tipo Documento: {self.tipo_documento}"
                f"\n-Documento: {self.documento}\n-Nombre: {self.nombre}"
                f"\n-Celular {self.celular}\n-Correo: {self.correo}"
                f"\n-Direccion{self.direccion}.")


class Operario(Persona):
    """
    Representa a un operario con credenciales de autenticación.
    """
    def __init__(self, token_usuario: str, token_password: str, id_cliente: int, 
                 nombre: str, documento: str, celular: str, correo: str, 
                 direccion: str, tipo_documento: str):
        """
        Inicializa los atributos del operario.
        """
        super().__init__(id_cliente, nombre, documento, celular, correo, direccion, tipo_documento)
        self._token_usuario = token_usuario
        self._token_password = token_password

    def validar(self) -> bool:
        """
        Valida que la dirección del operario no esté vacía.
        """
        return bool(self.__direccion.strip())

    def obtenerinformacion(self) -> str:
        """
        Retorna la información del operario.
        """
        return (f"ID: {self.id_persona}\n-Tipo Documento: {self.tipo_documento}"
                f"\n-Documento: {self.documento}\n-Nombre: {self.nombre}"
                f"\n-Celular {self.celular}\n-Correo: {self.correo}"
                f"\n-Direccion{self.direccion}.")


class ClasificadorPaquete:
    """
    Proporciona métodos para clasificar paquetes según su peso y calcular costos de envío.
    """
    @staticmethod
    def clasificar(peso: float) -> str:
        """
        Determina el tipo de paquete según su peso.
        """
        if peso < 1:
            return "básico"
        elif 1 <= peso <= 5:
            return "estándar"
        return "dimensionado"

    @staticmethod
    def calcular_costo(peso: float, tipo: str) -> float:
        """
        Calcula el costo de envío basado en el peso y tipo de paquete.
        """
        base = 5.0
        if tipo == "básico":
            return base
        if tipo == "estándar":
            return base * 1.5
        return base * 2 + (peso * 0.5)


class Paquete:
    """
    Representa un paquete con dimensiones, peso y estado de aprobación.
    """
    def __init__(self, id_paquete: int, dimensiones: str, peso: float, observaciones: str):
        """
        Inicializa un paquete y calcula automáticamente su tipo y costo de envío.
        """
        self.id_paquete = id_paquete
        self.dimensiones = dimensiones
        self.peso = peso
        self.observaciones = observaciones
        self.tipo = ClasificadorPaquete.clasificar(peso)
        self.aprobado = False
        self.costo_envio = ClasificadorPaquete.calcular_costo(peso, self.tipo)

    def actualizar_info(self, dimensiones: str, peso: float, observaciones: str):
        """
        Actualiza la información del paquete y recalcula su tipo y costo de envío.
        """
        self.dimensiones = dimensiones
        self.peso = peso
        self.observaciones = observaciones
        self.tipo = ClasificadorPaquete.clasificar(peso)
        self.costo_envio = ClasificadorPaquete.calcular_costo(peso, self.tipo)

    def aprobar(self):
        """
        Aprueba el paquete para su envío.
        """
        self.aprobado = True


class Envio:
    """
    Representa un envío con información de remitente, destinatario y paquetes asociados.
    """
    def __init__(self, id_envio: int, remitente: Cliente, destinatario: Cliente, 
                 paquetes: List[Paquete], observacion: str):
        """
        Inicializa un envío, asegurándose de que todos los paquetes estén aprobados.
        """
        if not all(p.aprobado for p in paquetes):
            raise ValueError("Todos los paquetes deben estar aprobados antes del envío")
        if not destinatario.validar():
            raise ValueError("Dirección del destinatario no válida")
        
        self.id_envio = id_envio
        self.remitente = remitente
        self.destinatario = destinatario
        self.paquetes = paquetes
        self.trazabilidad = []
        self.observaciones = observacion
        self.costo_total = sum(p.costo_envio for p in paquetes)
        self.actualizar_trazabilidad("Envío creado")

    def actualizar_estado(self, estado: str):
        """
        Agrega un nuevo estado a la trazabilidad del envío.
        """
        self.actualizar_trazabilidad(estado)

    def actualizar_trazabilidad(self, estado: str):
        """
        Agrega un estado a la lista de trazabilidad del envío.
        """
        self.trazabilidad.append(estado)

    def rastrear_envio(self) -> List[str]:
        """
        Retorna la lista de estados del envío.
        """
        return self.trazabilidad


class MetodoPago(ABC):
    """
    Clase abstracta para los métodos de pago.
    """
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        pass


class PagoTarjeta(MetodoPago):
    """
    Representa un pago realizado con tarjeta de crédito.
    """
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado con tarjeta de crédito."


class PagoPayPal(MetodoPago):
    """
    Representa un pago realizado con PayPal.
    """
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado con PayPal."


class PagoEfectivo(MetodoPago):
    """
    Representa un pago realizado en efectivo.
    """
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado en Sucursal."
