from django.test import TestCase
from .utils import process_payment

class PaymentUtilityTests(TestCase):
    def test_process_payment_success(self):
        # Test a successful payment
        result = process_payment(100.0, "4111111111111111", 2, 2020, "111")
        self.assertEqual(result['status'], "success")
        self.assertTrue('authorization_code' in result)

    def test_process_payment_failure(self):
        # Test a payment failure
        result = process_payment(100.0, "invalid_card", 2, 2020, "111")
        self.assertEqual(result['status'], "failure")
        self.assertFalse('authorization_code' in result)

    def test_process_payment_invalid_cvv(self):
        # Test an invalid CVV
        result = process_payment(100.0, "4111111111111111", 2, 2020, "999")
        self.assertEqual(result['status'], "failure")
        self.assertFalse('authorization_code' in result)