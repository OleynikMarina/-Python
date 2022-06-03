from requests import get, utils
import json

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = get(URL)
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
dict_json = json.loads(response.text)

def currency_rates(val):
    if val in content:
        print(f"Курс {val} = {dict_json['Valute'][val]['Value']}")
    else: return None

currency_rates('EUR')
