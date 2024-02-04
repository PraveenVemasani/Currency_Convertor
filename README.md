# Currency Converter

Welcome to the Currency Converter, a web application designed to simplify currency conversion. This application utilizes the Flask API along with two external APIs to provide a comprehensive currency conversion experience.

<img width="960" alt="image" src="https://github.com/PraveenVemasani/Currency_Convertor/assets/107190143/acf4d05b-9ac0-4501-b0c5-c60d8b84a38b">
<img width="960" alt="image" src="https://github.com/PraveenVemasani/Currency_Convertor/assets/107190143/36214f4e-d7bb-46fe-a1ef-7d24584234b9">
<img width="960" alt="image" src="https://github.com/PraveenVemasani/Currency_Convertor/assets/107190143/212f810f-86aa-4891-ac6d-770548909b0c">

## Flask-API

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries, and it has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

For detailed information on Flask-API  you can refer to the following resource:

- [Flask API](https://flask.palletsprojects.com/en/3.0.x/api/): A handy resource that provides a quick reference of all the interfaces of Flask.


## Features

**Country Information:** 
- Get a list of supported nations along with their currency symbols and corresponding national flags.
  
**Currency Conversion:** 
- Perform currency conversion from one country to another with real-time exchange rates.
  
**User-Friendly Interface:** 
- Choose currencies easily and get instant conversion results.

## APIs Used

**Country Information API:** This API provides information about nations, including currency symbols and flags.

- API Endpoint: [Country Information API](https://flagsapi.com/)
  
**Currency Conversion API:** This API is used for real-time currency conversion.
- API Endpoint: [Currency Conversion API](https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/)



## Usage



**Supported Countries Display:**

- Visit the website to view a list of supported nations along with their currency codes and flags.

**Currency Conversion:**

- Choose the 'From' and 'To' currencies from the dropdown lists.
- Enter the amount you want to convert in the 'Amount' field.
- Click the 'Convert' button to get the conversion result.

**Result Display:**

- The result will be displayed, showing the converted amount, source and target currencies, and the exchange rate.

### Note

- To use the Currency Conversion API, you'll need to obtain an API key from [Currency Conversion API](https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/) and replace it in the app.py file.

## Acknowledgements

Special thanks to the creators of the [Country Information API](https://flagsapi.com/) and [Currency Conversion API](https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates/) for their valuable services.
