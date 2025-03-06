from cls import clases
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
    
    def crear_factura(self):
        """Genera una factura basada en los envíos seleccionados por el usuario."""
        
        if not self.__sistemaGestion.envios:
            print("❌ No hay envíos disponibles para facturar.")
            return

        print("\n📜 Envíos disponibles para facturar:")
        for envio in self.__sistemaGestion.envios:
            print(f"ID: {envio._Envio__id_envio}, Remitente: {envio._Envio__remitente._Cliente__nombre}, Total: {envio._Envio__costo_total} USD")

        id_envios = input("Ingrese los IDs de los envíos a facturar (separados por comas): ").strip()
        id_envios = [int(id.strip()) for id in id_envios.split(",") if id.strip().isdigit()]
        
        if not id_envios:
            print("❌ No se han ingresado IDs válidos.")
            return

        nuevo_id_factura = len(self.__sistemaGestion.facturas) + 1  # Generar un ID único
        factura = self.__sistemaGestion.generar_factura(nuevo_id_factura, id_envios)

        if "No se encontraron envíos" in factura:
            print(factura)
            return

        print(f"\n✅ {factura}")

        # Procesar pago
        metodo_pago = self.seleccionar_metodo_pago()
        if metodo_pago:
            resultado_pago = metodo_pago.procesar_pago(sum(e._Envio__costo_total for e in self.__sistemaGestion.envios if e._Envio__id_envio in id_envios))
            print(f"💳 {resultado_pago}")

    def seleccionar_metodo_pago(self) -> Optional[clases.MetodoPago]:
        """Permite al usuario elegir un método de pago."""
        opciones_pago = {
            "1": clases.PagoTarjeta(),
            "2": clases.PagoPayPal(),
            "3": clases.PagoEfectivo()
        }

        print("\n💰 Métodos de Pago Disponibles:")
        print("1. Tarjeta de Crédito")
        print("2. PayPal")
        print("3. Pago en Efectivo (Sucursal)")

        opcion = input("Seleccione el método de pago (1-3): ").strip()

        return opciones_pago.get(opcion, None)

    def buscar_y_filtrar(self):
        """Permite buscar y filtrar clientes, envíos o paquetes en el sistema."""
        print("\n🔍 Opciones de búsqueda:")
        print("1. Buscar Cliente")
        print("2. Buscar Envío")
        print("3. Buscar Paquete")
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            self.buscar_cliente()
        elif opcion == "2":
            self.buscar_envio()
        elif opcion == "3":
            self.buscar_paquete()
        else:
            print("❌ Opción inválida.")

    def buscar_cliente(self):
        """Busca clientes por nombre o documento."""
        criterio = input("Ingrese el nombre o documento del cliente: ").strip().lower()
        
        clientes_encontrados = [
            c for c in self.__sistemaGestion.clientes
            if criterio in c._Cliente__nombre.lower() or criterio in c._Cliente__documento
        ]

        if clientes_encontrados:
            print("\n📋 Clientes encontrados:")
            for c in clientes_encontrados:
                print(f"ID: {c._Cliente__id_persona}, Nombre: {c._Cliente__nombre}, Documento: {c._Cliente__documento}")
        else:
            print("❌ No se encontraron clientes con ese criterio.")

    def buscar_envio(self):
        """Busca envíos por ID o estado en trazabilidad."""
        criterio = input("Ingrese el ID del envío o estado (Ej: 'En tránsito'): ").strip().lower()

        envios_encontrados = [
            e for e in self.__sistemaGestion.envios
            if str(e._Envio__id_envio) == criterio or any(criterio in estado.lower() for estado in e._Envio__trazabilidad)
        ]

        if envios_encontrados:
            print("\n📦 Envíos encontrados:")
            for e in envios_encontrados:
                print(f"ID: {e._Envio__id_envio}, Remitente: {e._Envio__remitente._Cliente__nombre}, Estado: {e._Envio__trazabilidad[-1]}")
        else:
            print("❌ No se encontraron envíos con ese criterio.")

    def buscar_paquete(self):
        """Busca paquetes por ID o tipo."""
        criterio = input("Ingrese el ID del paquete o tipo (básico, estándar, dimensionado): ").strip().lower()

        paquetes_encontrados = [
            p for p in self.__sistemaGestion.paquetes
            if str(p.id_paquete) == criterio or p.tipo.lower() == criterio
        ]

        if paquetes_encontrados:
            print("\n📦 Paquetes encontrados:")
            for p in paquetes_encontrados:
                print(f"ID: {p.id_paquete}, Tipo: {p.tipo}, Peso: {p.peso} kg")
        else:
            print("❌ No se encontraron paquetes con ese criterio.")

