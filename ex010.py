import requests

# URL da API do Banco Central do Brasil para a cotação do dólar
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json'

response = requests.get(url)
data = response.json()

# Acessando a cotação do dólar
exchange_rate = data[0]['valor']

carteira = float(input('Digite o valor da carteira: '))

res = carteira / float(exchange_rate)

print(f'Com R${carteira:.2f} na carteira poderá comprar US${res:.2f}.')
