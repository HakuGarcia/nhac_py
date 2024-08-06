import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados = response.json()
    dados_restaurante = {}
    for item in dados:
        nome = item['Company']
        if nome not in dados_restaurante:
            dados_restaurante[nome] = []
        dados_restaurante[nome].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f" {response.status_code} fail")

for nome, dados in dados_restaurante.items():
    nome_arquivo = f'{nome}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)