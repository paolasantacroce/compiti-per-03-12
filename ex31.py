numero = int(input("Inserire il numero decimale da trasformare"))
n = binario = []
quoziente = 1
while True:
    if numero == 0 or quoziente == 0:
        break
    elif quoziente <= numero:
        quoziente = round(numero / 2)
        resto =numero%2
        binario.append(resto)
        numero = quoziente
    else: 
        numero = round(quoziente / 2)
        resto = quozeinte%2
        binario.append(resto)
        quoziente = numero
binario.reverse()
print(binario) 


