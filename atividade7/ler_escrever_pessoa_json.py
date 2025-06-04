import json

def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("Dados lidos do arquivo JSON:")
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Cidade: {dados['cidade']}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: Arquivo '{nome_arquivo}' não contém JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
pessoa = {
    "nome": "Vinicius",
    "idade": 24,
    "cidade": "São Paulo"
}

nome_arquivo = "pessoa.json"
escrever_json(nome_arquivo, pessoa)
ler_json(nome_arquivo)