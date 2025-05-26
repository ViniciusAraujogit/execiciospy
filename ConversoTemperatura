temperatura = float(input("Digite a temperatura para a conversão: "))
origemTemperatura = input("Digite a unidade de origem (Celsius, Fahrenheit ou Kelvin): ")
conversaoTemperatura = input("Digite a unidade para qual deseja converter (Celsius, Fahrenheit ou Kelvin): ")

if origemTemperatura == "Celsius" and conversaoTemperatura == "Fahrenheit":
    resultado = temperatura * 9/5 + 32
    print(f"{temperatura}°Celsius equivale a {resultado:.2f}°Fahrenheit")
elif origemTemperatura == "Celsius" and conversaoTemperatura == "Kelvin":
    resultado = temperatura + 273.15
    print(f"{temperatura}°Celsius equivale a {resultado:.2f}°Kelvin")
elif origemTemperatura == "Fahrenheit" and conversaoTemperatura == "Celsius":
    resultado = (temperatura - 32) * 5 / 9
    print(f"{temperatura}°Fahrenheit equivale a {resultado:.2f}°Celsius")
elif origemTemperatura == "Fahrenheit" and conversaoTemperatura == "Kelvin":
    resultado = (temperatura - 32) * 5 / 9 + 273.15
    print(f"{temperatura}°Fahrenheit equivale a {resultado:.2f}°Kelvin")
elif origemTemperatura == "Kelvin" and conversaoTemperatura == "Celsius":
    resultado = temperatura - 273.15
    print(f"{temperatura}°Kelvin equivale a {resultado:.2f}°Celsius")
elif origemTemperatura == "Kelvin" and conversaoTemperatura == "Fahrenheit":
    resultado = (temperatura - 273.15) * 9 / 5 + 32
    print(f"{temperatura}°Kelvin equivale a {resultado:.2f}°Fahrenheit")
elif origemTemperatura == conversaoTemperatura:
    resultado = temperatura  
    print(f"Unidades iguais. A temperatura permanece {temperatura}°{origemTemperatura}")
else:
    print("Unidade de origem ou destino inválida.")