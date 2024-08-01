#1- Mensagem automática: Crie uma função que receba um nome como parâmetro e
# escreva uma saudação baseada na hora atual.

#Madrugada - 0h às 5h - Boa madruga
#Manhã - 5h às 12h - Bom dia
#Tarde - 12h às 19h - Boa tarde
#Noite - 19h às 24h - Boa noite


import datetime
def tempo_agr(nome):

    tempo_agr = datetime.datetime.now()

    if tempo_agr.hour >= 5 and tempo_agr.hour <= 12:
        print("Bom Dia", nome, "!!!")

    elif tempo_agr.hour >= 12 and tempo_agr.hour <= 19:
        print("Boa Tarde", nome , "!!!")

    elif tempo_agr.hour >= 18 and tempo_agr.hour < 5:
        print("Boa Noite", nome, "!!!")

    elif tempo_agr.hour >= 0 and tempo_agr.hour < 5:
        print("Boa Madrugada", nome, "!!!")

    else:
        print("algo deu errado")


nome = input("Digite um nome: ")

tempo_agr(nome)
