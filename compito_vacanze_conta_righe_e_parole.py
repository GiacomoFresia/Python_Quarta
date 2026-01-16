# Leggere un file di testo e stampare: numero di righe, numero di parole, numero di
# caratteri (esclusi gli spazi).

file = open("testo_compito_vacanze.txt", "r", encoding='utf-8')
testo = file.read()
file.close()

righe = testo.split("\n")
num_righe = len(righe)
parole = testo.split()
num_parole = len(parole)
num_caratteri = 0
for c in testo:
    if c != " " and c != "\n":
        num_caratteri = num_caratteri + 1
print(f"Numero righe: {num_righe}")
print(f"Numero parole: {num_parole}")
print(f"Numero caratteri: {num_caratteri}")