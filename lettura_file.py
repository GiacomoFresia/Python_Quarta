file = open("./dati.csv", "r") # Oggetto file
righe = file.readlines() # Lista di stringhe che contiene le righe
file.close()
titoli = righe[0][0:-1].split(",")
print(titoli)

prima_riga = righe[0]

# Unpacking (spacchettamento)
titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
print(titolo1)

# Leggere tutte le altre righe del file e stamparle
# Usare un ciclo for pythonico 