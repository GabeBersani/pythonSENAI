#3 - Calculadora Básica: Crie uma função que receba dois números como parâmetros
# e exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão.

#3.1 - Crie uma função que receba dois números como parâmetros para cada uma das operações
# básicas citadas acima retornando somente o valor das operações.

#3.2 - Crie uma função que faça um menu para o usuário escolher a opção desejada.

print("Bem vindo a CALCULADORA!!! ")
def solicita_numeros():
    while True:
        try:

            num1 = float(input("Digite um numero: "))
            return num1
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

def solicita_numeros1():
    while True:
        try:
            num2 = float(input("Digite outro numero: "))
            return num2
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")


def escolha_operacoes():
    while True:
        try:


            escolha = int(input("\n [1] Adição \n [2] Subtração \n [3] multiplicação \n [4]divisão"
                                " \n escolha qual operação deseja: "))
            return escolha
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")


def conta_operacao(num1, num2, escolha):
    while True:
        try:

            if escolha == 1:
                soma = num1 + num2
                print("O resultado da adição é", soma)

            elif escolha == 2:
                subtracao = num1 - num2
                print("O resultado da subtração é", subtracao)

            elif escolha == 3:
                multiplicacao = num1 * num2
                print("O resultado da multiplicação é", multiplicacao)

            elif escolha == 4:
                divisao = num1 / num2
                print("O resultado da divisão é", divisao)

            else:
                print("algo deu errado")
            break

        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")


numero1 = solicita_numeros()
numero2 = solicita_numeros()
escolha = escolha_operacoes()
conta_operacao(numero1, numero2, escolha)

