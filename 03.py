nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print(f"{nome}, você pode votar!")
else:
    print(f"{nome}, você não pode votar ainda.")
