from flask import Flask, render_template, request, flash
from currency_converter import CurrencyConverter, ForexPythonException


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-converter'

@app.route('/')
def converter_form():
    """Renders the form to covert currrencies"""
   
    return render_template('converter-form.html')

@app.route('/converter')
def convert_currency():
    try:
        initial_currency = request.form.get('initial-currency')
        desired_currency = request.form.get('desired-currency')
        initial_amount = float(request.form.get('amount'))

        
        validate_currency_code(initial_currency)
        validate_currency_code(desired_currency)

        converter = CurrencyConverter(api_key='36612560ce8c01a0e9bc3ff0454e5e61')
        result = converter.convert(initial_currency, desired_currency, initial_amount)

        return render_template('conversion_result.html', result=result)
    except ValueError:
        flash('Invalid amount. Please enter a valid numeric amount.')
    except ForexPythonException as e:
        flash(f'Error: {str(e)}. Please enter valid currency codes.')

def validate_currency_code(currency_code):
    if not CurrencyConverter.is_valid_currency_code(currency_code):
        raise ForexPythonException(f'Invalid currency code: {currency_code}')

if __name__ == "__main__":
    app.run()