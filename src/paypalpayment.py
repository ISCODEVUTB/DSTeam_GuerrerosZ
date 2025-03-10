from src.paymentmethod import PaymentMethod
class PayPalPayment(PaymentMethod):
    """
    Represents a payment made with PayPal.
    """
    def process_payment(self, amount: float) -> str:
        return f"Payment of {amount} USD processed with PayPal."
