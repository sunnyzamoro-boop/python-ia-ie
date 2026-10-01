# Coletando renda e situação do correntista
renda = float(input("Digite a sua renda mensal R$"))
situação = input("Possui restrição / nome negativado (s/n): ")

# Validando renda e situação de restrição
emprestimo = (renda >= 3000) and situação == "n"

print("Emprestimo Aprovado: ", emprestimo)