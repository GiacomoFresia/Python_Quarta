# stampa il nome + lungo in termini di lettere

lista = ["Luca", "Mario", "Alice", "Giovanni"]

nmax = 0
n = ""

for nome in lista:
    n = len(nome)
    if n > nmax:
        nmax = n
        nomemax = nome
print(nomemax)


# data una lista crearne un altra con tutti i nomi in maiuscolo

lista = ["Luca", "Mario", "Alice", "Giovanni"]

lista2 = []

for name in lista:
    lista2.append(name.upper())
print(f"{lista2[::1]}")