from abc import ABC, abstractmethod
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

