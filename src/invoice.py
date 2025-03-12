from src.shipment import Shipment
from src.payment_method import PaymentMethod
from typing import List
class Invoice:
    """
    Represents an invoice generated from shipments.
    """
    def __init__(self, invoice_id: int, shipments: List[Shipment]):
        self.invoice_id = invoice_id
        self.shipments = shipments
        self.amount = sum(e.total_cost for e in shipments)

    def generate_invoice(self):
        return f"Invoice {self.invoice_id} generated for {self.amount} USD"

    def process_payment(self, payment_method: PaymentMethod) -> str:
        return payment_method.process_payment(self.amount)