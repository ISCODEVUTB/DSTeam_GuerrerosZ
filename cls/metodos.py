import clases
from typing import List, Optional
class Terminal():
    def __init__(self):
        self.__sistemaGestion = clases.SistemaGestion()
        self.__conjuntoCredencialesOperarios =[("operario1","12345")]
    
    def mostrar_mensaje_principal(self):
        print("Mensaje texto plano mensaje de entrada")

    def autenticar_credencial(self, token_usuario:str, token_contraseña:str) ->bool:
        for usuario, contraseña in self.__conjuntoCredencialesOperarios:
            if usuario == token_usuario and contraseña == token_contraseña:
                return True
        return False
    
    def crear_paquete(self, id_paquete: int, dimensiones: str, peso: float, observaciones: str) ->clases.Paquete:
        return clases.Paquete(id_paquete, dimensiones, peso, observaciones)

    def crear_envio(self, id_envio: int, remitente: clases.Cliente, destinatario: clases.Cliente, paquetes: List[clases.Paquete], observacion: str):
        return clases.Envio(id_envio,remitente,destinatario,paquetes,observacion)
    

