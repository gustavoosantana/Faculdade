def ex1():
    num = int(input("Informe o número: "))

    print("O resultado é:", (num * 3) - (2*(num+1)))

def ex2():
    b = float(input("Informe a base do triângulo: "))
    h = float(input("Informe a altura do triângulo: "))
    print("A área do triângulo é: ", (b * h) / 2)

def ex3():
    salario_atual = float(input("Informe o sálario atual: "))
    percent = float(input("Informe o percentual de reajuste (0 - 100): "))
    salario_novo = salario_atual * (percent/100)
    print("Novo sálario é igual a: ",salario_atual + salario_novo)

def ex4():
    aresta = float(input("Informe a aresta do cubo:"))
    volume = aresta ** 3
    print(f"O volume do cubo é: {volume}")

def ex5():
    dist = float(input("Informe a distância percorrida(KM): "))
    fuel = float(input("Informe o combustivél gasto(L): "))
    cons = dist / fuel
    print(f"O consumo foi de {cons}")

def ex6():
    comprimento = float(input("Informe o comprimento: "))
    largura = float(input("Informe a largura: "))
    preco = float(input("Preço do metro quadrado(R$): "))
    area = comprimento * largura
    print(f"O custo toal para forrar a sala é de {area * preco}")

def ex7():
    peso = float(input("Informe o peso em Kg: "))
    altura = float(input("Informe a altura em metros: "))
    print(f"O IMC é de: {peso / (altura**2)}")

def ex8():
    price = float(input("Informe a recompensa a ser dividada aos ganhadores:  "))
    ganhador1 = price * (46/100)
    ganhador2 = price * (32/100)
    ganhador3 =price * (22/100)
    print(f"Prêmios:\n Ganhador 1: {ganhador1}\n Ganhador 2: {ganhador2}\n Ganhador 3: {ganhador3}")

def ex9():
    valor_compra = float(input("Informe o valor da compra: "))
    valor_pago = float(input("Informe o valor pago: "))
    troco = valor_pago - valor_compra

    nota100 = troco // 100
    resto = troco % 100

    nota50 = resto // 50
    resto = resto % 50

    nota20 = resto // 20
    resto = resto % 20

    nota10 = resto // 10
    resto = resto % 10

    nota5 = resto // 5
    resto = resto % 5

    nota1 = resto // 1
    resto = resto % 1

    print(f"Compra: {valor_compra}\nValor pago: {valor_pago}\nTroco: {troco}\n\n 100R$: {nota100}\n 50R$: {nota50}\n 20R$: {nota20}\n 10R$: {nota10}\n 5R$: {nota5}\n 1R$: {nota1}")
ex9()