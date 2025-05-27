contadorimpar = 0
contadorpar = 0 

for _ in range (1000):
    numero = input("Digite um número ou 'fim' para encerrar o programa: ")

    if numero == 'fim':
        print("Programa encerrado!!!")
        break

    try:
        numero = int(numero)
        if (numero % 2 == 0):
            print ("É um número par!")
            contadorpar += 1
        else:
            print ("É um número impar!")
            contadorimpar += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro")

print (f"Quantidade de números pares: {contadorpar}")
print (f"Quantidade de números impares: {contadorimpar}")
            