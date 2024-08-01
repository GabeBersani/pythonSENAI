#5 - Solicite ao usuário um número de 1 a 7(representando um dia da semana) e exiba o nome correspondente ao dia
# (por exemplo, 1 para "Domingo", 2 para "Segunda-feira", etc.).

print("Iremos solicitar um número de 1 a 4 para podermos reprezentar os dias de semana")
print("")
while True:
    try:
        num_semana = int(input("Digite um numero para representar o dia de semana: "))

        if num_semana >= 8:
            print("esse numero é invalido, tente novamente")
        elif num_semana < 1:
            print("esse numero é invalido, tente novamente")
        elif num_semana == 1:
            print("domingo")
        elif num_semana == 2:
            print("segunda")
        elif num_semana == 3:
            print("terça")
        elif num_semana == 4:
            print("quarta")
        elif num_semana == 5:
            print("quinta")
        elif num_semana == 6:
            print("sexta")
        elif num_semana == 7:
            print("sabado")
        else:
            print("algo deu errado")
    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")