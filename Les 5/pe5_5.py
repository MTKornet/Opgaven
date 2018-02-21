def Bestand(input):
    NBestand=open('Zin.txt','w')
    NBestand.write(input)
    NBestand.close

def Gemiddelde(bestand):
    Aantal=0
    OBestand=open(bestand, 'r')
    zin=OBestand.read()
    OBestand.close

    woorden=zin.split()
    for lengte in woorden:
        if len(lengte)>0:
            Aantal=Aantal+len(lengte)
    gem=Aantal/len(woorden)
    return gem

Input=input('Voer een zin in!')
Bestand(Input)
print(Gemiddelde('Zin.txt'))
