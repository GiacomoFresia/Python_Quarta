a = input("Inserisci una stringa: ")
a = a.lower()
if a == a[::-1]:
    print("Ok")
else:
    print("La stringa non è polindroma")

n = int(input("Inserisci un numero: "))
if n >= 0:
    for i in range(n+1):
        print(i * i, end = " ")