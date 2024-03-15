#Funzione per il controllo
def numero_triangolare(numero):
    somma = 0
    k = 1

    while somma < numero:
        somma += k
        k += 1

    return somma == numero

# Acquisizione dell'input come intero
numero = int(input("Inserisci un numero: "))
#STampa
if numero_triangolare(numero):
    print(f"Il numero {numero} è triangolare.")
else:
    print(f"Il numero {numero} non è triangolare.")
