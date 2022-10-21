x = 0
y = 0
z = 0
nulo = 0

stop = False
while stop == False:

    stop_voto = False
    print("=== VOTAÇÃO ===")
    print("\nDigite o número do candidato que deseja votar: ")
    print("\nCandidato X = 889")
    print("\nCandidato Y = 847")
    print("\nCandidato Z = 515")
    print("\nBranco ou nulo = 0")
    
    try:
        voto = int(input("\nDigite o número do candidato que deseja votar: "))

        def votacao(voto):
            if (voto == 889):
                res = "Candidato X"
            elif (voto == 847):
                res = "Candidato Y"
            elif (voto == 515):
                res = "Candidato Z"
            else:
                res = "Branco ou Nulo"
            return res

        count = votacao(voto)

        if (count == "Candidato X"):
            x = (x + 1)
        elif (count == "Candidato Y"):
            y = (y + 1)
        elif (count == "Candidato Z"):
            z = (z + 1)
        else:
            nulo = (nulo + 1)

        stop_confirmacao = False
        while stop_confirmacao == False:
            
            print("\nVocê votou no candidato: ",count)

            parar_votacao = str (input("\nDeseja parar a votação?? [s/n]: "))
            if (parar_votacao == "s" or parar_votacao == 'S'):
                stop = True
                stop_confirmacao = True
                print("\nVotação concluída")
            elif (parar_votacao == "n" or parar_votacao == 'N'):
                stop_confirmacao = True
            else:
                print("\nOpção inválida")
                print("\nResponda novamente")
    except:
        print("\nCandidato inválido.")

if (x > y) and (x > z):
    print("\nO candidato X foi eleito")
elif (y > x) and (y > z):
    print("\nO candidato Y foi eleito")
elif (z > x) and (z > y):
    print("\nO candidato Z foi eleito")
else:
    print("\nA votação empatou !!!!")

print("\n+++ RESULTADOS +++")
print("\nO candidato X teve", x,"voto(s)")
print("O candidato Y teve", y,"voto(s)")
print("O candidato Z teve", z,"voto(s)")
print( nulo,"voto(s) branco(s) ou nulo(s)")
