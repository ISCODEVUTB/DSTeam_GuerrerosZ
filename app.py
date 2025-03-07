from src import methods  # Importamos el módulo methods desde src

def main():
    """Main function of the system that handles authentication and the main menu."""
    print("\n AUTHENTICATION REQUIRED")
    
    terminal = methods.Terminal()  # Create the Terminal object

    while True:
        # Request credentials from the user
        user = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        if terminal.authenticate_credentials(user, password):
            print(" Authentication successful.")
            break  # Exit the authentication loop and continue to the main menu
        else:
            print(" Incorrect credentials. Try again.")

    while True:
        # Display the main menu of the system
        print("\n MAIN MENU")
        print("1. Create Shipment")
        print("2. Generate Invoice")
        print("3. Search and Filter")
        print("4. Show Main Message")
        print("5. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            terminal.create_shipment()  # Call the method to create a shipment

        elif option == "2":
            terminal.create_invoice()  # Call the method to generate an invoice

        elif option == "3":
            terminal.search_and_filter()  # Call the method to search and filter

        elif option == "4":
            terminal.show_main_message()  # Show a main message

        elif option == "5":
            print(" Exiting the system. Goodbye!")
            break  # Terminate the program execution

        else:
            print(" Invalid option. Try again.")  # Handle error for invalid option

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly