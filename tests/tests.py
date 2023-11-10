import unittest
from app import convert_currency

class TestCurrencyConverter(unittest.TestCase):

    def test_conversion_same_currency(self):
        # Test if $1 USD converts to $1 USD
        with app.test_request_context('/', method='POST', data={
            'initial-currency': 'USD',
            'desired-currency': 'USD',
            'amount': '1'
        }):
            response = convert_currency()
            self.assertIn('$1.00 = $1.00', response.get_data(as_text=True))