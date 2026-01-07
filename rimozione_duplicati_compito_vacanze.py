# Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
# mantenendo l’ordine di prima apparizione.

def rimozione_duplicati(elementi):
    lista = []
    for e in elementi:
        if e in lista:
            pass
        else:
            lista.append(e)
    return lista

def main():
    elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
    lista = rimozione_duplicati(elementi)
    print(f"La lista senza i duplicati è: {lista}")

if __name__=="__main__":
    main()