#4 - Solicite dois números e verifica qual deles é o maior e exiba uma mensagem correspondente.

print("Vamos solicitar dois números ao usuario e verificar qual deles é o maior ")
print("")

while True:
    try:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))

        if num1 > num2:
            print("o primeiro numero é maior", num1)

        elif num2 > num1:
            print("o segundo numero é maior", num2)

        elif num1 == num2:
            print("os numeros são iguais")

        else:
            print("algo deu errado")


    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")