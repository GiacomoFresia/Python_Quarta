# Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
# per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
# recente.

def cerca_autore(libri, autore):
    ris = []
    for libro in libri:
        if libro["autore"] == autore:
            ris.append(libro)
    return ris

def prezzo_medio(libri):
    somma = 0
    for libro in libri:
        somma = somma + libro["prezzo"]
    prezzo_medio = somma / len(libri)
    return prezzo_medio

def libro_piu_recente(libri):
    libro_piu_recente = libri[0]
    for libro in libri:
        if libro["anno"] > libro_piu_recente["anno"]:
            libro_piu_recente = libro
    return libro_piu_recente

def main():
    libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    autore_cercato = input("Inserisci il nome dell'autore cercato: ")
    libro_trovato = cerca_autore(libri, autore_cercato)
    print(f"Autore cercato: {autore_cercato}\nLibro trovato: {libro_trovato}")

    prezzo_m = prezzo_medio(libri)
    print(f"Il prezzo medio di tutti i libri è: {prezzo_m}")

    l_piu_recente = libro_piu_recente(libri)
    print(f"Il libro più recente è:\n{l_piu_recente}")

if __name__=="__main__":
    main()
