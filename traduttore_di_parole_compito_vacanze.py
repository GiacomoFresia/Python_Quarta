# Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se
# una parola non è nel dizionario, lasciarla invariata.

dizionario = {
"ciao": "hello",
"mondo": "world",
"casa": "house",
"gatto": "cat",
"cane": "dog",
"libro": "book",
"albero": "tree"
}
frase = "ciao mondo il gatto è in casa"
frase_tradotta = ""
frase = frase.split()

for parola in frase:
    if parola in dizionario:
        frase_tradotta = frase_tradotta + dizionario[parola] + " "
    else:
        frase_tradotta = frase_tradotta + parola + " "
print(f"La frase tradotta è: {frase_tradotta}")