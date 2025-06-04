import csv

def escrever_csv(nome_arquivo, dados):
    colunas = ["Nome", "Idade", "Cidade"]

    with open(nome_arquivo, mode="w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

dados_pessoas = [
    {"Nome": "Vinicius", "Idade": 24, "Cidade": "São Paulo"},
    {"Nome": "Isabella", "Idade": 23, "Cidade": "São Paulo"},
    {"Nome": "Felipe", "Idade": 24, "Cidade": "São Paulo"}
]

escrever_csv("pessoas.csv", dados_pessoas)