import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ''.join(random.choices(caracteres, k=tamanho))

print(f"Senha aleatória gerada: {senha}")