import requests

class ConvertitoreBinario:

    def __init__(self):
       
        pass

    def binario_a_decimale(self, num_bin):
        """
        Converte un numero binario in decimale.

        Args:
            num_bin: Il numero binario da convertire.

        Returns:
            Il numero decimale equivalente.
        """
        try:
            # Conversione tramite API
            risposta = requests.get(f"https://networkcalc.com/api/binary/{num_bin}")
            if risposta.status_code == 200:
                data = risposta.json()
                if 'converted' in data:
                    return data['converted']
        except requests.exceptions.ConnectionError:
            print("**ATTENZIONE: Connessione API non disponibile. Conversione manuale in corso...**")

        # Conversione manuale
        return self.converti_binario_decimale_manuale(num_bin)

    def converti_binario_decimale_manuale(self, num_bin):
        """
        Converte manualmente un numero binario in decimale.

        Args:
            num_bin: Il numero binario da convertire.

        Returns:
            Il numero decimale equivalente.
        """
        valore_esadecimale = "0123456789ABCDEF"
        lunghezza_binario = len(num_bin)
        valore_decimale = 0
        potenza_due = 1
        for i in range(lunghezza_binario-1, -1, -1):
            valore_decimale += int(num_bin[i]) * potenza_due
            potenza_due *= 2
        indice_esadecimale = valore_decimale % 16
        quoziente = valore_decimale // 16
        numero_esadecimale = valore_esadecimale[indice_esadecimale]
        while quoziente > 0:
            indice_esadecimale = quoziente % 16
            quoziente //= 16
            numero_esadecimale = valore_esadecimale[indice_esadecimale] + numero_esadecimale
        return numero_esadecimale

    def conta_zeri_uno(self, num_bin):
        """
        Conta il numero di zeri e uno in un numero binario.

        Args:
            num_bin: Il numero binario da analizzare.

        Returns:
            Il numero di zeri e uno in una tupla.
        """
        num_zero = num_bin.count('0')
        num_uno = num_bin.count('1')
        return num_zero, num_uno

# Funzione main

def main():
    convertitore = ConvertitoreBinario()
    num_bin = input("Inserisci un numero binario: ")
    decimale = convertitore.binario_a_decimale(num_bin)
    print("Decimale (manuale):", decimale)
    num_zero, num_uno = convertitore.conta_zeri_uno(num_bin)
    print("Numero di 0 nel numero binario:", num_zero)
    print("Numero di 1 nel numero binario:", num_uno)

# Avvio del programma

if __name__ == "__main__":
    main()
