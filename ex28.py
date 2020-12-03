nome = []
lanci = []
contatore = 1

while True:
    nome_candidato = input("inserire il nome dello studente " + str(contatore))
    lanci_candidato = input("inserire il numero di lanci di " + nome_candidato)
    nome.append(nome_candidato)
    lanci.append(lanci_candidato)
    contatore += 1
    domanda = int(input("vuoi inserire un nuovo candidato? Se si digita 1 se no digita 2"))

    if domanda == 1:
        break
    else:
        continue

print(max(lanci))
