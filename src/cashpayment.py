from src.paymentmethod import PaymentMethod
class CashPayment(PaymentMethod):
    """
    Represents a payment made in cash.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed at Branch."