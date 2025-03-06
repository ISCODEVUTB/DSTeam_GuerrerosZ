from cls import metodos
from cls.clases import * # Importamos el módulo metodos desde cls
def main():
    """Función principal del sistema que maneja la autenticación y el menú principal."""
    print("\n AUTENTICACIÓN REQUERIDA")
    
    terminal = metodos.Terminal()  # Creamos el objeto Terminal

    while True:
        # Solicita credenciales al usuario
        usuario = input("Ingrese usuario: ").strip()
        contraseña = input("Ingrese contraseña: ").strip()
        
        if terminal.autenticar_credencial(usuario, contraseña):
            print(" Autenticación exitosa.")
            break  # Sale del bucle de autenticación y continúa con el menú principal
        else:
            print(" Credenciales incorrectas. Intente de nuevo.")

    while True:
        # Despliega el menú principal del sistema
        print("\n MENÚ PRINCIPAL")
        print("1. Crear Envío")
        print("2. Generar Factura")
        print("3. Buscar y Filtrar")
        print("4. Mostrar Mensaje Principal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            terminal.crear_envio()  # Llama al método para crear un envío

        elif opcion == "2":
            terminal.crear_factura()  # Llama al método para generar una factura

        elif opcion == "3":
            terminal.buscar_y_filtrar()  # Llama al método para buscar y filtrar

        elif opcion == "4":
            terminal.mostrar_mensaje_principal()  # Muestra un mensaje principal

        elif opcion == "5":
            print(" Saliendo del sistema. ¡Hasta luego!")
            break  # Termina la ejecución del programa

        else:
            print(" Opción inválida. Intente de nuevo.")  # Manejo de error por opción no válida

if __name__ == "__main__":
    main()  # Ejecuta la función principal si el script es ejecutado directamente
