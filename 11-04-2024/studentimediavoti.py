def suddividi_per_media(studenti, intervalli):
    if len(intervalli) != 3 or intervalli[0] >= intervalli[1] or intervalli[1] >= intervalli[2]:
        print("Intervalli non validi.")
        return None
    
    studenti_per_media = {'basso': [], 'medio': [], 'alto': []}
    
    for key in studenti:
        for studente in studenti[key]:
            voti = studente[1]
            media = sum(voti) / len(voti) if voti else 0
            if media >= intervalli[2]:
                studenti_per_media['alto'].append(studente)
            elif media >= intervalli[1]:
                studenti_per_media['medio'].append(studente)
            else:
                studenti_per_media['basso'].append(studente)
    
    return studenti_per_media

def chiedi_dati_studenti():
    studenti = {}
    while True:
        gruppo = input("Inserisci la lettera di inizio e fine del gruppo di studenti (formato 'inizio-fine', lascia vuoto per terminare): ")
        if not gruppo:
            break
        inizio, fine = gruppo.split('-')
        cognomi = (inizio.lower(), fine.lower())
        studenti[cognomi] = []
        while True:
            nome = input("Inserisci il nome dello studente (lascia vuoto per terminare il gruppo): ")
            if not nome:
                break
            voti = []
            while True:
                voto = input("Inserisci un voto (lascia vuoto per terminare): ")
                if not voto:
                    break
                voti.append(int(voto))
            studenti[cognomi].append([nome, voti])
    return studenti

def chiedi_intervalli():
    intervalli = []
    while True:
        intervallo = input("Inserisci un intervallo di media (lascia vuoto per terminare, devi inserire esattamente tre intervalli): ")
        if not intervallo:
            if len(intervalli) == 3:
                break
            else:
                print("Devi inserire esattamente tre intervalli.")
                continue
        intervalli.append(int(intervallo))
    return intervalli

# Main
studenti = chiedi_dati_studenti()
intervalli = chiedi_intervalli()

studenti_divisi = suddividi_per_media(studenti, intervalli)
print(studenti_divisi)