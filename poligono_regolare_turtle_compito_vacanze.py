# Scrivere una funzione che disegni un poligono regolare dato il numero di lati e la lunghezza
# del lato.
# Esempi di chiamata:
# poligono(4, 100) # quadrato
# poligono(6, 80) # esagono
# poligono(8, 60) # ottagono

import turtle

def main():
    lati = int(input("Inserisci il numero di lati: "))
    lunghezza = 100
    angolo = 360 / lati
    for i in range(lati):
        turtle.forward(lunghezza)
        turtle.left(angolo)
    turtle.mainloop()

if __name__ == "__main__":
    main()