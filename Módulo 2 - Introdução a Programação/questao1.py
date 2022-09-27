nome = (input("Digite a idade do aluno(a): "))
n1 = float(input("Digite a primeira nota do aluno(a): "))
n2 = float(input("Digite a segunda nota do aluno(a): "))
faltas = int(input("Digite a quantidade de faltas do aluno(a): "))

media = (n1+n2)/2

if(media >=7 and faltas < 3):
    print("Aluno aprovado com média " , media , " e " , faltas , "faltas")
else:
    print("Aluno reprovado com média " , media , " e " , faltas , "faltas")

