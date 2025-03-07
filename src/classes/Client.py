from src.classes.Person import Person

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
