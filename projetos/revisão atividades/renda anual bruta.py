#8 - Solicite ao usuário o valor de sua renda anual bruta e, em seguida,
# calcule e exiba o desconto do Imposto de Renda de acordo com a tabela progressiva de 2024.

#Faixa de Renda Anual Bruta                           Alíquota
#Até R$ 56.072,00                                                0%
#De R$ 56.072,01 a R$ 238.532,00                    7,50%
#De R$ 238.532,01 a R$ 522.400,00                  15%
#De R$ 522.400,01 a R$ 987.600,00                 22,50%
#Acima de R$ 987.600,00                                   27,50%

print("Iremos solicitar ao usuario sua renda anual brura")
print("E em seguida vamos calcular o desconto do Imposto de Renda")

while True:
    try:
        print("Coloque ponto caso tenha centavos no seu valor")
        renda = float(input("Digite sua renda anual brura: "))


        if renda <= 56072:
            print("não tem imposto")

        elif renda >= 56072.01 and renda <= 238532:
            conta = renda * 0.075
            print("Imposto de Renda: ", conta)

        elif renda >= 238532.01 and renda <= 522400:
            conta1 = renda * 0.15
            print("Imposto de Renda: ", conta1)

        elif renda >= 522400.01 and renda <= 987600:
            conta2 = renda * 0.225
            print("Imposto de Renda: ", conta2)

        elif renda >= 987600.01:
            conta3 = renda * 0.275
            print("Imposto de Renda: ", conta3)

        else:
            ("algo deu errado tente novamente")

    except ValueError:
        # aso der erro executa aqui
        print("algo deu errado, digite um numero, ex: 1000")


