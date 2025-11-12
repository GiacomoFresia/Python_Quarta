# Chiedere all'utente un numero intero, un carattere. Creare una stringa che sia quel 
# carattere ripetuto tante volte quante il numero inserito

numero = int(input("Inserisci un numero intero: "))
carattere = input("Inserisci un carattere: ")
stringa = carattere * numero
print(f"La stringa è {stringa}")