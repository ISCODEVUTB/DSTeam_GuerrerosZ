from src.classes.Paymentmethod import PaymentMethod
class CardPayment(PaymentMethod):
    """
    Represents a payment made with a credit card.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed with credit card."
