# Scrivere una funzione che disegni un poligono regolare dato il numero di lati e la lunghezza
# del lato.
# Esempi di chiamata:
# poligono(4, 100) # quadrato
# poligono(6, 80) # esagono
# poligono(8, 60) # ottagono

import turtle

def sposta(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def poligono (n, lung):
    angolo = 360 / n
    for _ in range(n):
        turtle.forward(lung)
        turtle.left(angolo)

def main():
    nPoligoni = 4
    lato = 90
    shift = 180
    x_0, y_0 = -340, -lato/2
    for i in range(nPoligoni):
        y = y_0
        x = x_0 + shift * i
        sposta(x,y)
        poligono(i + 3, lato)

if __name__ == "__main__":
    main()