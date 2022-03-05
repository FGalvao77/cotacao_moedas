# cotação do euro
import requests
import datetime

def main():
    url = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')

    if url.status_code == 200:
        valor_euro = url.json()['EUR']['low']
        print(f'\nO valor do euro é: R$ {valor_euro} | Data: {datetime.datetime.today()}\n')
    else:
        print(f'ERROR: {url.status_code}')

if __name__ == '__main__':
    main()