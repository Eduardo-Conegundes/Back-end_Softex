from datetime import date

stop = False
while stop == False:
    
    try:
        data = date.today()
        ano_atual = int(data.strftime('%Y'))

        nome = str (input("\nDigite seu nome: "))
        ano = int (input("\nInsira o ano do seu nascimento: "))
        
        if (ano >= 1922) and (ano <= 2021):
            idade = ano_atual - ano
            print(nome + " tem ", idade ," anos ou completará em", ano_atual)
            stop = True
    
    except:
        print("\nOs dados inseridos são invalidos!!")
        print("\nInsira seus dados novamente!!")
