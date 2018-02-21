def NList(bestand):
    Tekst = open(bestand, 'r')
    Inhoud=Tekst.readlines()
    Tekst.close()
    Lijst=[]
    for Nummer1 in Inhoud:
        Nummer2=Nummer1[0:6]
        Lijst.append(Nummer2)
    return Lijst

kaartnummers=NList('kaartnummers')
locatieMax=kaartnummers.index(max(kaartnummers))+1
Aantal=len(kaartnummers)

print('Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}'.format(Aantal,max(kaartnummers),locatieMax))