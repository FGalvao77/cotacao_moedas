# cotação do rublo russo
import requests
import datetime

def main():
    url = requests.get('https://economia.awesomeapi.com.br/all/RUB-BRL')

    if url.status_code == 200:
        valor_rublo = url.json()['RUB']['low']
        print(f'\nO valor do rublo é: R$ {valor_rublo} | Data: {datetime.datetime.today()}\n')
    else:
        print(f'ERROR: {url.status_code}')

if __name__ == '__main__':
    main()