import clases
class Terminal():
    def __init__(self):
        self.__sistemaGestion = clases.SistemaGestion()
        self.__conjuntoCredencialesOperarios =[]
    
    def mostrar_mensaje_principal(self):
        print("Mensaje texto plano mensaje de entrada")

    def autenticar_credencial(self, token_usuario:str, token_contraseña:str):
        token_usuario

