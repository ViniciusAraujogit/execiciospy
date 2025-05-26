idade = int(input("Digite a sua Idade: "))

if idade < 0:
    print ("Idade invalida")
elif idade <= 12:
    print ("Você esta classificado como criança!")
elif idade <= 17:
    print ("Você esta classificado como adolescente!")
elif idade <= 59:
    print ("Você esta classificado como adulto!")
else:
    print ("Você esta classificado como idoso!")