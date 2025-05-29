def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float):
    gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return gorjeta

valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite o valor da porcentagem da gorjeta: "))

print(f"Gorjeta: R$ {calcular_gorjeta(valor,porcentagem):.2f}")