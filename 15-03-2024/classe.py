class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} {self.cognome} e ho {self.eta} anni.")

# Creazione di oggetti Persona
persona1 = Persona(input("Inserisci nome: "), input("Inserisci cognome: "), int(input("Inserisci età: ")))
persona2 = Persona(input("Inserisci nome: "), input("Inserisci cognome: "), int(input("Inserisci età: ")))
persona3 = Persona(input("Inserisci nome: "), input("Inserisci cognome: "), int(input("Inserisci età: ")))

# Stampa informazioni
persona1.saluta()
persona2.saluta()
persona3.saluta()











