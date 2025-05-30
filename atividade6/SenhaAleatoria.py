import random

tamanho = int(input("Digite o tamanho da senha: "))

caracteres =  ["!","@","#","$","%","¨","&","*","-","+","/","?"]

aleatorio = ''.join(random.sample(caracteres, k=tamanho))

print(f"Senha aleatoria com carecteres especiais gerada: {aleatorio}")