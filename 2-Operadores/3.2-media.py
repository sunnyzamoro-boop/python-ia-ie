#Realizando nota do aluno
nome = input("Digite seu nome: ")
nota_1 = float(input("Digite primeira nota: "))
nota_2 = float(input("Digite segunda nota: "))
nota_3 = float(input("Digite terceira pessoa: "))

# Realizando cálculo da média 
media = (nota_1 + nota_2 + nota_3) / 3

print ("A média do aluno(a) ", nome, " é ", media)
print (f"A media do aluno(a) {nome} é {media:.2f} ele foi", situacao)


if media < 4:
    print("Reprovado")
elif media <=6:

else:
    situacao = "Aprovado"
