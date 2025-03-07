import unittest


class TestCardPayment(unittest.TestCase):
    def setUp(self):
        self.card_payment = CardPayment()

    def test_process_payment(self):
        amount = 100.0
        expected_output = f"Payment of {amount} USD processed with credit card."
        self.assertEqual(self.card_payment.process_payment(amount), expected_output)

if __name__ == "__main__":
    unittest.main()

