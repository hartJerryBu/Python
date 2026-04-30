cislo = 1
seznam_cisel = [cislo]
while cislo < 1000:
    vysledek = seznam_cisel[-1] * 2 + 1
    seznam_cisel.append(vysledek)
    cislo = vysledek
print(seznam_cisel)
