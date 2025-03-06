from cls import metodos

def main():
    print("\n🔐 AUTENTICACIÓN REQUERIDA")
    
    terminal = metodos.Terminal()  # Creamos el objeto Terminal

    while True:
        usuario = input("Ingrese usuario: ").strip()
        contraseña = input("Ingrese contraseña: ").strip()
        
        if terminal.autenticar_credencial(usuario, contraseña):
            print("✅ Autenticación exitosa.")
            break  # Sale del bucle de autenticación y continúa con el menú principal
        else:
            print("❌ Credenciales incorrectas. Intente de nuevo.")

    while True:
        print("\n📦 MENÚ PRINCIPAL")
        print("1. Crear Envío")
        print("2. Generar Factura")
        print("3. Buscar y Filtrar")
        print("4. Mostrar Mensaje Principal")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            terminal.crear_envio()

        elif opcion == "2":
            terminal.crear_factura()

        elif opcion == "3":
            terminal.buscar_y_filtrar()

        elif opcion == "4":
            terminal.mostrar_mensaje_principal()

        elif opcion == "5":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
