import requests

URL = 'http://viacep.com.br/ws/{}/json'

while(True):
    cep = input('Insira o cep:')
    if not cep:
        break

    response = requests.get(URL.format(cep))
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.content)