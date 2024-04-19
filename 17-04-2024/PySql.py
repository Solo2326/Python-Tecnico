import mysql.connector
from mysql.connector import Error
import getpass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

def connetti_al_server(host_name, nome_utente, password):
    """Stabilisce una connessione al server MySQL."""
    connessione = None
    try:
        connessione = mysql.connector.connect(
            host=host_name,
            user=nome_utente,
            password=password
        )
        print("Connessione al server avvenuta con successo")
    except mysql.connector.Error as err:
        print(f"Errore di connessione: '{err}'")
    return connessione

def crea_database(connessione, nome_database):
    """Crea un database, se non esiste già."""
    if connessione:
        cursore = connessione.cursor()
        query_creazione_database = f"CREATE DATABASE IF NOT EXISTS {nome_database}"
        try:
            cursore.execute(query_creazione_database)
            connessione.commit()
            print(f"Database '{nome_database}' creato correttamente")
        except mysql.connector.Error as err:
            print(f"Errore nella creazione del database: '{err}'")
        finally:
            cursore.close()
    else:
        print("Errore: connessione al database non fornita.")

def crea_tabella(connessione, nome_database, nome_tabella, schema_tabella):
    """Crea una tabella nel database specificato."""
    if connessione:
        cursore = connessione.cursor()
        try:
            cursore.execute(f"USE {nome_database}")
            query_creazione_tabella = f"""
                CREATE TABLE IF NOT EXISTS {nome_tabella} (
                    {schema_tabella}
                ); 
            """
            cursore.execute(query_creazione_tabella)
            connessione.commit()
            print(f"Tabella '{nome_tabella}' creata con successo")
        except mysql.connector.Error as err:
            print(f"Errore nella creazione della tabella: '{err}'")
        finally:
            cursore.close()
    else:
        print("Errore: connessione al database non fornita.")

def inserisci_dati(connessione, nome_database, nome_tabella, dati):
    """Inserisci i dati in una tabella."""
    if connessione:
        cursore = connessione.cursor()
        cursore.execute(f"USE {nome_database}")

        colonne = ', '.join([col[0] for col in cursore.description])
        segnaposto = ', '.join(['%s'] * len(dati[0]))
        query_inserimento = f"INSERT INTO {nome_tabella} ({colonne}) VALUES ({segnaposto})"

        try:
            cursore.executemany(query_inserimento, dati)
            connessione.commit()
            print("Dati inseriti con successo")
        except mysql.connector.Error as err:
            print(f"Errore nell'inserimento dei dati: '{err}'")
        finally:
            cursore.close()
    else:
        print("Errore: connessione al database non fornita.")

def recupera_dati(connessione, nome_database, nome_tabella):
    """Recupera tutti i dati da una tabella."""
    dati = None
    if connessione:
        cursore = connessione.cursor()
        cursore.execute(f"USE {nome_database}")
        query_recupero = f"SELECT * FROM {nome_tabella}"
        cursore.execute(query_recupero)
        dati = cursore.fetchall()
        cursore.close()
    else:
        print("Errore: connessione al database non fornita.")
    return dati

def stampa_report(dati):
    """Stampa un report contenente i dati recuperati."""
    if dati:
        print("Report Dati:")
        for riga in dati:
            print(riga)
    else:
        print("Nessun dato da stampare.")

def main():
    """Menu principale per l'interazione con il database."""
    while True:
        print("\nMenu:")
        print("1. Connetti al server")
        print("2. Crea database")
        print("3. Crea tabella")
        print("4. Inserisci dati")
        print("5. Recupera dati")
        print("6. Stampa report")
        print("7. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            nome_host = input("Inserisci il nome host del server: ")
            nome_utente = input("Inserisci il nome utente: ")
            password = getpass.getpass("Inserisci la password: ")
            connessione = connetti_al_server(nome_host, nome_utente, password)

        elif scelta == '2':
            if connessione:
                nome_database = input("Inserisci il nome del database da creare: ")
                crea_database(connessione, nome_database)
            else:
                print("Errore: connessione al database non stabilita.")

        elif scelta == '3':
            if connessione:
                nome_database = input("Inserisci il nome del database: ")
                nome_tabella = input("Inserisci il nome della tabella: ")
                schema_tabella = input("Inserisci lo schema della tabella (colonne e tipi): ")
                crea_tabella(connessione, nome_database, nome_tabella, schema_tabella)
            else:
                print("Errore: connessione al database non stabilita.")

        elif scelta == '4':
            if connessione:
                nome_database = input("Inserisci il nome del database: ")
                nome_tabella = input("Inserisci il nome della tabella: ")
                # Struttura per raccogliere i dati da inserire (personalizzala)
                dati = []  # Esempio: lista di tuple (nome, cognome, ...)
                inserisci_dati(connessione, nome_database, nome_tabella, dati)
            else:
                print("Errore: connessione al database non stabilita.")

        elif scelta == '5':
            if connessione:
                nome_database = input("Inserisci il nome del database: ")
                nome_tabella = input("Inserisci il nome della tabella: ")
                dati_recuperati = recupera_dati(connessione, nome_database, nome_tabella)
                stampa_report(dati_recuperati)
            else:
                print("Errore: connessione al database non stabilita.")

        elif scelta == '6':
            if connessione:
                nome_database = input("Inserisci il nome del database: ")
                nome_tabella = input("Inserisci il nome della tabella: ")
                dati_recuperati = recupera_dati(connessione, nome_database, nome_tabella)
                stampa_report(dati_recuperati)
            else:
                print("Errore: connessione al database non stabilita.")

        elif scelta == '7':
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == '__main__':
    main()

