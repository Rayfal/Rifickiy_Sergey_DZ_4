import requests
from bs4 import BeautifulSoup

def currency_rates(*args):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    quotes = soup.findAll('valute')
    for i in quotes:
        cod = i.find('charcode').text
        code = cod
        if code != i:
            name = i.find('name').text
            print(f'Вы ввели валюту: {name}')
            return i.find('value').text.replace(',', '.')
    return None
char = input('Введите код валюты: ').upper()
print(f'Курс валюты {char} = {currency_rates(char)} руб.')