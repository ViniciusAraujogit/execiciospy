for _ in range (1000):
    senha = input ("Digite a senha ou 'sair' para encerrar: ")

    if senha == 'sair':
        print ("Programa encerrado.")
        break
    
    if len(senha) > 8 and any(c.isdigit() for c in senha):
        print("Senha forte cadastada!")
        break
    else:
        print("Erro! A senha precisa ter pelo menos 8 caracteres e pelo menos um número.")