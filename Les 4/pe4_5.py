getallen=[4,5,3,-81]
def kwadraten_som(grondgetallen):
    totaal=0
    for getal in grondgetallen:
        if getal > 0:
            kwadraat=getal**2
            totaal=totaal+kwadraat
    return totaal
print(kwadraten_som(getallen))