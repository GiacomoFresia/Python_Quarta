print("Premi A per inserire.")
print("Premi B per modificare.")
print("Premi C per cancellare.")

tasto = input("-> ")
tasto = tasto.upper() # Trasforma il tasto in maiuscolo (sia un singolo carattere che una frase)
# upper() e lower() non sono funzioni ma sono METODI
# .lower() trasforma tutto in minuscolo

if tasto == "A":
    print("L'utente vuole inserire")
elif tasto == "B":
    print("L'utente vuole modificare")
elif tasto == "C":
    print("L'utente vuole cancellare")
else:
    print("Tasto non valido")