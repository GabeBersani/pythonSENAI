print("Jogo de adivinhação")
print("Bem vindo ao programa de jogos!!!")
print("Regras: \nO computador sorteara um numero de 0 a 100 para que o usuario tente"
      " adivinhar o numero escolhido pelo computador.")
print("Vamos começar!")
print("")
escolha = int(input("Escolha um numero entre 1 a 100: "))

import random

numero_computador = random.randint(1, 100)

while escolha != 0:
    if escolha == numero_computador:
        while True:
            try:
                print("parabens, você ganhou !!!")
                print("")
                jogar_novamente = input("digite sim se vc gostaria de jogar novamente, ou não se deseja sair : ")
                numero_computador = random.randint(1, 100)
                if jogar_novamente == "não":
                    print("jogo acabou")
                    break
                elif jogar_novamente == "sim":
                    numero_computador = random.randint(1, 100)
                    escolha = int(input("Escolha um numero entre 1 a 100: "))
                    break
                else:
                    print("algo deu errado, tente novamente")
            except ValueError:
                print("valor invalido")
        if jogar_novamente != "sim":
            escolha = 0
            break
    elif escolha > 100:
        while True:
            try:
                print("algo deu errado, tente jogar novamente")
                break
            except ValueError:
                print("numero invalido , digite um numero utilizado exemplo : 1")
        escolha = int(input("Escolha um numero entre 1 a 100: "))

    elif escolha > numero_computador:
        while True:
            try:
                print("esse numero é maior que o do computador")
                if escolha >= 1 and escolha <= 100:
                    break
            except ValueError:
                print("numero invalido , digite um numero utilizado exemplo : 1")
        escolha = int(input("Escolha um numero entre 1 a 100: "))

    elif escolha < numero_computador:
        while True:
            try:
                print("esse numero é menor que o do computador")
                if escolha >= 1 and escolha <= 100:
                    break
            except ValueError:
                print("numero invalido , digite um numero utilizado exemplo : 1")
        escolha = int(input("Escolha um numero entre 1 a 100: "))

    else:
        print("você parou de jogar")


