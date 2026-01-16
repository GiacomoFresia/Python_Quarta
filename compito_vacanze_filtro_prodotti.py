# Una lista contiene dizionari con chiavi nome, categoria, prezzo. Scrivere una funzione
# che restituisca solo i prodotti di una certa categoria con prezzo inferiore a un valore dato.

def prezzo_inferiore(prodotti, prezzo, categoria):
    prod_inferiore = []
    for prodotto in prodotti:
        if prodotto["prezzo"] < prezzo and prodotto["categoria"] == categoria:
            prod_inferiore.append(prodotto)
    return prod_inferiore

def main():
    prodotti = [
    {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
    {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
    {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
    {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
    {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
    {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
    ]

    categoriaX = input("Inserisci la categoria da confrontare: ")
    prezzoMax = int(input("Inserisci il prezzo da confrontare: "))
    prodotti_prezzo_inferiore = prezzo_inferiore(prodotti, prezzoMax, categoriaX)
    print(f"La lista dei prodotti con un prezzo inferiore a {prezzoMax} e con la categioria uguale a {categoriaX} è:\n{prodotti_prezzo_inferiore}")

if __name__=="__main__":
    main()