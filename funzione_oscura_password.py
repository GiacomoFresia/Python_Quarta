# Fare la funzione oscura_password

def oscura_password(s):
    nCaratteri = len(s)
    return s[0] + ((nCaratteri -1) * '*')

lista = ["ciao", "unoduetre"]
passwordOscurata = []
for password in lista:
    passwordOscurata.append(oscura_password(password))
print(passwordOscurata)