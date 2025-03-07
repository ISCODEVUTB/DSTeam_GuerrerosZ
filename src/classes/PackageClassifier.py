from typing import Literal

class PackageClassifier:
    """
    Provides methods to classify packages based on their weight and calculate shipping costs.
    """

    @staticmethod
    def classify(weight: float) -> Literal["basic", "standard", "oversized"]:
        """
        Determines the package type based on its weight.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        if weight < 1:
            return "basic"
        elif weight <= 5:
            return "standard"
        return "oversized"

    @staticmethod
    def calculate_cost(weight: float, package_type: str) -> float:
        """
        Calculates the shipping cost based on weight and package type.
        """
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        
        base_rates = {
            "basic": 5.0,
            "standard": 7.5,  # 5 * 1.5
            "oversized": 10.0  # 5 * 2
        }
        
        if package_type not in base_rates:
            raise ValueError("Invalid package type")

        base_cost = base_rates[package_type]
        extra_cost = weight * 0.5 if package_type == "oversized" else 0

        return base_cost + extra_cost
