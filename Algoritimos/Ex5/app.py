def ex1():
    int1 = 0 
    int2 = 0 
    int3 = 0  
    int4 = 0
    
    while True:
        num = float(input("Digite o número (Ou negativbo para sair): "))

        if 0 <= num <= 25:
            int1 += 1
        elif 26 <= num <= 50:
            int2 += 1
        elif 51 <= num <= 75:
            int3 += 1
        elif 76 <= num <= 100:
            int4 += 1
        
        if num < 0:
            break
    print(f"Intervalo 1: {int1}  Intervalo 2: {int2}  Intervalo 3: {int3}  Intervalo 4: {int4}")

def ex2():
    num = int(input("Digite o número: "))

    while num >= 0:
        if num % 4 == 0:
            print(num)
            num -= 4
        else:
            num -= num % 4
            print(num)