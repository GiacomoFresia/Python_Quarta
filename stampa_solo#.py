# leggere un file e stampare solo le righe che iniziano con #

file = open("./nomeFile", "r")
contenuto = file.readlines()
for riga in contenuto:
    if riga[0] == '#':
        print(riga)
file.close(file)