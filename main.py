#from fastapi import FastAPI
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
CORS(app)

@cross_origin()

@app.route("/", methods=['GET'])
def home():

    url = "https://www.indeed.com.br/jobs?q=social+media"

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

    return jsonify(ibovData);

if __name__ == "__main__":
    app.run(debug=True);