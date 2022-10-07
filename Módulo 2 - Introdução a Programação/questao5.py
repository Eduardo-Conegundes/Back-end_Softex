def calculadora(opr, n1,n2):
    if opr == 1:
        print(f'\nResultado: {n1 + n2}\n')

    elif opr == 2:
        print(f'\nResultado: {n1 - n2}\n')

    elif opr == 3:
        print(f'\nResultado: {n1 * n2}\n')

    elif opr == 4:
        print(f'\nResultado: {n1 / n2}\n')

opr = 1

while opr:
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[0] Sair")
    opr = int(input("\nEscolha a operação a ser realizada: "))

    if opr == 0:
        print("Programa encerrado !!!")
        exit()

    elif 1 <= opr <= 4:
        n1 = float(input("Insira o primeiro número: "))
        n2 = float(input("Insira o segundo número: "))

        calculadora(opr, n1, n2)
    
    else:
        print("\nValor da operação é inválido !!!")
