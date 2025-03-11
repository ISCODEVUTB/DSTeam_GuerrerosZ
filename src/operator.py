from src.person import Person

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
        return (f"ID: {self._person_id}\n-Document Type: {self._document_type}"
                f"\n-Document: {self._document}\n-Name: {self._name}"
                f"\n-Phone {self._phone}\n-Email: {self._email}"
                f"\n-Address{self.address}.")
