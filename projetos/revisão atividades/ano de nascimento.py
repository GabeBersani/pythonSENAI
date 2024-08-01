# 3 - Solicite o ano de nascimento de uma pessoa
# calcule a idade e verifica se a pessoa é maior ou menor de idade e exiba uma mensagem correspondente.

print("vamos calcular sua idade atual de acordo com o ano de nascimento")
print("vamos falar se é maior ou menor de idade")
print("")

while True:
    try:
        ano_nasc = int(input("Digite o ano de nascimento: "))
        subtracao = 2024 - ano_nasc

        if subtracao > 130:
            print("idade invalida")

        elif subtracao < 18:
            print("menor de idade, a idade é", subtracao)


        elif subtracao >= 18:
            print("maior de idade, a idade é", subtracao)

        elif subtracao < 0:
            print("algo deu errado, idade não disponivel")

        else:
            print("algo deu errado")


    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")