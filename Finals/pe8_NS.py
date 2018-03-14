def inlezen_beginstation(stations):
    'Opvragen beginstation'
    begin = input('Wat is uw begin station?')
    while begin not in stations:
        begin=input('Wat is uw begin station?')
    return begin

def inlezen_eindstation(stations,beginstation):
    'Opvragen eindstation'
    Index_Begin=stations.index(beginstation)
    eind = input('Wat is uw eind station?')
    while eind not in stations[Index_Begin:]:
        print('Deze trein komt niet in {}'.format(eind))
        eind = input('Wat is uw eind station?')
    return eind

def omroepen_reis(stations,beginstation,eindstation):
    'Printen van omroepen'
    Index_Begin=stations.index(beginstation)
    Index_Eind = stations.index(eindstation)
    Aantal_Stations=Index_Eind-Index_Begin
    Prijs=Aantal_Stations*5
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation,Index_Begin+1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, Index_Eind+1))
    print('De afstand bedraagt {} station(s).'.format(Aantal_Stations))
    print('De prijs van het kaartje is {} euro.'.format(Prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for tussenstations in stations[Index_Begin+1:Index_Eind]:
        print(' - {}'.format(tussenstations))
    print('Jij stapt uit in: {}'.format(eindstation))

stations=['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal',
          'Amsterdam Amstel','Utrecht Centraal','\'s-Hertogenbosch','Eindhoven','Weert',
          'Roermond','Sittard','Maastricht']
beginstation=inlezen_beginstation(stations)
eindstation=inlezen_eindstation(stations,beginstation)
omroepen_reis(stations,beginstation,eindstation)