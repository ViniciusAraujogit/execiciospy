try: 
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        resultado = numero1 / numero2
    else:
        print("Erro: operação inválida. Use apenas +, -, * ou /.")
    
    if operacao in ['+', '-', '*', '/'] and not (operacao == '/' and numero2 == 0):
        print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")

except ValueError:
    print("Erro: você digitou um valor que não é número.")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
