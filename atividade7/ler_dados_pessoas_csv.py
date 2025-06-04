import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            print("Dados do arquivo CSV:\n")
            for linha in leitor:
                nome = linha["Nome"]
                idade = linha["Idade"]
                cidade = linha["Cidade"]
                print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

ler_csv("pessoas.csv")