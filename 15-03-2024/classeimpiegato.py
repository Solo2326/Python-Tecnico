class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self):
        if self.stipendio <= 3000:
            self.stipendio *= 1.1  # Aumenta lo stipendio del 10%
        else:
            print("Stipendio già superiore a 3000€: aumento non applicato.")

    def stampa_stipendio(self):
        print("---- Prima dell'aumento ----")
        print("Nome:", self.nome, self.cognome)
        print("Matricola:", self.matricola)
        print("Stipendio: {:.2f}€".format(self.stipendio))

        print("\n---- Dopo l'aumento ----")
        self.aumenta_stipendio()
        print("Nome:", self.nome, self.cognome)
        print("Matricola:", self.matricola)
        print("Stipendio: {:.2f}€".format(self.stipendio))


# Inserimento dati da parte dell'utente
nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
matricola = input("Inserisci la tua matricola: ")
#verifaca che l'input di stipendio sia giusto se no messaggio errorre.
try:
    stipendio = float(input("Inserisci il tuo stipendio: "))
except ValueError:
    print("Errore: stipendio non valido.")
    exit()

# Crea la classe Impiegato.
impiegato = Impiegato(nome, cognome, matricola, stipendio)

# Stampa stipendio prima e dopo l'aumento
impiegato.stampa_stipendio()

