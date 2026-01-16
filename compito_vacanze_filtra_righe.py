# Leggere un file e scrivere su un nuovo file solo le righe che contengono una certa parola chiave.

def crea_file(parola):
    file = open("compito_vacanze_log.txt", "r", encoding='utf-8')
    testo = file.read().lower()
    file.close()

    righe = testo.split("\n")
    file_nuovo = open("compito_vacanze_log_nuovo.txt", "w", encoding='utf-8')
    for riga in righe:
        if parola in riga:
            file_nuovo.write(riga + "\n")
    file_nuovo.close()

def main():
    parola = input("Inserisci una parola: ")
    parola = parola.lower()
    crea_file(parola)

if __name__=="__main__":
    main()