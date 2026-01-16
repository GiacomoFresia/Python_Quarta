# Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
# Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più
# presenze, (c) trovare chi era presente in una certa data.

def conta(presenze, nome):
    n_presenze = 0
    for studente in presenze:
        if nome == studente:
            n_presenze = len(presenze[nome])
    return n_presenze

def piu_presenze(presenze):
    n_max = 0
    for studente in presenze:
        num = len(presenze[studente])
        if num > n_max:
            n_max = num
            nome_max = studente
    return n_max, nome_max

def presente_in_data(presenze, data):
    nomi = []
    for studente in presenze:
        if data in presenze[studente]:
            nomi.append(studente)
    return nomi

def main():
    presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }

    nome = input("Inserisci il nome: ")
    num_presenze = conta(presenze, nome)
    print(f"Il numero di presenze di {nome} è {num_presenze}")

    max_presenze, max_nome = piu_presenze(presenze)
    print(f"Lo studente con piu presenze è: {max_nome} con {max_presenze} presenze")

    dataX = input("Inserisci una data: ")
    nomi = presente_in_data(presenze, dataX)
    print(f"Studenti presenti in data {dataX}: {nomi}")

if __name__=="__main__":
    main()