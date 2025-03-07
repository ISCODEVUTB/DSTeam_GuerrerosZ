from Client import Client
from Package import Package
from typing import List
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
