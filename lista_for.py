# Scorre la lista e quando trova una parola che inizia con 'c' stampa qualcosa

l = ["ciao", "python", "casa"]

for parola in l:
    if parola[0] == "c":
        print("!")


# Concatenare le parole della lista

l = ["ciao", "python", "casa"]
string = " "

for parola in l:
    string = string + " " + parola
print(string)

# un altro modo per fare questo esercizio

l = ["ciao", "python", "casa"]
string = l[0]

for parola in l[1:]:
    string = string + " " + parola
print(string)