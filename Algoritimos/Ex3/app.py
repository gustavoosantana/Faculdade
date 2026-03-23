def ex1():
    num = float(input("Informe o número: "))
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

def ex2():
    num = float(input("Informe o número: "))
    if num % 5 == 0:
        print("O número é multiplo de 5")
    else:
        print("O número não é multiplo de 5")

def ex3():
    a = float(input("Informe o valor A: "))
    b = float(input("Informe o valor B: "))
    if a == b:
        c = a + b
        print(c)
    else:
        c = a * b
        print(c)

def ex4():
    salario = float(input("Informe o sálario: "))
    if salario <= 500:
        desconto = salario * (15/100)
        valor = salario - desconto
        print(f"O reajuste foi para {valor}")
    elif salario >= 500 and salario <= 1000:
        desconto = salario * (10/100)
        valor = salario - desconto
        print(f"O reajuste foi para {valor}")
    else:
        desconto = salario * (5/100)
        valor = salario - desconto
        print(f"O reajuste foi para {valor}")
        
def ex5():
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe o segundo número: "))
    
    if num1 % num2 == 0:
        print("O número é divisível pelo segundo")
    else:
        print("O número não é divisível pelo segundo")

def ex6():
    produto = float(input("Informe o preço do produto: "))
    if produto >= 100:
        produto = produto - (produto * (10/100))
        print(f"O produto sofreu um desconto de 10%: {produto}")
    else: 
        print(f"O produto não sofre alteração no preço: {produto}")

def ex7():
    senha = int(input("Informe a senha: "))
    if senha == 2026:
        print("Logado")
    else:
        print("Erro")

def ex8():
    salario_bruto = float(input("Informe o salário: "))
    prestacao = float(input("Informe o valor da prestação do empréstimo: "))
    tempo = int(input("Informe o tempo de serviço: "))

    if prestacao > salario_bruto * (30/100):
        print("Negado")
        print(salario_bruto * (30/100))
    elif tempo > 2: 
        print("Aprovado com bônus")
    else:
        print("Aprovado")

def ex9():
    idade = int(input("Informe a idade do lutador"))
    peso = float(input("Informe o peso: "))
    if idade < 18:
        print("Categoria juvenil")
    elif peso < 80:
        print("Peso Médio")
    else:
        print("Peso Pesado")

def ex10():
    salario = float(input("Informe o salário: "))
    if salario <= 1500:
        salario = salario + (salario * 15/100)
        print(f"O Salário recebeu aumento de 15%: {salario}")
    elif salario <= 3000:
        salario = salario + (salario * 10/100)
        print(f"O Salário recebeu aumento de 10%: {salario}")
    else: 
        salario = salario + (salario * 5/100)
        print(f"O Salário recebeu aumento de 5%: {salario}")

def ex11():
    x = int(input("Informe o valor X: "))
    y = int(input("Informe o valor Y: "))
    if x < 0 and y > 0:
        print("O número está no segundo quadrante Q2")
    elif x > 0 and y > 0:
        print("O número está no primeiro quadrante Q1")
    elif x < 0 and y < 0:
        print("O número está no terceiro quadrante Q3")
    elif x > 0 and y < 0:
        print("O número está no quarto quadrante Q4")
    else:
        print("O número está na origem 0,0")

def ex12():
    l1 = float(input("Informe o primeiro lado do triângulo: "))
    l2 = float(input("Informe o segndo lado do triângulo: "))
    l3 = float(input("Informe o terceiro lado do triângulo: "))
    verificacao =  l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 
    if verificacao == True and l1 == l2 == l3:
        print("O triângulo é equilatero")
    elif verificacao == True and l1 == l2 or l1 == l3 or l2 == l3:
        print("O triângulo é isósceles")
    elif verificacao == True and l1 != l2 and l1 != l3 and l2 != l3:
        print("O triângulo é escaleno")
    else: 
        print("Não é um triângulo")

def ex13():
    a = float(input("Informe o valor A: "))
    b = float(input("Informe o valor B: "))
    c = float(input("Informe o valor C: "))

    delta = b ** 2 - (4 * a * c)
    
    if delta > 0:
        x = -b / (2 * a)
        print(f"Uma raiz {x}")
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Raiz 1: {x1}")
        print(f"Raiz 2 {x2}")