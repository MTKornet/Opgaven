def List(bestand):
    Tekst = open(bestand, 'r')
    Inhoud=Tekst.readlines()
    Tekst.close()
    for term in Inhoud:
        ZEnter=term.strip()
        NaNu=ZEnter.split(',')
        print('{} heeft kaartnummer: {}'.format(NaNu[1],NaNu[0]))

Kaart=List('kaartnummers')
print(Kaart)
