from forex_python.converter import CurrencyRates, CurrencyCodes, get_symbol
import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.url = f'http://data.fixer.io/api/latest?access_key={api_key}'
        data = requests.get(self.url).json()
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        c = CurrencyCodes()
        initial_amount = amount
        initial_symbol = c.get_symbol(from_currency)
        converted_symbol = c.get_symbol(to_currency)

        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        amount = round(amount * self.rates[to_currency], 2)
        
        result = '{}{} = {}{}'.format(initial_symbol, initial_amount, converted_symbol, amount)
        return result

