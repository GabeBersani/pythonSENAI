#1 - Solicite um número ao usuário e verifica se o número é positivo ou negativo e exiba uma mensagem positivo ou negativo.

print("Digite um numero para descobrir se o numero é positivo ou negativo")
print("")

while True:
    try:
        numero = int(input("Digite um numero: "))

        if numero == 0:
            print("esse numero é neutro")

        elif numero > 0:
            print("esse numero é positivo")



        elif numero < 0:
            print("esse numero é negativo")


        else:
            print("algo deu errado")


    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")
