print("Calculadora da Lei de Ohm")
calculo = int(input(" [1] Corrente eletrica \n [2] Resistência Elétrica \n [3] Tensão Elétrica \n [4] Resistência resistor \n Digite"
                    " qual medida deseja calcular:"))

while calculo != 0:

    if calculo == 1:
        while True:
            try:
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


    elif calculo == 2:
        while True:
            try:
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

    elif calculo == 3:
        while True:
            try:
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

    elif calculo == 4:

        while True:
            try:
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
                if TensaoL > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")

        calculo4 = TensaoF - TensaoL
        calculo5 = calculo4 / CorrenteL
        print("o valor da Resistência resistor é", calculo5, "Ohms")
    calculo = int(input("\n [1] Corrente eletrica \n [2] Resistência Elétrica \n [3] Tensão Elétrica \n [4] Resistência resistor \n Digite qual medida deseja calcular:"))

else:
    print("não foi possível realizar essa conta")



