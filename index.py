# Definição da função para calcular o IMC com base no peso e altura fornecidos
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  # Cálculo do IMC utilizando a fórmula peso / altura^2
    return imc

# Definição da função para classificar o IMC com base no valor do IMC fornecido
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"  # Retorna a string "Abaixo do peso" se o IMC for menor que 18.5
    elif imc < 25:
        return "Peso normal"  # Retorna a string "Peso normal" se o IMC estiver entre 18.5 e 24.9
    elif imc < 30:
        return "Sobrepeso"  # Retorna a string "Sobrepeso" se o IMC estiver entre 25 e 29.9
    elif imc < 35:
        return "Obesidade Grau I"  # Retorna a string "Obesidade Grau I" se o IMC estiver entre 30 e 34.9
    elif imc < 40:
        return "Obesidade Grau II"  # Retorna a string "Obesidade Grau II" se o IMC estiver entre 35 e 39.9
    else:
        return "Obesidade Grau III"  # Retorna a string "Obesidade Grau III" se o IMC for maior ou igual a 40

# Solicitação do peso e altura ao usuário
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Cálculo do IMC com base no peso e altura fornecidos
imc = calcular_imc(peso, altura)

# Classificação do IMC com base no valor calculado
classificacao = classificar_imc(imc)

# Exibição do resultado para o usuário
print("Seu IMC é:", imc)
print("Classificação:", classificacao)

