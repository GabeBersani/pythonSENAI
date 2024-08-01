#Utiliza a bliblioteca datetime para mostrar o ano, mes e dia da semana
# pegar o horario atual e dar uma saudação para o usuario

import datetime
while True:
    try:
        tempo_agr = datetime.datetime.now()
        semana = tempo_agr.strftime("%A")
        mes = tempo_agr.strftime("%B")
        print("")
        print("Bem vindo a biblioteca datetime!!!")
        escolha = int(input("\n [1] Dia, Mes e ano \n [2] horas \n [3] dia da semana "
                            "\n Digite qual deseja ver:"))
        if escolha == 1:
            if "January" == mes:
                trad_mes = "janeiro"
            elif "February" == mes:
                trad_mes = "fevereiro"
            elif "March" == mes:
                trad_mes = "março"
            elif "April" == mes:
                trad_mes = "abril"
            elif "May" == mes:
                trad_mes = "maio"
            elif "June" == mes:
                trad_mes = "junho"
            elif "July" == mes:
                trad_mes = "julho"
            elif "August" == mes:
                trad_mes = "agosto"
            elif "September" == mes:
                trad_mes = "setembro"
            elif "October" == mes:
                trad_mes = "outubro"
            elif "November" == mes:
                trad_mes = "novembro"
            elif "December" == mes:
                trad_mes = "dezembro"
            print("O Dia é:",tempo_agr.day, "Mes:",trad_mes, "Ano:",tempo_agr.year )

        elif escolha == 2:
            if tempo_agr.hour >= 5 and tempo_agr.hour <= 12:
                print("Bom Dia!!!")
            elif tempo_agr.hour >= 12 and tempo_agr.hour <= 18:
                print("Boa Tarde!!!")
            elif tempo_agr.hour >= 18 and tempo_agr.hour < 5:
                print("Boa Noite!!!")
            print("A hora atual é:", tempo_agr.hour, "horas", tempo_agr.minute, "minutos", tempo_agr.second,
                  "segundos")

        elif escolha == 3:
            if "Monday" == semana:
                traducao = "segunda"
            elif "Tuesday" == semana:
                traducao = "terça"
            elif "Wednesday" == semana:
                traducao = "quarta"
            elif "Thursday" == semana:
                traducao = "quinta"
            elif "Friday" == semana:
                traducao = "sexta"
            elif "Saturday" == semana:
                traducao = "sabado"
            elif "Sunday" == semana:
                traducao = "domingo"
            print("O dia da semana atual é:", traducao)

        else:
            print("algo deu errado")

    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero, 1, 2 ou 3")







