#6 - Solicite ao usuário três números inteiros e mostre o maior deles.

print("Iremos solicitar ao usuário três números inteiros e mostraremos o maior deles")
print("")

while True:
    try:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        num3 = int(input("Digite o terceiro numero: "))

        if num1 > num2 and num1 > num3:
            print("o primeiro numero é o maior")

        elif num2 > num1 and num2 > num3:
            print("o segundo numero é maior")

        elif num3 > num1 and num3 > num2:
            print("o terceiro numero é maior")

        else:
            print("algo deu errado")


    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")