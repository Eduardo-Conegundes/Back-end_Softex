def calculadora(n1, n2, opr):
   
    if(opr == 1):
        resultado = n1 + n2
        print (resultado)
    elif(opr == 2):
        resultado = n1 - n2
        print (resultado)
    elif (opr == 3):
        resultado = n1 * n2
        print (resultado)
    elif (opr == 4):
        resultado = n1 / n2
        print (resultado)
    else:
        resultado = 0
        print(resultado)

print("Digite o número da operação que deseja realizar")
print("[1]Soma") 
print("[2]Subtração") 
print("[3]Multiplicação") 
print("[4]Divisão")
opr = int(input(""))    

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calculadora( n1, n2 , opr )
