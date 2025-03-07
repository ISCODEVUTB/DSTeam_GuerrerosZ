import unittest
from src.classes.Paymentmethod import PaymentMethod
from src.classes.CardPayment import CardPayment
from src.classes.CashPayment import CashPayment
from src.classes.PayPalPayment import PayPalPayment

class TestPaymentMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Configura las instancias de las clases de pago para reutilización."""
        cls.payments = {
            "card": CardPayment(),
            "cash": CashPayment(),
            "paypal": PayPalPayment()
        }

    def test_abstract_class_instantiation(self):
        """Verifica que PaymentMethod no pueda ser instanciado directamente."""
        self.assertRaises(TypeError, PaymentMethod)

    def test_payment_processing(self):
        """Prueba el procesamiento de pagos en distintos métodos."""
        test_cases = [
            ("card", 100.0, "Payment of 100.0 USD processed with credit card."),
            ("cash", 200.0, "Payment of 200.0 USD processed at Branch."),
            ("paypal", 150.0, "Payment of 150.0 USD processed with PayPal.")
        ]

        for method, amount, expected in test_cases:
            with self.subTest(payment_method=method):
                self.assertEqual(self.payments[method].process_payment(amount), expected)

if __name__ == "__main__":
    unittest.main()
