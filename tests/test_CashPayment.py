import unittest
from src.cashpayment import CashPayment  # Asegurar que la ruta es correcta

class TestCashPayment(unittest.TestCase):
    def setUp(self):
        self.cash_payment = CashPayment()

    def test_process_payment(self):
        amount = 100.0
        expected_output = f"Payment of {amount} USD processed at Branch."
        self.assertEqual(self.cash_payment.process_payment(amount), expected_output)

if __name__ == "__main__":
    unittest.main()
