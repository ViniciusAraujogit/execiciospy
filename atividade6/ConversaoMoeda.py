import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
resposta = requests.get(url)
dados = resposta.json()

info = dados[moeda + "BRL"]

print("\nCotação atual:")
print(f"Moeda              : {info['name']}")
print(f"Valor Atual        : R$ {float(info['bid']):.2f}")
print(f"Valor Máximo       : R$ {float(info['high']):.2f}")
print(f"Valor Mínimo       : R$ {float(info['low']):.2f}")
print(f"Última Atualização : {info['create_date']}")
