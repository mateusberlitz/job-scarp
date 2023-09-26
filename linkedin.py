import requests
from bs4 import BeautifulSoup
import json

# URL da página de busca no InfoJobs
url = "https://www.linkedin.com/jobs/search/?currentJobId=3728323774&keywords=social%20media&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true"

# Realize uma solicitação HTTP para a página
response = requests.get(url)

print(response)

# Inicialize uma lista para armazenar as vagas
vagas_lista = []

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseie o conteúdo da página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre os elementos que contêm as informações das vagas
    vagas = soup.find_all('article')

    # Itere sobre as vagas encontradas e adicione-as à lista
    for vaga in vagas:
        titulo = vaga.find('h2')
        if titulo:
            vagas_lista.append({"Título": titulo.text.strip()})

    # Crie uma resposta JSON com a lista de vagas
    resposta_json = json.dumps({"vagas": vagas_lista}, ensure_ascii=False, indent=2)
    print(resposta_json)
else:
    print("Não foi possível acessar a página.")