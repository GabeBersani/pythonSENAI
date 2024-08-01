#2 - Conversor de Temperatura: Crie uma função que receba um valor de temperatura em graus Celsius
# como parâmetro e retorne o valor convertido para Fahrenheit e Kelvin.

def temperatura(temp_agr):

    fahrenheit = temp_agr * 1.8 + 32

    kelvin = temp_agr + 273.15

    print("A temperatura em ahrenheit é", fahrenheit, "e em kelvin é",  kelvin)


def solicita_temperatura():
    while True:
        try:
            temperatura = float(input("Digite a temperatura em graus Celsius: "))
            return temperatura
        except ValueError:
            print("Valor invalido, digite um número utilizando o ponto como separador. Ex: 1.0")




temp_agr = solicita_temperatura()
temperatura(temp_agr)
