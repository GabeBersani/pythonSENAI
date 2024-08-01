#2 - Solicite duas notas de um aluno e calcule a média. Se a média for maior ou igual a 70
# o aluno está aprovado. Caso  contrário, está reprovado.

print("Digite o valor de duas notas e vamos descobrir se você foi aprovado ou reprovado ")
print("")
print("se a média for maior ou igual a 70 o aluno está aprovado, caso  contrário, está reprovado.")
print("")

while True:
    try:
        nota1 = int(input("Digite a sua primeira nota: "))
        nota2 = int(input("Digite a sua segunda nota: "))
        soma = nota1 + nota2
        media = soma / 2

        if media >= 70:
            print("voce foi aprovado, sua nota foi", media)

        elif media < 70:
            print("você foi reprovado, sua nota foi", media)

        else:
            print("algo deu errado")


    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero inteiro")