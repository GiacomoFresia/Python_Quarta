# Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
# Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più
# presenze, (c) trovare chi era presente in una certa data.

def conta_presenze(presenze, nome):
    return len(presenze[nome])

def studente_piu_presente(presenze):
    massimo = 0
    studente_max = ""
    for studente in presenze:
        if len(presenze[studente]) > massimo:
            massimo = len(presenze[studente])
            studente_max = studente
    return studente_max

def presenti_in_data(presenze, data):
    ris = []
    for studente in presenze:
        if data in presenze[studente]:
            ris.append(studente)
    return ris

def main():
    presenze = {
        "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
        "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
        "Luca": ["2024-01-10", "2024-01-11"],
        "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }

    nome = input("Inserisci il nome: ")
    num_presenze = conta_presenze(presenze, nome)
    print(f"Numero di presenze: {num_presenze}")
    studente_max = studente_piu_presente(presenze)
    print(f"Studente con più presenze: {studente_max}")
    data = input("Inserisci una data: ")
    presenti = presenti_in_data(presenze, data)
    print(f"Presenti in quella data: {presenti}")

if __name__ == "__main__":
    main()