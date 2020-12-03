citta = []
escursione_termica = []
massima = []
minima = []
contatore = 1
while True:
    nome = input("Inserire il nome della citta: ")
    citta.append(nome)
    valore = int(input("Inserire il valore di controllo per l'escursione termica: "))
    massim = int(input("Inserire la temperatura massima registrata: "))
    massima.append(massim)
    minim = int(input("Inserisci temperatura minima registrata: "))
    minima.append(minim)
    escursione = massim-minim
    print ("L'escursione termica e di: ", escursione, "gradi")
    escursione_termica.append(escursione)
    if citta == 1:
        contatore += 1
    else:
        continue
    if escursione_termica == valore:
        print("L'escursione termica presenta un valore accettabile")
    elif escursione_termica > valore:
        print("L'escursione termica e elevata")
        contatore +=1
    elif escursione_termica < valore:
        print("L'escursione termica presenta un valore basso")
    else:
        print("I valori inseriti non sono accettabili")
    print (citta)
    print (massima)
    print (minima)
    x= input("Se vuoi continuare scrivi 1, senno inserisci 0 ")
    if x== "0":
        break
    else:
        continue
print(contatore)