def lijst(invoer):
    List=[]
    getallen=invoer.split('-')
    getallen.sort()
    for nummer in getallen:
        List.append(int(nummer))
    return List

def som(getallen):
    totaal=0
    for getal in getallen:
        totaal=totaal+getal
    return totaal

Reeks="5-9-7-1-7-8-3-2-4-8-7-9"
Lijst=(lijst(Reeks))
Maximum=max(Lijst)
Minimum=min(Lijst)
Aantal=len(Lijst)
Totaal=som(Lijst)
Gemiddelde=Totaal/len(Lijst)
print("Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} en Som van de getallen: {}\nGemiddelde: {}".format(Lijst,Maximum,Minimum,Aantal,Totaal,Gemiddelde))