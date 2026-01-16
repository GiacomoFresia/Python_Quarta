# Una lista contiene dizionari con chiavi titolo, regista, anno, durata (in minuti).
# Scrivere funzioni per:
# (a) trovare tutti i film di un certo regista
# (b) calcolare la durata media dei film
# (c) trovare il film più vecchio

def trova_film(film, nome):
    lista = []
    for f in film:
        if nome == f["regista"]:
            lista.append(f)
    return lista

def durata_media(film):
    durata = 0
    for f in film:
        durata = durata + f["durata"]
    durata_m = durata / len(film)
    return durata_m

def film_piu_vecchio(film):
    anno_min = 3000
    for f in film:
        if f["anno"] < anno_min:
            anno_min = f["anno"]
            film_min = f
    return film_min

def main():
    film = [
        {"titolo": "Inception", "regista": "Christopher Nolan", "anno": 2010, "durata": 148},
        {"titolo": "Interstellar", "regista": "Christopher Nolan", "anno": 2014, "durata": 169},
        {"titolo": "Pulp Fiction", "regista": "Quentin Tarantino", "anno": 1994, "durata": 154},
        {"titolo": "Django Unchained", "regista": "Quentin Tarantino", "anno": 2012, "durata": 165},
        {"titolo": "The Matrix", "regista": "Lana Wachowski", "anno": 1999, "durata": 136}
    ]

    nome = input("Nome del regista: ")
    lista_film = trova_film(film, nome)
    print(lista_film)

    durataM = durata_media(film)
    print(f"La durata media dei film è: {durataM}")

    f = film_piu_vecchio(film)
    print(f"Il film più vecchio è:\n{f}")

if __name__=="__main__":
    main()