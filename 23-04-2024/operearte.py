import mysql.connector
from mysql.connector import Error
import getpass

def create_tables(database_name):
  connection = create_server_connect("localhost", "root", "")
  if connection:
    cursor = connection.cursor()
    cursor.execute("USE {}".format(database_name))

    # Create OPERA table
    create_opera_table_query = """
      CREATE TABLE OPERA (
        CodO INT PRIMARY KEY AUTO_INCREMENT,
        Nome VARCHAR(255) NOT NULL,
        Categoria VARCHAR(255) NOT NULL,
        Citta VARCHAR(255) NOT NULL,
        Nazione VARCHAR(255) NOT NULL,
        Autore VARCHAR(255) NOT NULL,
        FOREIGN KEY (Autore) REFERENCES AUTORE(CodA)
      );
    """
    cursor.execute(create_opera_table_query)

    # Create AUTORE table
    create_autore_table_query = """
      CREATE TABLE AUTORE (
        CodA INT PRIMARY KEY AUTO_INCREMENT,
        Nome VARCHAR(255) NOT NULL,
        Cognome VARCHAR(255) NOT NULL,
        Anno INT,
        Citta VARCHAR(255) NOT NULL
      );
    """
    cursor.execute(create_autore_table_query)

    connection.commit()
    print("Tabelle 'OPERA' e 'AUTORE' create correttamente")
    cursor.close()
    connection.close()
  else:
    print("Errore di connessione al database MySQL.")
