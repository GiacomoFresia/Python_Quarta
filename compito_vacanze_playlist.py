# Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
# (a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
# due playlist in una nuova.

def conta(playlist):
    n = 0
    for c in playlist:
        n = n + len(playlist[c])
    return n

def cerca(playlist, canzoneX):
    s = []
    for c in playlist:
        if canzoneX in playlist[c]:
            s.append(c)
    return s

def unisci_playlist(playlist, nome1, nome2):
    nuova = []
    for canzone in playlist[nome1]:
        nuova.append(canzone)
    for canzone in playlist[nome2]:
        nuova.append(canzone)
    return nuova

def main():
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }
    num = conta(playlist)
    print(f"Il numero di canzoni è: {num}")

    canzone_x = input("Inserisci il nome di una canzone: ")
    s = cerca(playlist, canzone_x)
    print(s)

    nome1 = input("Inserisci il nome di una playlist: ")
    nome2 = input("Inserisci il nome di una playlist: ")
    nuova = unisci_playlist(playlist, nome1, nome2)
    print(f"La nuova playlist è:\n{nuova}")

if __name__=="__main__":
    main()
    