#vizsgálja meg melyik a legnagyobb
f = open("nagyobbszam.txt", "r", encoding ="UTF-8")
lista = []
for sor in f:
    lista.append(sor.strip())
print(lista)
f.close()
nagyobb = ""
for sor in lista:
    if nagyobb < sor:
        nagyobb = sor
print(nagyobb)