# 1) Faça um programa que converta uma temperatura em graus
# Fahrenheit para Celsius. A temperatura em Fahrenheit deverá
# ser lida do teclado. Utilize a fórmula C = (F - 32) * 5/9, onde F
# é a temperatura em Fahrenheit e C é a temperatura em
# Celsius.

def ex1():
    temp = int(input("Informe a tempera em graus Fahrenheit: "))
    print(f"A conversão de F para C é: {(temp - 32) * 5/9}")

def ex2():
    cota = 5.3
    valor = float(input("Informe o valor em dollar: "))
    print(f"O custo para cercar o terreno resultado da conversão é: {cota * valor}R$")

def ex3():
    km = float(input("Informe a distância percorrida em km: "))
    print(f"A conversão em metros é de: {km/3.6}")

def ex4():
    dias = int(input("Informe a quantidade de dias de serviço: "))

    valor_bruto = dias * 30
    desconto = valor_bruto * (8/100)
    valor_liquido = valor_bruto - desconto
    print(f"O custo para cercar o terreno valor para {dias} dias é de {valor_liquido}")

def ex5():
    degrau = float(input("Informe a altura do degrau: "))
    altura = float(input("Informe a altura a ser alcançada: "))
    print(f"A quantidade de degraus a subir: {altura / degrau}")

def ex6():
    tempo = float(input("Informe o tempo gasto: "))
    vm = float(input("Informe a velocidade média: "))
    print(f"Velocidade média: {vm} Tempo gasto: {tempo} Distância: {vm * tempo} Consumo: {(vm * tempo) / 12}L")

def ex7():
        c = float(input("Informe o comprimento: "))
        l = float(input("Informe a largura: "))
        p = float(input("Informe o preço do metro: "))
        area = c * l
        print(f"O custo para cercar o terreno é de: {area * p}")

def ex8():
     num = int(input("Digite um número inteiro de 3 digitos: "))
     unidade = num % 10
     dezena = (num // 10) % 10
     centena = num // 100 
     print(unidade,dezena,centena)
