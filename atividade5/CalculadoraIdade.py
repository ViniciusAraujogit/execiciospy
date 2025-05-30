def calcular_idade (ano_nascimento: int, ano_atual: int):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

anoNascimento = int (input("Digite o seu ano de nascimento: "))
anoAtual = int (input("Digite o ano atual: "))

print (f"Idade aproximada em dias: {calcular_idade(anoNascimento, anoAtual)}")