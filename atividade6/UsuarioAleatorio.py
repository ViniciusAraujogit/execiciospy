import requests

resposta = requests.get("https://randomuser.me/api/")
dados = resposta.json()

usuario = dados['results'][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario['email']
pais = usuario['location']['country']

print("Perfil de Usuário Gerado Aleatoriamente:")
print(f"Nome : {nome}")
print(f"E-mail: {email}")
print(f"País : {pais}")