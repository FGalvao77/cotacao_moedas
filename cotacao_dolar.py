# cotação dólar americano
import requests
import datetime

def main():
    url = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

    if url.status_code == 200:
        valor_dolar = url.json()['USD']['low']
        print(f'\nO valor do dólar é: R$ {valor_dolar} | Data: {datetime.datetime.today()}\n')
    else:
        print(f'ERROR: {url.status_code}')

if __name__ == '__main__':
    main()