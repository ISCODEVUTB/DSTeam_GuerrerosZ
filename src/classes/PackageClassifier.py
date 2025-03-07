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
