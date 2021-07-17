import unittest

from forex import forex_function

class TestForexAns(unittest.TestCase):
    def test_usd(self):
        message="value are not equal!"
        result = forex_function(11222.02,32.23)
        self.assertEqual(result, "Payment=TWD 361686",message)

    def test_jpy(self):
        message="value are not equal!"
        result = forex_function(31999,0.35)
        self.assertEqual(result, "Payment=TWD 11200",message)


