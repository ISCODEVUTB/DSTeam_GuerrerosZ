from src.classes.Client import Client
from src.classes.Package import Package
from src.classes.Shipment import Shipment
from src.classes.Invoice import Invoice
from typing import List, Optional
class ManagementSystem:
    """
    Management system for clients, packages, shipments, and billing.
    """
    def __init__(self):
        self.clients = []
        self.packages = []
        self.shipments = []
        self.invoices = []

    def register_client(self, client: Client):
        self.clients.append(client)

    def add_package(self, package: Package):
        self.packages.append(package)

    def update_package(self, package_id: int, dimensions: str, weight: float, observations: str):
        for p in self.packages:
            if p.package_id == package_id:
                p.update_info(dimensions, weight, observations)
                return True
        return False

    def approve_package(self, package_id: int):
        for p in self.packages:
            if p.package_id == package_id:
                p.approve()
                return True
        return False

    def create_shipment(self, shipment_id: int, sender: Client, recipient: Client, packages: List[int]):
        selected_packages = [p for p in self.packages if p.package_id in packages]
        shipment = Shipment(shipment_id, sender, recipient, selected_packages, "")
        self.shipments.append(shipment)

    def track_shipment(self, shipment_id: int) -> Optional[List[str]]:
        for shipment in self.shipments:
            if shipment.shipment_id == shipment_id:
                return shipment.track_shipment()
        return None

    def generate_invoice(self, invoice_id: int, shipment_ids: List[int]):
        invoiced_shipments = [e for e in self.shipments if e.shipment_id in shipment_ids]
        if invoiced_shipments:
            invoice = Invoice(invoice_id, invoiced_shipments)
            self.invoices.append(invoice)
            return invoice.generate_invoice()
        return "No shipments found to invoice"