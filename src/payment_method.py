from abc import ABC, abstractmethod
from typing import List, Optional
class PaymentMethod(ABC):
    """
    Abstract class for payment methods.
    """
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass