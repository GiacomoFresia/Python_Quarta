# Realizzare un programma Python che converta un indirizzo ip in 
# una stringa binaria di 32 bit.

ip = input("Inserisci un indirizzo IP: ")
ottetti_str = ip.split(".")
print(ottetti_str)
ottetti = []
for s in ottetti_str:
    ottetti.append(int(s))
print(ottetti)

for i in ottetti_str:
    if ottetti_str[i] % 2 == 0:
        print("0")
    else:
        print("1")

print(ottetti_str)