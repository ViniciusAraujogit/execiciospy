def palindromo(texto: str):
    
    texto = texto.lower()

    texto_limpo = ''
    for char in texto:
        if (char >= 'a' and char <= 'z') or (char >= '0' and char <= '9'):
            texto_limpo += char

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    
verificacao = input("Digite uma palavra para verificar se ela é um palíndromo: ")

print (f"A palavra {verificacao} é um palíndromo: {palindromo(verificacao)}")