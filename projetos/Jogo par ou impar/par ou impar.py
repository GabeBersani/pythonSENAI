print("Jogo par ou impar")
print("Bem vindo ao programa de jogos!!!")
print("Regras: \nO usuário deve escolher se deseja ser par ou ímpar e escolher um número, depois o computador  "
      "ira mostrar o resultado e quem ganhou")
print("Vamos começar!")
print("")
while True:
    try:
        escolha = int(input("\n [1] Impar \n [2] Par \n escolha qual deseja jogar: "))
        while escolha != 1 and escolha != 2:
            print("algo deu errado, tente novamente")
            escolha = int(input("\n [1] Impar \n [2] Par \n escolha qual deseja jogar: "))

        escolha_numero = int(input("Escolha um numero entre 1 e 5: "))
        while escolha_numero < 0 or  escolha_numero > 5:
            print("Escolha outro numero entre 1 e 5")
            escolha_numero = int(input("Escolha um numero entre 1 e 5: "))
        break

    except ValueError:
        print("desculpe, algo deu errado")
import random

numero_computador = random.randint(1, 5)

while True:
    if escolha == 1:
        calculo = numero_computador + escolha_numero
        if calculo % 2 == 0:
            print("ponto para computador")
            print("")
            print("o numero do computador é", numero_computador)
        elif calculo % 2 != 0:
            print("ponto para você")
            print("")
            print("o numero do computador é", numero_computador)
        print("")
        while True:
            try:
                jogar_novamente = input("digite sim se vc gostaria de jogar novamente ou não se gostaria de sair : ")
                if jogar_novamente == "não":
                    print("o jogo acabou")
                    break
                elif jogar_novamente == "sim":
                    numero_computador = random.randint(1, 5)
                    escolha = int(input("\n [1] Impar \n [2] Par \n escolha qual deseja jogar: "))
                    escolha_numero = int(input("Escolha um numero entre 1 e 5: "))
                    break
                else:
                    print("algo deu errado, tente novamente")
            except ValueError:
                print("valor invalido")
        if jogar_novamente != "sim":
            escolha = 0
            break

    elif escolha == 2:
        calculo = numero_computador + escolha_numero
        if calculo % 2 == 0:
            print("ponto para você")
            print("")
            print("o numero do computador é", numero_computador)
        elif calculo % 2 != 0:
            print("ponto para computador")
            print("")
            print("o numero do computador é", numero_computador)
        print("")
        while True:
            try:
                jogar_novamente = input("digite sim se vc gostaria de jogar novamente ou não se gostaria de sair : ")
                if jogar_novamente == "não":
                    print("o jogo acabou")
                    break
                elif jogar_novamente == "sim":
                    numero_computador = random.randint(1, 5)
                    escolha = int(input("\n [1] Impar \n [2] Par \n escolha qual deseja jogar: "))
                    escolha_numero = int(input("Escolha um numero entre 1 e 5: "))
                    break
                else:
                    print("algo deu errado, tente novamente")
                numero_computador = random.randint(1, 5)
            except ValueError:
                print("valor invalido")
        if jogar_novamente != "sim":
            escolha = 0
            break







