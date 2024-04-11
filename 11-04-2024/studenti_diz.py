studenti = {}

while True:
    n_matricola = input("Inserisci il numero di matricola: ")

    if n_matricola in studenti:
        print("Studente già presente.")
        continue

    studente = {
        "nome": input("Inserisci il nome dello studente: "),
        "cognome": input("Inserisci il cognome dello studente: "),
        "esami_sostenuti": {}
    }

    while True:
        esame_sostenuto = input("Inserisci il nome dell'esame sostenuto: ")
        voto_esame = int(input("Inserisci il voto dell'esame: "))

        studente["esami_sostenuti"][esame_sostenuto] = voto_esame

        cont = input("Vuoi inserire un altro esame? (s/n): ")
        if cont.lower() == "n":
            break

    studenti[n_matricola] = studente

    cont = input("Vuoi inserire un altro studente? (s/n): ")
    if cont.lower() == "n":
        break

# Stampa il dizionario
for n_matricola, studente in studenti.items():
    print(f"\n--- Studente {n_matricola} ---")
    print(f"Nome: {studente['nome']}")
    print(f"Cognome: {studente['cognome']}")

    for esame, voto in studente["esami_sostenuti"].items():
        print(f"- {esame}: {voto}")
