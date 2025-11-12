# Crea un programma in Python che chiede all'utente il suo nome
# e lo stampa sempre con l'iniziale maiuscola

nome = input("Inserisci il nome: ")
nome_maiuscolo = nome[0].upper() + nome[1:]
print(nome_maiuscolo)


# Crea un programma in Python che chiede all'utente un numero intero
# e stampa se il numero è divisibile per 2, per 3 o per 5 (Hint: usare
# operatore % per il resto della divisione)

numero = int(input("Inserisci un numero intero: "))
if numero % 2 == 0:
    print(f"Il numero {numero} è divisibile per 2")
if numero % 3 == 0:
    print(f"Il numero {numero} è divisibile per 3")
if numero % 5 == 0:
    print(f"Il numero {numero} è divisibile per 5")


# Crea un programma in Python che chiede all'utente una frase e stampi
# la stringa un carattere si e uno no (caratteri alternati)

frase = input("Inserisci una frase: ")
frase_alternata = frase[::2]
print(f"La frase alternata è {frase_alternata}")


# Crea un programma in Python che chiede all'utente una frase e stampi
# la frase al contrario

frase = input("Inserisci una frase: ")
frase_inversa = frase[::-1]
print(f"La frase inversa è {frase_inversa}")