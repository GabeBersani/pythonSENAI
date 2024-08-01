#7 - Solicite ao usuário um número de 1 a 12(representando um mês do ano)
# e exiba o nome correspondente ao mês (por exemplo, 1 para "Janeiro", 2 para "Fevereiro", etc.).

print("Iremos solicitar ao usuario um numero de 1 a 12 para representar os meses do ano")

while True:
    try:
        num_mes = int(input("Digite um numero para representar um mês do ano: "))

        if num_mes >= 13:
            print("esse numero é invalido, tente novamente")
        elif num_mes < 1:
            print("esse numero é invalido, tente novamente")
        elif num_mes == 1:
            print("jeneiro")
        elif num_mes == 2:
            print("fevereiro")
        elif num_mes == 3:
            print("março")
        elif num_mes == 4:
            print("abril")
        elif num_mes == 5:
            print("maio")
        elif num_mes == 6:
            print("junho")
        elif num_mes == 7:
            print("julho")
        elif num_mes == 8:
            print("agosto")
        elif num_mes == 9:
            print("setembro")
        elif num_mes == 10:
            print("outubro")
        elif num_mes == 11:
            print("novembro")
        elif num_mes == 12:
            print("dezembro")
        else:
            print("algo deu errado")
    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")