def ex1():
    idade = int(input("Informe a idade: "))
    if idade > 18 and idade < 67:
        print("Pode doar sangue")
    else:
        print("Não pode doar sangue")

def ex2():
    x = int(input("Informe o valor de X: "))
    y = int(input("Informe o valor de Y: "))
    z = int(input("Informe o valor de Z: "))

    if z >= x and  z <= y:
        print("O número está dentro do intervalo")
    else:
        print("Não está dentro do intervalo")

def ex3():
    a = int(input("Informe o valor de A: "))
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))

def ex4():
    a = int(input("Informe o plano de trabalho(1-3): "))
    salario = float(input("Informe o salário atual: "))
    match a:
        case 1:
            salario = salario + (salario * (10/100))
            print(f"O salário recebeu um aumento de 10%: {salario}")
        case 2:
            salario = salario + (salario * (15/100))
            print(f"O salário recebeu um aumento de 15%: {salario}")
        case 3:
            salario = salario + (salario * (20/100))
            print(f"O salário recebeu um aumento de 20%: {salario}")

def ex5():
    base = int(input("Informe o valor da base: "))
    n = int(input("Informe o expoente: "))
    result = 1
    contador = 0

    while contador != n:
        result = result * base
        contador += 1
    print(result)

def ex6():
    x = int(input("Informe o valor de X: "))
    y = int(input("Informe o valor de Y: "))
    option = int(input("Escolha a operação desejada: \n1. Média entre os números\n2. Difernça do maior pelo menor\n3. Produto entre os números\n4. Divisão do primeiro pelo segundo"))
    match option:
        case 1:
            print(f"A média de X e Y é: {(x + y) / 2}")
        case 2:
            if x > y:
                print(f"A diferença do maior pelo menor {x - y}")
            else: 
                print(f"A diferença do maior pelo menor {y - x}")
        case 3:
            print(f"O produto dos números é: {x * y}")
        case 4:
            print(f"A divisão dos números é: {x / y}")

def ex7():
    codigo = int(input("Informe o código do produto: "))

    match codigo:
        case 1:
            print("Alimento não perecível")
        case 2 |3 |4:
            print("ALimento perecível")
        case 5 | 6:
            print("Vestuário")
        case 7:
            print("Higiene Pessoal")
        case codigo if codigo >= 8 and codigo <= 15:
            print("Limpeza e Utensílios Domésticos")
        case _:
            print("Código invalido.")
        
def ex8():
    num = 100
    while num <= 450:
        num +1
        if num % 7 == 0:
            print(num)
        else:
            num +1

def ex9():
    n = int(input("Quantos números deseja inserir?"))
    soma = 0
    impar = 0
    contador = 0

    while contador < n:
        num = int(input(f"Informe o {contador + 1} número"))

        if num % 2 == 0:
            soma = soma + num
        else:
            impar += 1
        contador += 1

    print(f"A soma dos números pares é: {soma}")
    print(f"A quantidade de números ímpares digitados foi: {impar}")

def ex10():
    n = int(input("Dê o número fatorial: "))
    contador = 0
    num = 1
    fat = 1

    while contador < n:
        num = num * fat
        fat +=1
        contador +=1

    print(num)

def ex11():
    print("Não aguento mais")