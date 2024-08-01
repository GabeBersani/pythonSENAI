#4 - Classificador de triangulo: Crie uma função que receba três números
#como parâmetros que serão os lados de um triângulo e retorne se ele é equilátero, isósceles ou escaleno.

#Equilátero se todos os lados possuem a mesma medida.
#Isósceles se dois lados possuem a mesma medida.
#Escaleno se todos os lados possuem medidas diferentes.

#valor dos lados:
def preimeiro_lado():
    while True:
        try:
            lado1 = int(input("Digite o primeiro lado do triângulo: "))
            return lado1
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

def segundo_lado():
    while True:
        try:
            lado2 = int(input("Digite o segundo lado do triângulo: "))
            return lado2
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

def terceiro_lado():
    while True:
        try:
            lado3 = int(input("Digite o terceiro lado do triângulo: "))
            return lado3
        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")

def conta_lados(lado1, lado2, lado3):
    while True:
        try:
            if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
                triangulo = "O triângulo apresentado é equilátero"
                print(triangulo)

            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
              triangulo = "O triângulo apresentado é isóceles"
              print(triangulo)

            elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
              triangulo = "O triângulo apresentado é escaleno"
              print(triangulo)

            else:
              print("As informações inseridas estão incorretas")
            break

        except ValueError:
            print("Valor invalido, digite um número. Ex: 1")



conta_lados(preimeiro_lado(), segundo_lado(), terceiro_lado())