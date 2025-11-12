# Prima lettera della password deve essere visibile e il resto *

password = input("Inserisci una password: ")
password_blanked = password[0] + "*" * (len(password) -1)     # Lunghezza di password con len
print(f"Hai inserito la password: {password_blanked}")

password = input("Inserisci una password: ")
password_blanked = password[0] + "*" * (len(password) -2) + password[-1]
print(f"Hai inserito la password: {password_blanked}")

password = input("Inserisci una password: ")
password_blanked = "*" * (len(password))
print(f"Hai inserito la password: {password_blanked}")