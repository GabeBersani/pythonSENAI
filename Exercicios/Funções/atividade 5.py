#5 - Calculadora IMC: Crie uma função que receba dois parâmetros que serão o peso e a altura de uma pessoa
# e retorne seu IMC.

#IMC = peso / (altura x altura)

#peso pessoa
def valor_peso():
    while True:
        try:
            peso = float(input("Digite o seu peso em KG: "))
            return peso
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

#altura pessoa
def valor_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros: "))
            return altura
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

#conta
def conta_imc(peso, altura):
    while True:
        try:
            alturaimc = altura * altura
            calculo = peso / alturaimc
            return calculo
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

def imc_toatl(calculo):
    while True:
        try:
            if calculo >= 17 and calculo <= 18.4:
              classificacao = "Seu IMC está na categoria abaixo do peso: "
              print(classificacao, (int(calculo)))

            elif calculo >= 18.5 and calculo <= 24.9:
              classificacao = "Seu IMC está na categoria peso normal: "
              print(classificacao, (int(calculo)))

            elif calculo >= 25 and calculo <= 29.9:
              classificacao = "Seu IMC está na categoria sobrepesso: "
              print(classificacao,(int(calculo)))

            elif calculo >= 30 and calculo <=40:
              classificacao = "Seu IMC está na categoria obesidade: "
              print(classificacao, (int(calculo)))
            else:
              print("Não tem correspondência de acordo com as informações inseridas")

            break

        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

peso = valor_peso()
altura = valor_altura()
calculo = conta_imc(peso, altura)
imc_toatl(calculo)
