import yfinance as yf
import json

import requests
from bs4 import BeautifulSoup
import json

# URL da página de busca no Indeed
url = "https://br.indeed.com/jobs?q=social+media&l=&from=searchOnHP"

# Realize uma solicitação HTTP para a página
response = requests.get(url)

# Inicialize uma lista para armazenar as vagas
vagas_lista = []

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseie o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre os elementos que contêm as informações das vagas
    vagas = soup.find_all('div', class_='jobsearch-SerpJobCard')

    # Itere sobre as vagas encontradas e adicione-as à lista
    for vaga in vagas:
        titulo = vaga.find('h2', class_='title')
        if titulo:
            vagas_lista.append({"Título": titulo.text.strip()})

    # Crie uma resposta JSON com a lista de vagas
    resposta_json = json.dumps({"vagas": vagas_lista}, ensure_ascii=False, indent=2)
    print(resposta_json)
else:
    print("Não foi possível acessar a página.")