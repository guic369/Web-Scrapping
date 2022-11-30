import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
print(now)

html = requests.get('https://www.tempo.com/quinta-do-sol.htm').content

soup = BeautifulSoup(html, 'html.parser')

tempo = soup.find(class_='titulo')
print(tempo.text)

temp_atual = soup.find(class_='dato-temperatura changeUnitT')
print(f'A temperatura atual é de {temp_atual.text}')

temp_min = soup.find(class_='minima changeUnitT')
print(f'A minima para hoje é {temp_min.text}')

temp_max = soup.find(class_='maxima changeUnitT')
print(f'A maxima para hoje é {temp_max.text}')

probab_chuva = soup.find(class_='probabilidad-lluvia')
print(f'A probabilidade de chuva é de{probab_chuva.text}')