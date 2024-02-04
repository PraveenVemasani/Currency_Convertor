# app.py
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

url_symbols = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/symbols"
url_convert = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

headers = {
    "X-RapidAPI-Key": "059ec661eamshb86fd3689ccb760p1db0cajsn7b48c2a6612f",
    "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response_symbols = requests.get(url_symbols, headers=headers)
symbols_data = response_symbols.json().get("symbols", {})

@app.route('/')
def index():
    return render_template('home.html', currencies=symbols_data)

@app.route('/convert', methods=['POST'])
def convert():
    amount = request.form.get('inp')
    from_currency_full = request.form.get('fromCurrency')
    to_currency_full = request.form.get('toCurrency')
    from_symbol, from_name = from_currency_full.split(maxsplit=1)
    to_symbol, to_name = to_currency_full.split(maxsplit=1)

    # Update the querystring with user-input values
    querystring = {
        "from": from_symbol,
        "to": to_symbol,
        "amount": amount
    }

    response = requests.get(url_convert, headers=headers, params=querystring)
    result = response.json()  # Assuming the response is in JSON format
    # return (result)
    countries={
        "from_country":from_name,
        "to_country":to_name
    }
    return render_template('home.html', currencies=symbols_data, result=result,countries=countries)

if __name__ == '__main__':
    app.run(debug=True)
