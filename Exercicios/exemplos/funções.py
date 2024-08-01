from datetime import datetime


def menu_calculadora():
    print("menu calculadora")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")

menu_calculadora()

def ola_nome(nome):
    print("Ola", nome)
ola_nome("Gabriele")

def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
print("idade é ",calcula_idade(2007))


def solicite_ano_nascimento():
    while True:
        try:
           ano_nascimento = int(input("Digite o ano de nascimento: "))
           if ano_nascimento > datetime.now().year:
               return ano_nascimento
           else:
               print("digite um ano menor que o atual")
        except ValueError:
            print("Digite somente numeros. Ex: 1997")
