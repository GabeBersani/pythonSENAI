

def calculadora_escolha():
    while True:
        try:
            escolha = int(input(" [1] Corrente eletrica \n [2] Resistência Elétrica "
                        "\n [3] Tensão Elétrica \n [4] Resistência resistor \n Digite"
                        " qual medida deseja calcular:"))
            return escolha
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")


def calculo_1(escolha):
    while True:
        try:
            if escolha == 1:
                V = float(input("Digite a Tensão em volts: "))
                if V > 0:
                    break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    while True:
        try:
            R = float(input("Digite a Resistencia em Ohms: "))
            if R > 0:
                break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    calculo1 = V / R
    print("o valor da Corrente eletrica é", calculo1, "A (amperes)")

def calculo_2(escolha):
    while True:
        try:
            if escolha == 2:
                V = float(input("Digite a Tensão em volts: "))
                if V > 0:
                    break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")
    while True:
        try:
            I = float(input("Digite a Corrente Elétrica: "))
            if I > 0:
                break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    calculo2 = V / I
    print("o valor da Resistência Elétrica é", calculo2, "Ohms")

def calculo_3(escolha):
    while True:
        try:
            if escolha == 3:
                R = float(input("Digite a Resistência Elétrica:: "))
                if R > 0:
                    break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    while True:
        try:
            I = float(input("Digite a Corrente Elétrica: "))
            if I > 0:
                break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    calculo3 = R * I
    print("o valor da Tensão Elétrica é", calculo3, "V (volts)")


def calculo_4(escolha):
    while True:
        try:
            if escolha == 4:
                TensaoF = float(input("Digite a Tensão da fonte: "))
                if TensaoF > 0:
                    break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    while True:
        try:
            TensaoL = float(input("Digite a Tensão do LED: "))
            if TensaoL > 0:
                break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    while True:
        try:
            CorrenteL = float(input("Digite a Corrente do LED: "))
            if CorrenteL > 0:
                break
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

    calculo4 = TensaoF - TensaoL
    calculo5 = calculo4 / CorrenteL
    print("o valor da Resistência resistor é", calculo5, "Ohms")


while True:
    print("Bem vindo ao calculadora Ohm")
    escolha = calculadora_escolha()
    if escolha == 1:
        calculo_1(escolha)
    elif escolha == 2:
        calculo_2(escolha)
    elif escolha == 3:
        calculo_3(escolha)
    elif escolha == 4:
        calculo_4(escolha)

