import requests
from time import sleep
from urllib3 import disable_warnings

disable_warnings()

url = 'https://httpbin.org/ip'
requisicao = requests.get(url, verify=False)
print(f'Seu ip externo é: {requisicao.json()['origin']}')
sleep(5)