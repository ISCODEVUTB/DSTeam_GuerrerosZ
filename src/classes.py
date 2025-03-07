from abc import ABC, abstractmethod
from typing import List, Optional

# Base class for validations
class Validable(ABC):
    """
    Abstract base class for validatable objects.
    """
    @abstractmethod
    def validate(self) -> bool:
        pass


class Person(ABC):
    """
    Abstract base class to represent a person with basic information.
    """
    def __init__(self, person_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str):
        """
        Initializes the common attributes of a person.
        """
        self._person_id = person_id
        self._name = name
        self._document_type = document_type
        self._document = document
        self._phone = phone
        self._email = email
        self.address = address

    @abstractmethod
    def get_information(self) -> str:
        """
        Returns the person's information in string format.
        """
        return (f"ID: {self._person_id}\n-Document Type: {self._document_type}"
                f"\n-Document: {self._document}\n-Name: {self._name}"
                f"\n-Phone {self._phone}\n-Email: {self._email}"
                f"\n-Address{self.address}.")


class Client(Person):
    """
    Represents a client, inheriting from the Person class.
    """
    def __init__(self, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str):
        """
        Initializes the client's attributes.
        """
        super().__init__(client_id, name, document, phone, email, address, document_type)

    def validate(self) -> bool:
        """
        Validates that the client's address is not empty.
        """
        return bool(self.address.strip())

    def get_information(self) -> str:
        """
        Returns the client's information.
        """
        return (f"ID: {self.person_id}\n-Document Type: {self.document_type}"
                f"\n-Document: {self.document}\n-Name: {self.name}"
                f"\n-Phone {self.phone}\n-Email: {self.email}"
                f"\n-Address{self.address}.")


class Operator(Person):
    """
    Represents an operator with authentication credentials.
    """
    def __init__(self, user_token: str, password_token: str, client_id: int, name: str, document: str, phone: str, email: str, address: str, document_type: str):
        """
        Initializes the operator's attributes.
        """
        super().__init__(client_id, name, document, phone, email, address, document_type)
        self._user_token = user_token
        self._password_token = password_token

    def validate(self) -> bool:
        """
        Validates that the operator's address is not empty.
        """
        return bool(self.__address.strip())

    def get_information(self) -> str:
        """
        Returns the operator's information.
        """
        return (f"ID: {self.person_id}\n-Document Type: {self.document_type}"
                f"\n-Document: {self.document}\n-Name: {self.name}"
                f"\n-Phone {self.phone}\n-Email: {self.email}"
                f"\n-Address{self.address}.")


class PackageClassifier:
    """
    Provides methods to classify packages based on their weight and calculate shipping costs.
    """
    @staticmethod
    def classify(weight: float) -> str:
        """
        Determines the package type based on its weight.
        """
        if weight < 1:
            return "basic"
        elif 1 <= weight <= 5:
            return "standard"
        return "oversized"

    @staticmethod
    def calculate_cost(weight: float, type: str) -> float:
        """
        Calculates the shipping cost based on the weight and package type.
        """
        base = 5.0
        if type == "basic":
            return base
        if type == "standard":
            return base * 1.5
        return base * 2 + (weight * 0.5)


class Package:
    """
    Represents a package with dimensions, weight, and approval status.
    """
    def __init__(self, package_id: int, dimensions: str, weight: float, observations: str):
        """
        Initializes a package and automatically calculates its type and shipping cost.
        """
        self.package_id = package_id
        self.dimensions = dimensions
        self.weight = weight
        self.observations = observations
        self.type = PackageClassifier.classify(weight)
        self.approved = False
        self.shipping_cost = PackageClassifier.calculate_cost(weight, self.type)

    def update_info(self, dimensions: str, weight: float, observations: str):
        """
        Updates the package's information and recalculates its type and shipping cost.
        """
        self.dimensions = dimensions
        self.weight = weight
        self.observations = observations
        self.type = PackageClassifier.classify(weight)
        self.shipping_cost = PackageClassifier.calculate_cost(weight, self.type)

    def approve(self):
        """
        Approves the package for shipping.
        """
        self.approved = True


class Shipment:
    """
    Represents a shipment with sender, recipient, and associated packages information.
    """
    def __init__(self, shipment_id: int, sender: Client, recipient: Client, packages: List[Package], observation: str):
        """
        Initializes a shipment, ensuring all packages are approved.
        """
        if not all(p.approved for p in packages):
            raise ValueError("All packages must be approved before shipping")
        if not recipient.validate():
            raise ValueError("Recipient's address is invalid")
        
        self.shipment_id = shipment_id
        self.sender = sender
        self.recipient = recipient
        self.packages = packages
        self.tracking = []
        self.observations = observation
        self.total_cost = sum(p.shipping_cost for p in packages)
        self.update_tracking("Shipment created")

    def update_status(self, status: str):
        """
        Adds a new status to the shipment's tracking.
        """
        self.update_tracking(status)

    def update_tracking(self, status: str):
        """
        Adds a status to the shipment's tracking list.
        """
        self.tracking.append(status)

    def track_shipment(self) -> List[str]:
        """
        Returns the list of shipment statuses.
        """
        return self.tracking


class PaymentMethod(ABC):
    """
    Abstract class for payment methods.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class CardPayment(PaymentMethod):
    """
    Represents a payment made with a credit card.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed with credit card."


class PayPalPayment(PaymentMethod):
    """
    Represents a payment made with PayPal.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed with PayPal."


class CashPayment(PaymentMethod):
    """
    Represents a payment made in cash.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed at Branch."

class Invoice:
    """
    Represents an invoice generated from shipments.
    """
    def __init__(self, invoice_id: int, shipments: List[Shipment]):
        self.invoice_id = invoice_id
        self.shipments = shipments
        self.amount = sum(e.total_cost for e in shipments)

    def generate_invoice(self):
        return f"Invoice {self.invoice_id} generated for {self.amount} USD"

    def process_payment(self, payment_method: PaymentMethod) -> str:
        return payment_method.process_payment(self.amount)


class ManagementSystem:
    """
    Management system for clients, packages, shipments, and billing.
    """
    def __init__(self):
        self.clients = []
        self.packages = []
        self.shipments = []
        self.invoices = []

    def register_client(self, client: Client):
        self.clients.append(client)

    def add_package(self, package: Package):
        self.packages.append(package)

    def update_package(self, package_id: int, dimensions: str, weight: float, observations: str):
        for p in self.packages:
            if p.package_id == package_id:
                p.update_info(dimensions, weight, observations)
                return True
        return False

    def approve_package(self, package_id: int):
        for p in self.packages:
            if p.package_id == package_id:
                p.approve()
                return True
        return False

    def create_shipment(self, shipment_id: int, sender: Client, recipient: Client, packages: List[int]):
        selected_packages = [p for p in self.packages if p.package_id in packages]
        shipment = Shipment(shipment_id, sender, recipient, selected_packages, "")
        self.shipments.append(shipment)

    def track_shipment(self, shipment_id: int) -> Optional[List[str]]:
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment.track_shipment()
        return None

    def generate_invoice(self, invoice_id: int, shipment_ids: List[int]):
        invoiced_shipments = [e for e in self.shipments if e.shipment_id in shipment_ids]
        if invoiced_shipments:
            invoice = Invoice(invoice_id, invoiced_shipments)
            self.invoices.append(invoice)
            return invoice.generate_invoice()
        return "No shipments found to invoice"