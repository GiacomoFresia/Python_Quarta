ip = input("Inserisci un indirizzo IP: ")
# .split(SEP) è un metodo delle stringhe che suddivide una
# stringa cercando il carattere separatore SEP
ottetti_str = ip.split(".") 
print(ottetti_str)

ottetti = [] # Lista vuota
for s in ottetti_str:
    ottetti.append(int(s))

print(bin(ottetti[3]))

# Chiede all'utente il numero di bit, poi chiede 1 numero binario (stringhe)
# Se la lunghezza del numero binario inserito è minore del numero di bit
# Aggiungere a sinistra tanti 0 quanti bastano per arrivare al numero di bit

num = int(input("Inserisci il numero di bit: "))
binario = input("Inserisci un numero binario: ")

if lunghezza < num:
    print(num + ((8 - lunghezza) * 0))
elif lunghezza > num:
    print("Numero sbagliato di bit")
