# O while repete tudo que esta dentro dele
while True:
    # O Try vai tentar executar esse bloco de codigo
    try:
        idade = int(input('Digite sua idade: '))

        #O if verifica se a idade é valida
        if idade > 0 and idade < 100:
            print("Idade:", idade)
            # O breal sai do while
            break
        else:
            print("Idade invalida")
    except ValueError:
        # aso der erro executa aqui
        print("Digite sua idade em numero. Ex: 26")
