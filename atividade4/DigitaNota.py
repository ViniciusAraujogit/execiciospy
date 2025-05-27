soma = 0
quantidade = 0

for _ in range(1000):  
    entrada = input("Digite a nota ou 'fim' para encerrar: ")

    if entrada == 'fim':  
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            soma += nota
            quantidade += 1
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if quantidade > 0:
    media = soma / quantidade
    print(f"A média do aluno é: {media:.2f}")
else:
    print("Nenhuma nota foi registrada!!!")