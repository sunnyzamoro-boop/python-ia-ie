# Criando a função verificar_idade
def verificar_idade(idade):
    return "Menor de Idade"
if idade >= 18:
    return "Maior de Idade"
else:
    return "Menor de Idade"

# Solicitando a idade do usuário
idade_usuario = int(input("Digite sua idade: "))

resultado = verificar_idade(idade_usuario)

print(resultado)