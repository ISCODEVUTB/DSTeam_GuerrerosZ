from src.classes import Client, Package, Shipment, Invoice, Paymentmethod, CardPayment, PayPalPayment, CashPayment, ManagementSystem,PackageClassifier
import re
from typing import Optional, List

class Terminal:
    def __init__(self):
        """Initializes the terminal with a management system and operator credentials."""
        self.__management_system = ManagementSystem.ManagementSystem()
        self.__operator_credentials_set = [("operator1", "12345")]

    def show_main_message(self):
        """Displays a welcome message on the terminal."""
        print("Plain text welcome message")

    def authenticate_credentials(self, user_token: str, password_token: str) -> bool:
        """Verifies if the entered credentials correspond to a registered operator."""
        return (user_token, password_token) in self.__operator_credentials_set

    def request_sender_info(self) -> Client:
        """Requests and returns the sender's information."""
        return self.__request_client_info("sender")

    def request_recipient_info(self) -> Client:
        """Requests and returns the recipient's information."""
        return self.__request_client_info("recipient")

    def __request_client_info(self, type: str) -> Client:
        """Requests the information of a client (sender or recipient) with data validation."""
        print(f"\n Enter the {type}'s data:")

        def validate_number(message: str) -> int:
            """Requests a positive integer from the user."""
            while True:
                try:
                    value = int(input(message).strip())
                    if value > 0:
                        return value
                    print(" Error: You must enter a positive number.")
                except ValueError:
                    print(" Invalid input. Enter a valid number.")

        client_id = validate_number("Enter client ID: ")

        def validate_text(message: str) -> str:
            """Requests a non-empty text from the user."""
            while True:
                text = input(message).strip()
                if text:
                    return text
                print(" Error: The field cannot be empty.")

        def validate_option(message, valid_options):
            """Validates that the entered option is one of the allowed ones."""
            while True:
                option = input(message).strip().upper()
                if option in valid_options:
                    return option
                print(f" Invalid option. Must be one of: {', '.join(valid_options)}.")

        document_type = validate_option("Enter document type (CC/CE/PAS): ", ["CC", "CE", "PAS"])
        document = validate_text("Enter document: ")
        name = validate_text("Enter name: ")
        phone = validate_text("Enter phone: ")
        email = validate_text("Enter email: ")
        address = validate_text("Enter address: ")

        return Client(client_id, name, document, phone, email, address, document_type)

    def request_package_info(self, n: int, package_id: int) -> List[Package]:
        """Requests the information of 'n' packages and returns them in a list of Package objects."""
        packages = []

        def validate_number(message: str) -> float:
            """Requests a positive float number from the user."""
            while True:
                try:
                    value = float(input(message).strip())
                    if value > 0:
                        return value
                    print(" Error: You must enter a positive number.")
                except ValueError:
                    print(" Invalid input. Enter a valid number.")

        for _ in range(n):
            print("\n Enter the package's data:")
            package_id += 1  # Correctly increments in each iteration
            weight = validate_number("Enter the package's weight (kg): ")
            length = validate_number("Enter the package's length (cm): ")
            width = validate_number("Enter the package's width (cm): ")
            height = validate_number("Enter the package's height (cm): ")
            dimensions = f"{length},{width},{height}"
            observations = input("Enter package observations (optional): ").strip()

            package = Package(package_id, dimensions, weight, observations)
            packages.append(package)

        print(f"\n {n} packages have been registered successfully.")
        return packages

    def create_shipment(self) -> str:
        """Creates a new shipment with user-entered data."""
        sender = self.request_sender_info()
        recipient = self.request_recipient_info()
        num_packages = int(input("Enter the number of packages: "))
        package_list = self.request_package_info(num_packages, package_id=len(self.__management_system.packages))

        # Register clients and add packages
        self.__management_system.register_client(sender)
        self.__management_system.register_client(recipient)

        for package in package_list:
            self.__management_system.add_package(package)

        observation = input("Enter shipment observations (optional): ").strip()

        # Generate a new unique shipment ID
        new_shipment_id = len(self.__management_system.shipments) + 1
        shipment = self.__management_system.create_shipment(new_shipment_id, sender, recipient, [p.package_id for p in package_list], observation)

        print("\n Shipment created successfully.")
        return shipment

    def create_invoice(self):
        """Generates an invoice based on the shipments selected by the user."""
        if not self.__management_system.shipments:
            print("No shipments available to invoice.")
            return

        print("\n Shipments available for invoicing:")
        for shipment in self.__management_system.shipments:
            print(f"ID: {shipment.shipment_id}, Sender: {shipment.sender.name}, Total: {shipment.total_cost} USD")

        shipment_ids = input("Enter the IDs of the shipments to invoice (separated by commas): ").strip()
        shipment_ids = [int(id.strip()) for id in shipment_ids.split(",") if id.strip().isdigit()]

        if not shipment_ids:
            print("No valid IDs entered.")
            return

        new_invoice_id = len(self.__management_system.invoices) + 1  # Generate a unique ID
        invoice = self.__management_system.generate_invoice(new_invoice_id, shipment_ids)

        if "No shipments found" in invoice:
            print(invoice)
            return

        print(f"\n{invoice}")

        # Process payment
        payment_method = self.select_payment_method()
        if payment_method:
            total_cost = sum(shipment.total_cost for shipment in self.__management_system.shipments if shipment.shipment_id in shipment_ids)
            payment_result = payment_method.process_payment(total_cost)
            print(f"{payment_result}")

    def select_payment_method(self) -> Optional[Paymentmethod]:
        """Allows the user to choose a payment method."""
        payment_options = {
            "1": CardPayment(),
            "2": PayPalPayment(),
            "3": CashPayment()
        }

        print("\n Available Payment Methods:")
        print("1. Credit Card")
        print("2. PayPal")
        print("3. Cash (Branch)")

        option = input("Select the payment method (1-3): ").strip()

        return payment_options.get(option, None)

    def search_and_filter(self):
        """Allows searching and filtering clients, shipments, or packages in the system."""
        print("\n Search options:")
        print("1. Search Client")
        print("2. Search Shipment")
        print("3. Search Package")

        option = input("Select an option (1-3): ").strip()

        if option == "1":
            self.search_client()
        elif option == "2":
            self.search_shipment()
        elif option == "3":
            self.search_package()
        else:
            print(" Invalid option.")

    def search_client(self):
        """Searches clients by name or document."""
        criteria = input("Enter the client's name or document: ").strip().lower()

        found_clients = [
            c for c in self.__management_system.clients
            if criteria in c.name.lower() or criteria in c.document
        ]

        if found_clients:
            print("\n Found clients:")
            for c in found_clients:
                print(f"ID: {c.person_id}, Name: {c.name}, Document: {c.document}")
        else:
            print(" No clients found with that criteria.")

    def search_shipment(self):
        """Searches shipments by ID or status in tracking."""
        criteria = input("Enter the shipment ID or status (e.g., 'In transit'): ").strip().lower()

        found_shipments = [
            e for e in self.__management_system.shipments
            if str(e.shipment_id) == criteria or any(criteria in status.lower() for status in e.tracking)
        ]

        if found_shipments:
            print("\n Found shipments:")
            for e in found_shipments:
                print(f"ID: {e.shipment_id}, Sender: {e.sender.name}, Status: {', '.join(e.tracking)}")
        else:
            print(" No shipments found with that criteria.")