qtd_rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = float(input("Digite o peso bruto em KG: "))
qtd_pessoas = int(input("Digite a quantidade de pessoas que cabem no veículo: "))

if(qtd_rodas == 2 or qtd_rodas == 3):
    print("Habilitação categoria A")

if(qtd_rodas == 4 and qtd_pessoas <= 8 and peso <= 3500):
    print("Habilitação categoria B")

if(qtd_rodas >= 4 and peso >= 3500 and peso <= 6000):
    print("Habilitação categoria C")

if(qtd_rodas >=4 and qtd_pessoas > 8):
    print("Habilitação categoria D")

if(qtd_rodas >=4 and peso > 6000):
    print("Habilitação categoria E")