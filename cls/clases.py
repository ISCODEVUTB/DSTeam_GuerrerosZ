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
    def __init__(self, id_persona: int, nombre: str, documento: str, celular: str, correo: str, direccion: str, tipo_documento: str):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__tipo_documento = tipo_documento
        self.__documento = documento
        self.__celular = celular
        self.__correo = correo
        self.__direccion = direccion
    @abstractmethod
    def obtenerinformacion(self) ->str:
        return f"ID: {self.__id_persona}\n-Tipo Documento: {self.__tipo_documento}\n-Documento: {self.__documento}\n-Nombre: {self.__nombre}\n-Celular {self.__celular}\n-Correo: {self.__correo}\n-Direccion{self.__direccion}."


class Cliente(Persona):
    def __init__(self, id_cliente: int, nombre: str, documento: str, celular: str, correo: str, direccion: str, tipo_documento: str):
        super().__init__(id_cliente,nombre,documento,celular,correo,direccion,tipo_documento)

    def validar(self) -> bool:
        return bool(self.__direccion.strip())
    
    def obtenerinformacion(self) ->str:
        return f"ID: {self.__id_persona}\n-Tipo Documento: {self.__tipo_documento}\n-Documento: {self.__documento}\n-Nombre: {self.__nombre}\n-Celular {self.__celular}\n-Correo: {self.__correo}\n-Direccion{self.__direccion}."

class Operario(Persona):
    def __init__(self, token_usuario: str, token_password: str , id_cliente: int, nombre: str, documento: str, celular: str, correo: str, direccion: str, tipo_documento: str):
        super().__init__(id_cliente,nombre,documento,celular,correo,direccion,tipo_documento)
        self.__token_usuario = token_usuario
        self.__token_password = token_password

    def validar(self) -> bool:
        return bool(self.__direccion.strip())
    
    def obtenerinformacion(self) ->str:
        return f"ID: {self.__id_persona}\n-Tipo Documento: {self.__tipo_documento}\n-Documento: {self.__documento}\n-Nombre: {self.__nombre}\n-Celular {self.__celular}\n-Correo: {self.__correo}\n-Direccion{self.__direccion}."

class Vendedor(Persona):
    def __init__(self, token_usuario: str, token_password: str , id_cliente: int, nombre: str, documento: str, celular: str, correo: str, direccion: str, tipo_documento: str):
        super().__init__(id_cliente,nombre,documento,celular,correo,direccion,tipo_documento)
        self.__token_usuario = token_usuario
        self.__token_password = token_password

    def validar(self) -> bool:
        return bool(self.__direccion.strip())
    
    def obtenerinformacion(self) ->str:
        return f"ID: {self.__id_persona}\n-Tipo Documento: {self.__tipo_documento}\n-Documento: {self.__documento}\n-Nombre: {self.__nombre}\n-Celular {self.__celular}\n-Correo: {self.__correo}\n-Direccion{self.__direccion}."


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
        else:
            return "dimensionado"

    @staticmethod
    def calcular_costo(peso: float, tipo: str) -> float:
        """
        Calcula el costo de envío basado en el peso y tipo de paquete.
        """
        base = 5.0
        if tipo == "básico":
            return base
        elif tipo == "estándar":
            return base * 1.5
        else:
            return base * 2 + (peso * 0.5)


class Paquete:
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
    def __init__(self, id_envio: int, remitente: Cliente, destinatario: Cliente, paquetes: List[Paquete], observacion: str):
        if not all(p.aprobado for p in paquetes):
            raise ValueError("Todos los paquetes deben estar aprobados antes del envío")
        if not destinatario.validar():
            raise ValueError("Dirección del destinatario no válida")
        self.__id_envio = id_envio
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__paquetes = paquetes
        self.__trazabilidad = []
        self.__observaciones = observacion
        self.__costo_total = sum(p.costo_envio for p in paquetes)
        self.actualizar_trazabilidad("Envío creado")

    def actualizar_estado(self, estado: str):
        """
        Agrega un nuevo estado a la trazabilidad del envío.
        """
        self.actualizar_trazabilidad(estado)

    def actualizar_trazabilidad(self, estado: str):
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
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado con tarjeta de crédito."


class PagoPayPal(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado con PayPal."
class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago de {monto} USD procesado en Sucursal."


class Factura:
    """
    Representa una factura generada a partir de envíos.
    """
    def __init__(self, id_factura: int, envios: List[Envio]):
        self.id_factura = id_factura
        self.envios = envios
        self.monto = sum(e.costo_total for e in envios)

    def generar_factura(self):
        return f"Factura {self.id_factura} generada por {self.monto} USD"

    def procesar_pago(self, metodo_pago: MetodoPago) -> str:
        return metodo_pago.procesar_pago(self.monto)


class SistemaGestion:
    """
    Sistema de gestión de clientes, paquetes, envíos y facturación.
    """
    def __init__(self):
        self.clientes = []
        self.paquetes = []
        self.envios = []
        self.facturas = []

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def agregar_paquete(self, paquete: Paquete):
        self.paquetes.append(paquete)

    def actualizar_paquete(self, id_paquete: int, dimensiones: str, peso: float, observaciones: str):
        for p in self.paquetes:
            if p.id_paquete == id_paquete:
                p.actualizar_info(dimensiones, peso, observaciones)
                return True
        return False

    def aprobar_paquete(self, id_paquete: int):
        for p in self.paquetes:
            if p.id_paquete == id_paquete:
                p.aprobar()
                return True
        return False

    def crear_envio(self, id_envio: int, remitente: Cliente, destinatario: Cliente, paquetes: List[int]):
        paquetes_seleccionados = [p for p in self.paquetes if p.id_paquete in paquetes]
        envio = Envio(id_envio, remitente, destinatario, paquetes_seleccionados, "")
        self.envios.append(envio)

    def rastrear_envio(self, id_envio: int) -> Optional[List[str]]:
        for envio in self.envios:
            if envio.id_envio == id_envio:
                return envio.rastrear_envio()
        return None

    def generar_factura(self, id_factura: int, id_envios: List[int]):
        envios_facturados = [e for e in self.envios if e.id_envio in id_envios]
        if envios_facturados:
            factura = Factura(id_factura, envios_facturados)
            self.facturas.append(factura)
            return factura.generar_factura()
        return "No se encontraron envíos para facturar"