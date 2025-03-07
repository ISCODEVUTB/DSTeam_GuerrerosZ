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















