# L'utente inserisce in input una password
# Il programma stampa la password oscurata da *

password = input("Inserisci una password: ")
password_blanked = "*" * len(password)     # Lunghezza di password con len
print(f"Hai inserito la password: {password_blanked}")