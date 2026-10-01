# Solicitando o nome e a idade do usuário
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade: "))

# Criando acondição for >= a 18 anos 
if idade >= 18:
    print("Maior de Idade")

else:
    print("Menor de Idade")