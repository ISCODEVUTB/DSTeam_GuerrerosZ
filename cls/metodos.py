import clases
class Terminal():
    def __init__(self):
        self.__sistemaGestion = clases.SistemaGestion()
        self.__conjuntoCredenciales =[]
    
    def mostrar_mensaje_principal(self):
        print("Mensaje texto plano mensaje de entrada")

    def autenticar_credencial(self, token_usuario:str, toker_contraseña:str):
        token

