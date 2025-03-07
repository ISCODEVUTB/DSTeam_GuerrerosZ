from src.classes.PackageClassifier import PackageClassifier

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















