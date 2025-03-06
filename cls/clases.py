from abc import ABC, abstractmethod
from typing import List, Optional


# Clase base para validaciones
class Validable(ABC):
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
    @staticmethod
    def clasificar(peso: float) -> str:
        if peso < 1:
            return "básico"
        elif 1 <= peso <= 5:
            return "estándar"
        else:
            return "dimensionado"

    @staticmethod
    def calcular_costo(peso: float, tipo: str) -> float:
        base = 5.0
        if tipo == "básico":
            return base
        elif tipo == "estándar":
            return base * 1.5
        else:
            return base * 2 + (peso * 0.5)


class Paquete(Validable):
    def __init__(self, id_paquete: int, dimensiones: str, peso: float, observaciones: str):
        self.__id_paquete = id_paquete
        self.__dimensiones = dimensiones
        self.__peso = peso
        self.__observaciones = observaciones
        self.__tipo = ClasificadorPaquete.clasificar(peso)
        self.__aprobado = False
        self.__costo_envio = ClasificadorPaquete.calcular_costo(peso, self.__tipo)

    def actualizar_info(self, dimensiones: str, peso: float, observaciones: str):
        self.__dimensiones = dimensiones
        self.__peso = peso
        self.__observaciones = observaciones
        self.__tipo = ClasificadorPaquete.clasificar(peso)
        self.__costo_envio = ClasificadorPaquete.calcular_costo(peso, self.__tipo)

    def aprobar(self):
        self.__aprobado = True

    @property
    def aprobado(self):
        return self.__aprobado

    @property
    def costo_envio(self):
        return self.__costo_envio

    @property
    def id_paquete(self):
        return self.__id_paquete


class Envio(Validable):
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
        self.__aprobacion = False
        self.__costo_total = sum(p.costo_envio for p in paquetes)
        self.actualizar_trazabilidad("Envío creado")

    def actualizar_estado(self, estado: str):
        self.actualizar_trazabilidad(estado)

    def actualizar_trazabilidad(self, estado: str):
        self.__trazabilidad.append(estado)

    def rastrear_envio(self) -> List[str]:
        return self.__trazabilidad


class MetodoPago(ABC):
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
    def __init__(self, id_factura: int, envios: List[Envio]):
        self.__id_factura = id_factura
        self.__envios = envios
        self.__monto = sum(e._Envio__costo_total for e in envios)

    def generar_factura(self):
        return f"Factura {self.__id_factura} generada por {self.__monto} USD"

    def procesar_pago(self, metodo_pago: MetodoPago) -> str:
        return metodo_pago.procesar_pago(self.__monto)


class SistemaGestion:
    def __init__(self):
        self.__clientes = []
        self.__paquetes = []
        self.__envios = []
        self.__facturas = []

    def registrar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def agregar_paquete(self, paquete: Paquete):
        self.__paquetes.append(paquete)

    def actualizar_paquete(self, id_paquete: int, dimensiones: str, peso: float, observaciones: str):
        for p in self.__paquetes:
            if p.id_paquete == id_paquete:
                p.actualizar_info(dimensiones, peso, observaciones)
                return True
        return False

    def aprobar_paquete(self, id_paquete: int):
        for p in self.__paquetes:
            if p.id_paquete == id_paquete:
                p.aprobar()
                return True
        return False

    def crear_envio(self, id_envio: int, remitente: Cliente, destinatario: Cliente, paquetes: List[int]):
        paquetes_seleccionados = [p for p in self.__paquetes if p.id_paquete in paquetes]
        envio = Envio(id_envio, remitente, destinatario, paquetes_seleccionados, "")
        self.__envios.append(envio)

    def rastrear_envio(self, id_envio: int) -> Optional[List[str]]:
        for envio in self.__envios:
            if envio._Envio__id_envio == id_envio:
                return envio.rastrear_envio()
        return None

    def generar_factura(self, id_factura: int, id_envios: List[int]):
        envios_facturados = [e for e in self.__envios if e._Envio__id_envio in id_envios]
        if envios_facturados:
            factura = Factura(id_factura, envios_facturados)
            self.__facturas.append(factura)
            return factura.generar_factura()
        return "No se encontraron envíos para facturar"
