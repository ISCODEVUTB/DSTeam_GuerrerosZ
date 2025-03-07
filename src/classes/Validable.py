from abc import ABC, abstractmethod
from typing import List, Optional

class Validable(ABC):
    """
    Abstract base class for validatable objects.
    """
    @abstractmethod
    def validate(self) -> bool:
        pass
