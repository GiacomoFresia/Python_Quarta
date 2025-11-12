# In Python possiamo delimitare con "" oppure con ''
stringa = "Ciao mondo!"
print(stringa)

# Esempio di indicizzazione della stringa
print(f"L'ultimo carattere della stringa è {stringa[-1]}")   # -1 sarebbe l'ultimo carattere

# Esempio di slicing delle stringhe (modo di tagliare le stringhe / estrarre porzioni di stringa)
print(f"La sottostringa 2-5 è {stringa[2:5]}.")   # L'indice di sinistra è incluso, quello di destra è escluso (il 5 è escluso, mi prende il 2,3,4 ossia a, o e lo spazio)

nome = "Mario"
cognome = "Rossi"
# Concatenazione tra stringhe
x = nome + " " + cognome    # X è una stringa (vengono sommate(concatenate) le 2 stringhe)
print(x)

# Assegnazione multipla(vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"

# Concatenazione di una stringa con se stessa più volte(stampa il nome per 5 volte)
y = nome*5
print(y)

y = (nome + " ")*5
print(y)
