import unittest
from src.classes.Paymentmethod import PaymentMethod
from src.classes.CardPayment import CardPayment
from src.classes.CashPayment import CashPayment

class TestPaymentMethods(unittest.TestCase):

    def test_abstract_method(self):
        """Verifica que no se pueda instanciar directamente `PaymentMethod`."""
        with self.assertRaises(TypeError):
            PaymentMethod()  # No debería ser instanciable

    def test_card_payment(self):
        """Verifica el procesamiento de pago con tarjeta."""
        card = CardPayment()
        amount = 100.0
        expected = f"Payment of {amount} USD processed with credit card."
        self.assertEqual(card.process_payment(amount), expected)

    def test_cash_payment(self):
        """Verifica el procesamiento de pago en efectivo."""
        cash = CashPayment()
        amount = 200.0
        expected = f"Payment of {amount} USD processed at Branch."
        self.assertEqual(cash.process_payment(amount), expected)

if __name__ == "__main__":
    unittest.main()
