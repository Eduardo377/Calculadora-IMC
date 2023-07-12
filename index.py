def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade Grau I"
    elif imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print("Seu IMC é:", imc)
print("Classificação:", classificacao)
