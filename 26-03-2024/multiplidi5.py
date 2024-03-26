#POPOLARE UNA LISTA DI N ELEMENTI CON I PRIMI N MULTIPLI DI 5 ESCLUDENDO LO ZERO. DOPO AVER TERMINATO L'INSERIMENTO VISUALIZZARE IN OUTPUT I VALORI DELLA LISTA E IL RELATIVO INDICE.

listamultipli = []
n = int(input("Inserisci quanti n multipli di 5 stampare.\n\n"))
for i in range(1, n + 1):   #ciclo + inserimento del multiplo 
    multiplo = i * 5
    listamultipli.append(multiplo)


for i, valore in enumerate(listamultipli): #stampa
    print(f"Indice: {i+1} - Valore: {valore}")
